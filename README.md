Dépôt accompagnant le cours 201-SN4-RE
======================================

Démarrage
---------

1.  Clonez ce dépôt sur votre poste en utilisant Git.

1.  Ouvrez-votre éditeur sur ce dépôt

1.  Assurez-vous d'avoir [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
    
    Powershell

    ```ps1
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

1.  Ouvrez un terminal dans le répertoire du dépôt

1.  Installer les dépendances

    ```
    uv sync
    ```

1.  Exécuter l'ensemble des scripts d'assurance qualité

    ```
    uv run nox
    ```

Aide-mémoire
------------

1.  Ajouter des dépendancesW

    ```
    uv add --dev pytest
    ```

1.  Exécuter le programme

    ```
    uv run intropy
    ```

Permissions
-----------

Le contenu de ce dépôt est distribué sous différentes licences:

- Le code source (Python) est distribué sous licence
  _BSD-2-Clause Plus Patent License_ (`BSD-2-Clause-Patent`).

- La documentation, notes de cours, diapos, et autres contenus didactiques
  sont distribués sous licence
  _Creative Commons Attribution Share Alike 4.0 International_ (`CC-BY-SA-4.0`).

Copyright (c) 2026 Charles Bouchard-Légaré
