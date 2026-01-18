
---

### **LEARNINGS.md**

```markdown
# Ce que j'ai appris avec le projet Task Manager CLI

## Python

- Manipulation de fichiers JSON (`json.load`, `json.dump`)
- Factorisation de fonctions communes (`load_tasks`, `save_tasks`)
- List comprehension et mapping (`STATUS_MAP`)
- Création de fonctions modulaires (`add_tasks`, `delete_tasks`, `update_task`, `list_tasks`, `filter_tasks`)

## CLI

- Lecture des arguments avec `sys.argv`
- Interface CLI simple et modulable
- Affichage formaté et fonction `display_tasks`

## Tests unitaires

- Pytest pour tester les fonctions
- Capturer la sortie CLI avec `io.StringIO`
- Organisation tests : setup, act, assert, cleanup

## Git

- Branches et merges (`feature/tests`, `feature/refactor`, `master`, `version/base`)
- Push/pull et workflow GitHub
- SSH key authentication pour GitHub

## CI/CD

- GitHub Actions pour automatiser tests unitaires
- Workflow déclenché sur push ou pull request
- Installation des dépendances et exécution de pytest

## Docker

- Création de Dockerfile pour containeriser l'application
- Build et run d’un container pour exécuter le CLI
- Différence entre image et container

## Bonnes pratiques

- Séparer logique métier et stockage
- Factoriser les fonctions répétitives
- Maintenir un code lisible et modulaire
- Commits fréquents et messages clairs
- Préparer le projet pour intégration continue et tests automatiques

---

## Objectifs futurs

- Ajouter tests d’intégration et couverture complète
- Transformer le projet en package installable
- Ajouter une interface web ou API
- Approfondir CI/CD et déploiement Docker multi-services
