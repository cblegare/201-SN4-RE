###################
Chapitre 0 : Python
###################

.. topic:: Avant de commencer

    Avant de commencez à appendre Python, vous aurez besoin d'outils pour
    écrire votre code et le compiler.

    Pour à la fois gérer différentes versions de Python, installer et
    isoler vos dépendances, compiler et conditionner vos modules et structurer
    vos projets, installez `uv`_ et vérifiez que la commande suivante affiche
    la version de `uv` installée et retourne *exit code* de `0`:

    .. code::

        uv --version

    Étant donné un projet existant, installez tout ce qu'il faut avec une seule
    commande:

    .. code::

        uv sync

    Pour gérer vos fichier et rédiger votre code, à la fois
    `Visual Studio Code` (VSCode) et JetBrains PyCharm_ sont des excellents éditeurs
    pour Python.

    Pour simplifier l'apprentissage, ce guide présentera des instructions à
    exécuter en ligne de commandes dans un terminal (comme BaSH_ ou PowerShell_).
    Si vous connaissez des manière d'arriver aux même résultats en utilisant une
    interface graphique, n'hésitez pas à vous en servir.

    .. _uv: https://docs.astral.sh/uv/
    .. _PyCharm: https://www.jetbrains.com/pycharm/
    .. _Visual Studio Code: https://code.visualstudio.com/
    .. _BaSH: https://fr.wikipedia.org/wiki/Bourne-Again_shell
    .. _PowerShell: https://en.wikipedia.org/wiki/PowerShell

Le but de ce chapitre est que vous appreniez à coder comme un informaticien,
jonglant avec des pratiques et approches tirées des mathématiques, du langage
et de l'ingénierie.
Nous essaierons non seulement de développer des compétences techniques de
programmation, mais aussi des compétences de conception et de communication
de systèmes parfois complexes ou abstraits.

.. toctree::
    :glob:

    part*
