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


Variables, expressions et énoncés
=================================

Valeurs et types
----------------

Une valeur est l'une des choses de base avec lesquelles un programme fonctionne,
comme une lettre ou un numéro. Les valeurs que nous avons vues jusqu'ici sont 1, 2,
et 'Hello, World!'.

Ces valeurs appartiennent à différents types: 2 est un entier, et 'Hello, World!'C'est une corde, dit parce qu’il contient une « chaîne » de lettres. Vous (et l'interprète) pouvez identifier strings parce qu'ils sont enfermés dans des guillemets.

Si vous ne savez pas quel type de valeur a une valeur, l'interprète peut vous le dire.


1. Philosophie et Syntaxe de base
=================================

Typage dynamique
----------------
Python est un langage à typage dynamique fort. Vous n'avez pas besoin de déclarer le type d'une variable lors de sa création. Le type est déduit à l'exécution.

.. code-block:: python

   age = 25          # int
   nom = "Alice"     # str
   est_actif = True  # bool

   # Le type peut changer dynamiquement
   age = "Vingt-cinq"

.. note::
   Bien que dynamique, Python supporte les *Type Hints* (annotations de type) très utiles pour la documentation et l'analyse statique :
   ``def saluer(nom: str) -> str:``

L'Indentation comme structure
-----------------------------
Contrairement à d'autres langages qui utilisent des accolades ou des mots-clés pour délimiter les blocs de code, Python utilise **l'indentation stricte** (généralement 4 espaces).

.. code-block:: python

   if age == 25:
       print("Âge exact")
       # Ce code est dans le bloc if
   print("Fin de la vérification") # Ce code est hors du bloc

2. Structures de contrôle
=========================

Conditions
----------
Les conditions utilisent ``if``, ``elif`` (sinon si), et ``else``. Les opérateurs logiques s'écrivent en toutes lettres : ``and``, ``or``, ``not``.

.. code-block:: python

   if age > 18 and est_actif:
       print("Accès autorisé")
   elif not est_actif:
       print("Compte inactif")
   else:
       print("Accès refusé")

Boucles : L'itération par défaut
--------------------------------
En Python, la boucle ``for`` est conçue pour itérer directement sur des collections (tableaux, listes, etc.), sans gérer manuellement d'index.

.. code-block:: python

   noms = ["Alice", "Bob", "Charlie"]

   # Itération directe sur les éléments
   for nom in noms:
       print(nom)

   # Si vous avez absolument besoin d'un index numérique, utilisez range()
   for i in range(5):  # 0 à 4
       print(i)

3. Structures de données natives
================================

Les Listes (Tableaux dynamiques)
--------------------------------
Les listes sont mutables et peuvent contenir des types mixtes.

.. code-block:: python

   valeurs = [10, 20, 30]
   valeurs.append(40)      # Ajout à la fin
   premier = valeurs[0]    # Accès par index
   dernier = valeurs[-1]   # Index négatif : part de la fin

Les Dictionnaires (Tables de hachage)
-------------------------------------
Ils stockent des paires clé-valeur. Très utilisés et optimisés en Python.

.. code-block:: python

   etudiant = {
       "id": 12345,
       "nom": "Tremblay",
       "cours": ["Math", "Prog"]
   }

   print(etudiant["nom"])
   etudiant["note"] = 95 # Ajout d'une nouvelle clé

4. Fonctions et Paramètres
==========================

Les fonctions sont définies avec le mot-clé ``def``. Python gère de manière très flexible les arguments par défaut et nommés.

.. code-block:: python

   def calculer_moyenne(notes, bonus=0):
       if not notes:
           return 0
       return (sum(notes) / len(notes)) + bonus

   # Appel standard
   moyenne1 = calculer_moyenne([80, 90, 85])

   # Appel avec argument nommé (très utile pour la lisibilité)
   moyenne2 = calculer_moyenne(notes=[70, 75], bonus=5)

5. Programmation Orientée Objet (POO)
=====================================

Tout en Python est un objet. La définition d'une classe est simple, mais nécessite de comprendre le mot-clé ``self``, qui doit être le premier paramètre de toute méthode d'instance. Il représente l'instance courante de la classe.

.. code-block:: python

   class Utilisateur:
       # Le constructeur s'appelle toujours __init__
       def __init__(self, nom, age):
           self.nom = nom        # Attribut public
           self._age = age       # Attribut "protégé" par convention (un souligné)
           self.__id = 123       # Attribut "privé" (name mangling)

       def afficher_profil(self):
           print(f"Utilisateur: {self.nom}")

   # Instanciation (pas de mot-clé "new")
   user1 = Utilisateur("Alice", 25)
   user1.afficher_profil()

.. warning::

    Python n'a pas de modificateurs d'accès stricts (public, private). Le simple souligné ``_`` est une convention indiquant qu'un attribut ne devrait pas être manipulé de l'extérieur, mais le langage ne le bloque pas techniquement.
