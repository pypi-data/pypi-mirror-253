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

from iut_pe.helpers import ScodocAPI, Student, FileHandler, default_parser
import os
import subprocess


def ping():
    """Fiche poursuite d'études ScoDoc
    iut-pe-ping: permet de tester la connection avec l'API de ScoDoc.
    """
    # args parser
    parser = default_parser("iut-pe-ping", ping.__doc__)
    args = parser.parse_args()
    config = FileHandler(args.config).load(config=True)
    api = ScodocAPI(**config["scodoc"])
    api.ping()


def fetch(config, lazy=True, reset=False, EID=None, SID=None):
    #######################
    # Initialise database #
    #######################
    database = FileHandler(config["paths"].get("database", "./etudiants.json"))
    if reset:
        database.delete()
    try:
        students_db = database.load()
    except Exception:
        print(f"Initialisation du fichier {database}")
        students_db = {}
        database.dump(students_db)
    print(f"Base de données: {database}")

    ####################################
    # get list of students from ScoDoc #
    ####################################
    api = ScodocAPI(**config["scodoc"])
    if EID:
        print(f"Récupération des données pour l'étudiant {EID}")
        students = api.call(f"etudiants/etudid/{EID}")
    elif SID:
        print(f"Récupération des données pour les étudiants du semestre {SID}")
        students = api.call(f"formsemestre/{SID}/etudiants")
    else:
        print("Récupération des données pour les étudiants de tous les semestres courants", end="... ")
        students = api.call("etudiants/courants")
        print(f" -> {len(students)} students found.")

    ###################################################
    # loop over the students to build up the database #
    ###################################################
    for i, student in enumerate(students):
        print(f'{i + 1:03d}/{len(students):03d} {student["civilite"]} {student["nom"]} {student["prenom"].title()} [{student["id"]}]')

        if lazy and str(student["id"]) in students_db:
            print(" -> student already in the database.")
            continue

        try:
            semesters = api.call(f'etudiant/etudid/{student["id"]}/formsemestres')
        except Exception as e:
            print(f"ERREUR: étudiant non trouvé ({e})")
            continue

        student["semestres"] = []
        for semester in semesters:
            print(f'\t{semester["titre_num"]} {semester["date_debut"]} -> {semester["date_fin"]} [{semester["formsemestre_id"]}]')
            marks = api.call(f'etudiant/etudid/{student["id"]}/formsemestre/{semester["id"]}/bulletin')
            semester["resultats"] = {k: marks[k] for k in ["ues", "ues_capitalisees"]}
            semester["groups"] = marks["semestre"]["groupes"]
            semester["absences"] = marks["semestre"]["absences"]
            student["semestres"].append(semester)
        students_db[str(student["id"])] = student
        database.dump(students_db)


def fetch_script():
    """Récupère les informations étudiants depuis ScoDoc et les enregistre dans une base de donnée locale."""
    # args parser
    parser = default_parser("iut-pe-fetch", fetch.__doc__)
    parser.add_argument("--lazy", action="store_true", help="Ignore les étudiants déjà dans la base de données.")
    parser.add_argument("--reset", action="store_true", help="Reconstruit la base de données à partir de zéro.")
    parser.add_argument("--etudid", dest="EID", default=None, type=int, help="Enter l'identifiant ScoDoc d'un étudiant pour uniquement récupérer les informations de cet étudiant.")
    parser.add_argument("--semestreid", dest="SID", default=None, type=int, help="Enter l'identifiant ScoDoc d'un semestre pour uniquement récupérer les informations des étudiants de ce semestre.")
    args = parser.parse_args()

    ######################
    # configuration file #
    ######################
    config = FileHandler(args.config).load(config=True)

    fetch(config, reset=args.reset, EID=args.EID, SID=args.SID, lazy=args.lazy)


#########
# BUILD #
#########


