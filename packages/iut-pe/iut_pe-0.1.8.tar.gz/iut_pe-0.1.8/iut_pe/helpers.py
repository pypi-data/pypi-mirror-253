#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import requests
import os
import urllib3

###########
# CLASSES #
###########


class ScodocAPI:
    """Handles scodoc API connection and requests"""

    def __init__(self, url=None, login=None, password=None, departement=None, **kargs):
        self.url = os.path.join(url, "ScoDoc")
        self.login = login
        self.password = password
        self.token = None
        self.departement = departement

    def __str__(self):
        return f"{self.login}@{self.url}"

    def call(self, path, post=False):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        if not self.token:
            # print("get token")
            self.get_token()

        url = self.url

        if self.departement:
            url = os.path.join(url, self.departement)

        url = os.path.join(url, "api")
        url = os.path.join(url, path)

        if post:
            # print(f"[POST] {url} ({self.token})")
            response = requests.post(url, headers={"Authorization": f"Bearer {self.token}"}, verify=False)
        else:
            # print(f"[GET] {url} ({self.token})")
            response = requests.get(url, headers={"Authorization": f"Bearer {self.token}"}, verify=False)

        response.raise_for_status()
        return response.json()

    def get_token(self):
        url = os.path.join(self.url, "api", "tokens")
        auth = (self.login, self.password)
        # print(f"[POST] {url} {auth}")
        response = requests.post(url, auth=auth, verify=False)
        response.raise_for_status()
        self.token = response.json()["token"]

    def ping(self):
        print("ping?")
        self.call("etudiants/courants")
        print("pong!")


class FileHandler:
    def __init__(self, path, is_file=True):
        from pathlib import Path
        import os

        if isinstance(path, list):
            path = os.path.join(*path)

        path = Path(path).expanduser().resolve()
        self.is_file = is_file
        if is_file:
            self.file = path
            path, _ = os.path.split(path)
            self.path = Path(path)
        else:
            self.file = None
            self.path = Path(path)

    def __str__(self):
        if self.file:
            return str(self.file)
        else:
            return str(self.path)

    def __bool__(self):
        if self.file:
            return self.file.exists()
        else:
            return self.path.exists()

    def create_path(self):
        if self:
            return
        self.path.mkdir(parents=True)

    def delete(self):
        print(f"Suppression du fichier {self.file}")
        if self:
            self.file.unlink()

    def read(self):
        if not self.is_file:
            return None
        return open(self.file, "r")

    def write(self):
        if not self.is_file:
            return None
        return open(self.file, "w")

    def dump(self, data):
        import json

        json.dump(data, self.write(), indent=4)

    def load(self, config=False):
        import json
        import yaml

        # load a simple json file
        if not config:
            return json.load(self.read())

        # load a configuration yaml file
        if not self:
            print(f"Le fichier de configuration n'a pas été trouvé à l'emplacement {self}.")
            print("Vérifier le chemin et utiliser l'option --config si besoin.\n")
            raise FileNotFoundError("File not found")

        config = yaml.safe_load(self.read())
        if config.get("paths") is None:
            config["paths"] = {}

        return config


