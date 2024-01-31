[![Badge pypi version](https://img.shields.io/pypi/v/iut-pe?style=for-the-badge&logo=pypi&logoColor=white&labelColor=%230073B7&color=gray)](https://pypi.org/project/iut-pe/)
[![Coverage](https://img.shields.io/gitlab/pipeline-coverage/roubine%2Fiut-pe?gitlab_url=https%3A%2F%2Fgricad-gitlab.univ-grenoble-alpes.fr%2F&job_name=pages&branch=main&style=for-the-badge&logo=python&logoColor=white)](https://roubine.gricad-pages.univ-grenoble-alpes.fr/iut-pe/coverage/)
[![Badge exemples](https://img.shields.io/badge/Exemples%20de%20fiches-blue?logo=latex&style=for-the-badge&color=darkgreen)](https://gricad-gitlab.univ-grenoble-alpes.fr/roubine/iut-pe/-/jobs/artifacts/main/browse/public/pdf?job=pages)

# IUT poursuites d'études
Automatisation de la création de fiches poursuites d'études avec ScoDoc

## Installation
Installation des dépendances système (ubuntu/debian)
```bash
sudo apt update
sudo apt install texlive-full
```

### Installation avec pip
Création de l'environnement virtuel
```bash
python3 -m venv ~/.virtualenvs/iut-pe
source  ~/.virtualenvs/iut-pe/bin/activate
```
Installation
```bash
pip install iut-pe
```

### Installation depuis les sources
Création de l'environnement virtuel
```bash
python3 -m venv ~/.virtualenvs/iut-pe
source  ~/.virtualenvs/iut-pe/bin/activate
pip install -U pip
pip install poetry
```

Installation du module (les sources sont ici téléchargées dans un dossier `~/src`)
```
git clone https://gricad-gitlab.univ-grenoble-alpes.fr/roubine/iut-pe.git
cd ~/src/iut-pe
poetry install
```

## Usage
### Fichier de configuration
Le fichier de configuration est au format YAML et par défaut doit dans le chemin courant (là où la commande est exécutée).
L'option `--config` permets d'utiliser un autre chemin lors de l'execution de la commande.

Voici toutes les entrées du fichier:
```yaml
scodoc:
    url: https://scodoc.tromblon-univ.fr # L'URL de base du server web ScoDoc
    departement: MYDEPT # L'acronyme du département
    login: idlee # Votre login
    password: SpamEggs # Votre mot de passe
    groupe: Parcours # La catégorie des groupes dont les noms seront utilisé pour déterminer le parcours de l'étudiant si plusieurs parcours sont présents
latex:
    name: Eric Idle # Vorte nom
    city: Tromblon les Jons poussants # La ville où est faite la fiche
    address:
        - IUT 42 # L'adresse de l'IUT
        - Université de Tromblon # sur autant de lignes que vous voulez
        - eric.idle@tromblon-univ.fr # avec le mail et le téléphone si vous voulez
paths:
    database: ./etudiants.json # le chemin du ficher base de données (défaut: ./etudiants.json)
    latex: ./latex # le chemin vers le dossier latex (défaut: ./latex)
    pdf: ./pdf # le chemin vers le dossier pdf (défaut: ./pdf)
    logo: ./logo.png # le chemin vers le logo (défaut: ./logo.png)
    sign: ./sign.png # le chemin vers la signature (défaut: ./sign.png)
```

### Les  Commandes
`iut-pe` fournit 3 lignes commandes:
- `iut-pe-ping`: teste si la connection avec ScoDoc fonctionne.
- `iut-pe-fetch`: récupère les informations de ScoDoc et de construire la base de données.
- `iut-pe-build`: crée les fichiers pdf à l'aide de LaTex.

### Exemple de configuration
Toutes les données sont dans le dossier `~/travail/poursuite-etudes` (éviter les espaces).
Pour simplifier **on travaille dans le fichier courant** où on dépose le fichier de configuration.

```bash
cd ~/travail/poursuites-etudes/
cat config.yml
# scodoc:
#     url: https://iut1-scodocbut.u-ga.fr
#     departement: GCCD
#     login: monlogin
#     password: monmdp
#     groupe: Parcours
# latex:
#     name: Emmanuel Roubin
#     city: Saint Martin d'hères
#     address:
#         - IUT 1 de Grenoble
#         - Département Génie Civil - Construction Durable
#         - Domaine Universitaire
#         - 151, rue de la papeterie
#         - BP 67
#         - 38402 Saint-Martin d’Hères cedex
#         - iut1.gccd.de@univ-grenoble-alpes.fr
```

Puis on source l'environnement python.
```bash
source  ~/.virtualenvs/iut-pe/bin/activate
```

**Étaper 1:** vérification de la connection. Si vous voyez s'afficher `pong!` c'est que la connection à ScoDoc fonctionne.
```bash
iut-pe-ping
# ping?
# pong! 
```

**Étape 2:** création de la base de données.

Pour tous les étudiants des semestres courants
```bash
iut-pe-fetch
```
Uniquement pour le semestre 42 (id à récupérer dans l'URL de ScoDoc)
```bash
iut-pe-fetch --semestre 42
```
Uniquement pour l'étudiant 421 (etudid à récupérer dans l'URL de ScoDoc)
```bash
iut-pe-fetch --etudid 421
```
Cela doit créer un fichier `json` dans le dossier courant. Dans notre cas:
```bash
~/travail/poursuites-etudes/
    config.yml
    etudiants.json
```

**Étape 3:** construire les fichiers pdf.
Pour cette étape on peut rajouter 2 fichiers `png` dans le dossier courant:
- `~/travail/poursuites-etudes/logo.png`: le logo de l'université
- `~/travail/poursuites-etudes/sign.png`: la signature du DE

On construit les fichiers pdf des étudiants présents dans la base de données avec la commande:
```bash
iut-pe-build
```
Ce qui créé 2 dossiers avec les sources latex (afin de pouvoir les modifier à la main et les recompiler à souhait) et les fichiers pdf. Ici dans le cas où un seul étudiant est dans la base de données on a l'architecture suivante:
```bash
~/travail/poursuites-etudes/
    config.yml
    etudiants.json
    pdf
        Nom_Prenom_421.pdf
    latex
        421.tex
        421.tex.log
        421.aux
        421.log
```


### Notes
- Si vous ne souhaitez pas travailler dans le dossier courant il faudra utiliser l'option `--config` pour localiser le fichier de configuration et renseigner les variables `paths` dans le fichier de configuration.
- L'option `--reset` permet de remettre à 0 la base de données des étudiants afin de ne pas recompiler toutes les fiches à chaque fois.
- Il n'est pas obligatoire d'ajouter un logo ou une signature. Le fiche peut être générée sans.
- Aucun fichier pdf n'est supprimé automatiquement.

## Disclamer
- Cet outil est en phase de développement. Il est uniquement testé sur la configuration du département GCCD de l'IUT1 de Grenoble. La probabilité qu'il ne fonctionne pas pour d'autres configurations est relativement élevée. Merci d'utiliser les [issues](https://gricad-gitlab.univ-grenoble-alpes.fr/roubine/iut-pe/-/issues) en cas de problèmes.
- Pas de support pour d'autres systèmes d'exploitation que Linux avec Debian/Ubuntu.
