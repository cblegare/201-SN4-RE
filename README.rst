#####################################################
420-611-BT - Algèbre linaire et géométrie vectorielle
#####################################################

Ce dépôt contient les sources de matériel pour le cours
**420-611-BT - Algèbre linéaire et géométrie vectorielle**.


Compilation
===========

Ces instructions mène à la compilation des documents.

Prérequis
---------

Ce dépôt utilise [`uv`](https://docs.astral.sh/uv/) pour la résolution et
l'installation de certaines dépendances. Le logiciel doit être installé
et utilisable dans un terminal. Vérifiez votre installation:

```shell
uv --version
```

Installez les dépendances de scripts avec la commande suivante:

```shell
uv sync
```

Vous aurez aussi besoin d'une installation LaTeX fonctionnelle.


Exécuter les scripts de vérification et compilation
---------------------------------------------------

Exécutez tous les scripts avec la commande suivante:

```shell
uv run nox
```
