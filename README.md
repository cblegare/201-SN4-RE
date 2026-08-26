Introduction à Python
=====================

1.  Clonez le dépôt suivant:

    ```
    git clone https://gitlab.com/cblegareprof/intropy
    ```

2.  Ouvrez-votre éditeur sur ce dépôt

3.  Assurez-vous d'avoir [`uv`](https://docs.astral.sh/uv/getting-started/installation/)

    ```ps1
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.12.6/install.ps1 | iex"
    ```

4.  Installer les dépendances
    
    ```
    uv sync
    ```
    
5.  Ajouter des dépendances

    ```
    uv add --dev pytest
    ```

6.  Exécuter les tests

    ```
    uv run pytest
    ```

7.  Exécuter le programme

    ```
    uv run intropy
    ```