class Student:
    def __init__(self, d: dict):
        # self.d = d
        self.student_id = str(d["id"])
        self.full_name = f'{d["nom"].upper()} {d["prenom"].title()}'
        self.pdf_from = f"{self.student_id}.pdf"
        self.pdf_to = f'{self.full_name.replace(" ", "_")}_{self.student_id}.pdf'
        self.latex_variables = {}

        self.last_step = max([s["semestre_id"] for s in d["semestres"]])

        def keep_semester(s):
            if self.last_step == 4:
                # but 2 remove s4
                if s["semestre_id"] == 4:
                    return False
            elif self.last_step > 4:
                # but 3 remove s5/s6
                if s["semestre_id"] > 4:
                    return False

            return len(s["resultats"]["ues"]) >= 5

        self.semesters = [Semester(s) for s in d["semestres"] if keep_semester(s)]

    def __str__(self):
        return f"{self.full_name} [{self.student_id}]"

    def get_but(self):
        return self.semesters[0].title

    def get_promotion(self):
        return self.semesters[0].start.split("/")[-1]

    def get_cursus(self, partition=None):
        cursus = []
        for semester in self.semesters:
            if len(semester.cursus) == 1:
                #  get cursus from semester cursus if only one available
                c = semester.cursus[0]["name"]
            else:
                # get parcours from group
                groups_with_partiton = [g for g in semester.groups if g["partition"] == partition]
                if not len(groups_with_partiton):
                    # can't find partition
                    continue
                c = groups_with_partiton[0]["name"]

            if c not in cursus:
                cursus.append(c)

            print(f"[debug] get cursus {semester}: {', '.join(cursus)} ({partition})")

        return " ".join(cursus)

    def get_semesters(self):
        return ", ".join([s.name for s in self.semesters])

    def get_title(self):
        if self.last_step <= 2:
            return "Fiche de réorientation BUT 1"

        if self.last_step <= 4:
            return "Fiche de réorientation BUT 2"

        return "Fiche de poursuite d'études BUT 3"

    def get_competences_dict(self):
        for semester in self.semesters:
            for competences in [_["competences"] for _ in semester.cursus if len(_["competences"]) == 5]:
                # for the first first sets of 5 competences in the first semester returns the dict with latex keys
                return {"bc" + "abcde"[i]: bc for i, bc in enumerate(competences)}

        print("[warning] Les 5 blocs de compétances n'ont pas été trouvés")
        return {}

    def get_results_dict(self):
        results = {}

        for semester in self.semesters:
            print(f"[debug] {semester} [{semester.latex_key}]")
            results[semester.latex_key] = semester.name

            # loop over the UE
            for ue_i, ue in enumerate(semester.ues):
                if ue_i > 4:
                    # sport, etc...
                    print(f'[debug] skipping ue {ue_i}: {ue["titre"]}')
                    continue

                # get ue marks
                ue_marks = ue["moyenne"]
                latex_key = semester.latex_key + "c" + "abcde"[ue_i]
                results[latex_key + "a"] = ue_marks["value"] if is_float(ue_marks["value"]) else "N/A"
                results[latex_key + "b"] = ue_marks["moy"] if is_float(ue_marks["moy"]) else "N/A"
                results[latex_key + "c"] = f'{ue_marks["rang"]}/{ue_marks["total"]}' if ue_marks["total"] else "N/A"

                # get ressources mark (overwrite for each eu but it should be the same)
                ue_ressources = ue["ressources"]
                r_keys = [r + f"{semester.semester_step}" for r in ["MAT", "COM", "ANG"]]
                for r_i, r_key in enumerate(r_keys):
                    latex_key = semester.latex_key + "r" + "abc"[r_i]
                    mark = ue_ressources.get(r_key, {"moyenne": "N/A"})["moyenne"]
                    if mark in ["~"]:
                        mark = "N/A"
                    results[latex_key] = mark

        return results

    def get_assiduity(self):
        abs_inj = 0
        abs_tot = 0
        abs_met = ""
        for semester in self.semesters:
            abs_inj += semester.assiduity["injustifie"]
            abs_tot += semester.assiduity["total"]
            abs_met = semester.assiduity["metrique"].split()[0]

        def _s(n):
            return "s" if n > 1 else ""

        return f"{abs_inj} absence{_s(abs_inj)} injustifiée{_s(abs_inj)} pour {abs_tot} absence{_s(abs_tot)} au total sur {len(self.semesters)} semestres ({abs_met} journée)."

    def get_alternant(self):
        fi = [s.modality.lower() in ["formation initiale", "fi"] for s in self.semesters]
        return "Formation Initiale" if all(fi) else "Alternant"

    def get_avis(self):
        if self.last_step <= 4:
            return False

        # first_quarter = []
        # first_half = []
        # for ue in [ue["moyenne"] for s in self.semesters for ue in s.ues if ue["moyenne"]["total"]]:
        #     p = float(str(ue["rang"]).split()[0]) / float(ue["total"])
        #     first_quarter.append(p <= 0.25)
        #     first_half.append(p <= 0.5)
        # #     print(ue)
        # #     print(p, ue)
        # # print(first_quarter)
        # # print(first_half)
        #
        # if all(first_quarter):
        #     return "Très favorable"
        #
        # if all(first_half):
        #     return "Favorable"

        # return "Neutre"

        n = 0
        p = 0
        for ue in [ue["moyenne"] for s in self.semesters for ue in s.ues if ue["moyenne"]["total"]]:
            p += float(str(ue["rang"]).split()[0]) / float(ue["total"])
            n += 1

        if p / float(n) < 0.25:
            return "Très favorable"

        elif p / float(n) < 0.5:
            return "Favorable"

        return "Neutre"

    def init_latex_variables(self, partition=None):
        self.latex_variables = {"titre": self.get_title(), "parcours": self.get_cursus(partition=partition), "alternant": self.get_alternant(), "candidat": self.full_name, "but": self.get_but(), "promotion": self.get_promotion(), "semestres": self.get_semesters(), "assiduite": self.get_assiduity()}
        for k, v in self.get_competences_dict().items():
            self.latex_variables[k] = v

        for k, v in self.get_results_dict().items():
            self.latex_variables[k] = v

        avis = self.get_avis()
        if avis:
            self.latex_variables["avis"] = avis

    def show_latex_variables(self):
        for k, v in self.latex_variables.items():
            print(f"Latex variable {k:<10}: {v}")
        # print(self.define_latex_variables())

    def define_latex_variables(self):
        return "".join([f"{chr(92)}def{chr(92)}{k}{{{v}}}\n" for k, v in self.latex_variables.items()])


