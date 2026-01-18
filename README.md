# Task Manager CLI

[![CI](https://github.com/KazDoesCode/Project-based-learning/actions/workflows/ci.yaml/badge.svg)](https://github.com/KazDoesCode/Project-based-learning/actions/workflows/ci.yaml)  
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

Un gestionnaire de tâches simple en ligne de commande, écrit en Python.  
Permet d'ajouter, supprimer, lister, filtrer et mettre à jour des tâches stockées dans un fichier JSON.  
Projet conçu dans le cadre de l'apprentissage de Python, Git, CI/CD, Docker et bonnes pratiques de développement.

---

## Fonctionnalités

- Ajouter une tâche : `python main.py add "Titre de la tâche"`
- Supprimer une tâche : `python main.py delete <task_id>`
- Mettre à jour le statut d'une tâche : `python main.py update <task_id> <done|in_progress|not_done>`
- Lister toutes les tâches : `python main.py list`
- Filtrer les tâches par statut : `python main.py list <done|in_progress|not_done>`

Les statuts disponibles sont :  
- `done`   
- `in_progress`   
- `not_done` 

---

## Installation

1. Cloner le dépôt :

```bash
git clone git@github.com:KazDoesCode/Project-based-learning.git
cd Project-based-learning
```

2. Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Installer les dépendances :

```bash
pip install -r requirements.txt
```
## Docker

Construire et exécuter le container :
```bash
docker build -t task-manager .
docker run --rm task-manager list
```

Avec Docker Compose (si multi-services) :
```bash
docker-compose up
docker-compose down
```
## Tests

Tests unitaires avec pytest :
```bash
pytest tests/
```

GitHub Actions CI :

-Déclenchement sur push/pull request sur les branches master et feature/tests.
-Installation des dépendances.
-Exécution des tests automatiquement.

## Structure du projet
.
├─ main.py               # Point d'entrée CLI
├─ tasks.py              # Logique des tâches
├─ storage.py            # Load/save JSON factorisé
├─ tests/                # Tests unitaires
│  ├─ __init__.py
│  └─ test_tasks.py
├─ data.json             # Fichier de stockage des tâches
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ .github/workflows/ci.yaml

## À venir / améliorations possibles

-Amélioration de la gestion des erreurs CLI.
-Passage à une base SQLite.
-Tests d'intégration CLI + stockage.
-Packaging Python (setup.py).
-Déploiement API ou Web.