def build(students, config, lazy=False, skip_latex=False):
    ###################
    # latex/pdf paths #
    ###################
    latex = FileHandler(config["paths"].get("latex", "latex"), is_file=False)
    latex.create_path()
    print(f"LaTex path: {latex}")
    pdf = FileHandler(config["paths"].get("pdf", "pdf"), is_file=False)
    pdf.create_path()
    print(f"PDF path: {pdf}")

    this_dir = os.path.dirname(os.path.abspath(__file__))
    template = FileHandler([this_dir, "static", "template.tex"])
    logo = FileHandler(config["paths"].get("logo", "logo.png"))
    if logo:
        print(f"Logo: {logo}")
    else:
        print("Le logo n'a pas été trouvé.")
    sign = FileHandler(config["paths"].get("sign", "sign.png"))
    if sign:
        print(f"Signature: {sign}")
    else:
        print("La signature n'a pas été trouvée.")

    ###############################################
    # loop of students to build and compile latex #
    ###############################################
    student_n = len(students)
    for student_i, student_dict in enumerate([v for k, v in students.items()]):
        student = Student(student_dict)
        print(f"{student_i + 1:03d}/{student_n:03d} {student} ({len(student.semesters)} semestres)")

        if not len(student.semesters):
            print(" -> pas de semestres retenus.")
            continue

        # pdf files
        pdf_from = FileHandler(os.path.join(latex.path, student.pdf_from))
        pdf_to = FileHandler(os.path.join(pdf.path, student.pdf_to))

        # skip already compiled files
        if lazy and bool(pdf_to):
            print(" déjà compilé")
            continue

        # variables to define in latex template
        student.init_latex_variables(partition=config["scodoc"].get("groupe", "Parcours"))
        # student.show_latex_variables()

        # create latex main file from the template (SED)
        replacements = [("SED_VARIABLES", student.define_latex_variables()), ("SED_FICHE_NUMBER", student.student_id), ("SED_ADDRESS", "\\\\\n    ".join(config["latex"]["address"])), ("SED_CITY", config["latex"]["city"]), ("SED_NAME", config["latex"]["name"]), ("SED_LOGO", f'{"" if logo else "%"}{chr(92)}includegraphics[height=2cm]{{{logo.file}}}'), ("SED_SIGN", f'{"" if sign else "%"}{chr(92)}includegraphics[height=2cm]{{{sign.file}}}')]

        tex = ""
        with template.read() as f:
            tex = f.read()
            for a, b in replacements:
                tex = tex.replace(a, b)

        student_tex = FileHandler([latex.path, f"{student.student_id}.tex"])
        with student_tex.write() as f:
            f.write(tex)

        if skip_latex:
            return

        # compile with pdflatex
        command = [f"pdflatex -halt-on-error -output-directory={latex.path} {student_tex.file} > {student_tex.file}.log"]
        subprocess.run(command, shell=True, check=True, text=True)

        # move pdf
        command = [f"mv {pdf_from} {pdf_to}"]
        subprocess.run(command, shell=True, check=True, text=True)

        print(f"-> {pdf_to}")


def build_script():
    """Créé et compile les fiches latex à partir des informations étudiants collectées avec iut-pe-fetch."""

    # args parser
    parser = default_parser("iut-pe-build", build.__doc__)
    parser.add_argument("--lazy", action="store_true", help="Ignore les pdf déjà présents.")
    args = parser.parse_args()

    # load configuration file configuration file
    config = FileHandler(args.config).load(config=True)

    # open students db
    database = FileHandler(config["paths"].get("database", "./etudiants.json"))
    if not database:
        print(f"La base de données {database} n'a pas été trouvée.")
        print("Utiliser en premier lieu la commande iut-pe-fetch afin de construire la base de données.\n")
        raise FileNotFoundError("Database not found")
    print(f"Base de données: {database}")
    etudiants = database.load()

    # run build latex
    build(etudiants, config, lazy=args.lazy)
