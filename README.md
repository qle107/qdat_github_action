# QDat

[![qdat_ci](https://github.com/qle107/qdat_github_action/actions/workflows/qdat_ci.yml/badge.svg)](https://github.com/qle107/qdat_github_action/actions/workflows/qdat_ci.yml)

Pipeline CI/CD personnel : metriques statistiques, tests unitaires multi-versions,
rapport JSON archive puis deploiement SSH vers `~/QDat/` sur le serveur.

## Contenu

| Fichier | Role |
| --- | --- |
| `qdat_metrics.py` | Fonctions `moyenne`, `mediane`, `etendue`, `normaliser` |
| `qdat_job.py` | Genere `rapport.json` (metriques + environnement + presence de la cle API) |
| `test_qdat_metrics.py` | 8 tests unitaires, y compris les cas d'erreur |

## Pipeline (`.github/workflows/qdat_ci.yml`)

1. **tests** — matrice Python 3.10 / 3.12, `compileall` puis `unittest discover`.
2. **rapport** — execute `qdat_job.py` et publie `rapport.json` en artefact.
3. **deploiement** — uniquement sur `main` : `scp` des fichiers vers `~/QDat/`,
   puis les tests sont rejoues **sur le serveur** pour valider le deploiement.

`concurrency` annule les runs obsoletes ; le mot de passe transite par la variable
d'environnement `SSHPASS` (jamais ecrit sur le disque du runner).

## Secrets et variables requis

| Nom | Type | Description |
| --- | --- | --- |
| `SSH_HOST` | variable | IP ou nom d'hote du serveur |
| `SSH_USER` | variable (optionnel) | Utilisateur SSH, `ubuntu` par defaut |
| `SSH_PASSWORD` | secret | Mot de passe SSH |
| `SECRET_API_KEY` | secret | Cle lue par `qdat_job.py` |

## Lancer en local

```bash
python -m unittest discover -s . -p "test_*.py" -v
python qdat_job.py
```