class Semester:
    def __init__(self, d: dict):
        # for k, v in d.items():
        #     print(f"[debug] semester {k:<10}: {v}")

        self.semester_id = d["id"]
        self.semester_step = d["semestre_id"]
        self.title = d["titre_formation"]
        self.start = d["date_debut"]
        self.end = d["date_fin"]
        self.year = d["annee_scolaire"]
        self.modality = d["modalite"]
        self.name = f"S{self.semester_step} {self.year}"

        # latex keys
        self.latex_key = "sem" + "abcdef"[self.semester_step - 1]

        # dicts
        self.assiduity = d["absences"]

        # list of dict
        self.ues = [ue for i, ue in enumerate(d["resultats"]["ues"].values()) if i < 5]
        self.cursus = [{"code": p["code"], "name": p["libelle"], "competences": [k for k in p["annees"][str((self.semester_step + 1) // 2)]["competences"].keys()]} for p in d["parcours"]]
        self.groups = [{"name": g["group_name"], "partition": g["partition"]["partition_name"]} for g in d["groups"]]

    def __str__(self):
        return f"S{self.semester_step} [{self.semester_id}] {self.title} {self.start} -> {self.end}"


def is_float(n):
    try:
        float(n)
        return True
    except Exception:
        return False


def default_parser(prog, doc):
    import argparse

    parser = argparse.ArgumentParser(prog=prog, description=doc, epilog="---")
    parser.add_argument(
        "--config",
        default="config.yml",
        type=str,
        help="Chemin vers le fichier de configuration (défaut: répertoire courant).",
    )
    return parser


def handle_accents(s):
    import unicodedata

    # for now it just remove the accents :(
    return "".join((c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"))


def format_student_data(data, level="base"):
    keys_to_keep = {
        "base": ["id", "prenom", "civilite", "nom", "semestres"],
        # "semestres": ["semestre_id", "titre_formation", "date_debut", "date_fin", "annee_scolaire", "parcours", "resultats" "groups", "absences"],
        "semestres": ["semestre_id", "titre_formation", "date_debut", "date_fin", "annee_scolaire", "resultats"],
        # "parcours": ["annees", "libelle"],  # semestres
        # "annees": ["competences"],  # semestres / parcours
        # "competences": [],  # semestres / parcours / annees
        "resultats": ["ues"],  # semestres
        "ues": ["*"],  # semestres / resultats
    }.get(level, [])

    if "*" not in keys_to_keep:
        data = {k: v for k, v in data.items() if k in keys_to_keep}

    # format for ues level
    if level == "ues":
        new_data = []
        for ue_key, ue_values in data.items():
            print(ue_key)
            new_data.append(
                {
                    "code": ue_key,
                    "type": "BC",
                    "n": str(ue_key.split(".")[-1]),
                    "titre": ue_values["titre"],
                    "moyenne": ue_values["moyenne"]["value"],
                    "moyenne_promo": ue_values["moyenne"]["moy"],
                    "rang": ue_values["moyenne"]["rang"],
                    "total": ue_values["moyenne"]["total"],
                }
            )
            # if ue_key > 1:
            #     continue

        return new_data

    for k, v in data.items():
        if type(v) is int:
            data[k] = v
        elif type(v) is str:
            data[k] = handle_accents(v)
        elif type(v) is list and k in keys_to_keep:
            data[k] = [format_student_data(v1, level=k) for v1 in v]
        elif type(v) is dict and k in keys_to_keep:
            data[k] = format_student_data(v, level=k)

    return data
