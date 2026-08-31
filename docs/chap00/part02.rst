Variables, expressions et énoncés
=================================

Valeurs et types
----------------

Une valeur est l'une des choses de base avec lesquelles un programme fonctionne,
comme une lettre ou un numéro. Les valeurs que nous avons vues jusqu'ici sont 1, 2,
et 'Hello, World!'.

Ces valeurs appartiennent à différents types: ``2`` est un entier, et
``"Hello, World!"`` est une chaîne de caractère (*string*).
Vous (et l'interprète) pouvez identifier ces string parce qu'ils sont
placées entre des guillemets (``"``).

Si vous ne savez pas quel type de valeur a une valeur, l'interprète peut
vous aider.

.. code:: python

    >>> type("Hello World!")
    <class 'str'>
    >>> type(17)
    <class 'int'>
    >>> type(1.3)
    <class 'float'>
    >>> type('17')
    <class 'str'>
    >>> type('3.2')
    <class 'str'>


Variables
---------

L'une des fonctionnalités les plus puissantes d'un langage de programmation
est la capacité de manipuler des variables. Une variable est un nom qui fait
référence à une valeur.

Une instruction d'affectation (*assignment statement*) crée de nouvelles
variables et leur donne des valeurs :

.. code:: python

   >>> message = "Voici quelque chose de différent"
   >>> n = 17
   >>> pi = 3.1415926535897932

Cet exemple effectue trois affectations.
La première assigne une chaîne à une nouvelle variable nommée ``message`` ;
la deuxième donne l'entier ``17`` à ``n`` ;
la troisième assigne la valeur (approximative) de π à ``pi``.

Le type d'une variable est le type de la valeur à laquelle elle fait référence.

.. code-block:: python

    >>> type(message)
    <class 'str'>
    >>> type(n)
    <class 'int'>
    >>> type(pi)
    <class 'float'>

Noms de variables et mots-clés
------------------------------

Les programmeurs choisissent généralement des noms significatifs pour leurs
variables. Ils documentent à quoi sert la variable.

Les noms de variables peuvent être aussi longs que vous le souhaitez.
Ils peuvent contenir des lettres et des chiffres, mais ils doivent commencer
par une lettre. Il est légal d'utiliser des majuscules, mais c'est une
bonne idée de commencer les noms de variables par une minuscule
(vous verrez pourquoi plus tard).

Le caractère de soulignement (*underscore*), ``_``, peut apparaître dans
un nom. Il est souvent utilisé dans les noms composés de plusieurs mots,
comme ``mon_nom`` ou ``vitesse_hirondelle_a_vide``.

Si vous donnez à une variable un nom illégal, vous obtenez une erreur de syntaxe :

.. code:: text

    >>> 76trombones = 'big parade'
    File "<stdin>", line 1
        76trombones = 'big parade'
        ^
    SyntaxError: invalid decimal literal
    >>> more@ = 1000000
      File "<stdin>", line 1
        more@ = 1000000
              ^
    SyntaxError: invalid syntax
    >>> class = 'Zymologie théorique avancée'
        File "<stdin>", line 1
        class = 'Zymologie théorique avancée'
                ^
    SyntaxError: invalid syntax

``76trombones`` est illégal car il ne commence pas par une lettre.
``more@`` est illégal car il contient un caractère illégal, ``@``.
Mais quel est le problème avec ``class`` ?

Il s'avère que ``class`` est l'un des mots-clés de Python.
L'interpréteur utilise les mots-clés pour reconnaître la structure
du programme, et ils ne peuvent pas être utilisés comme noms de variables.

Python 3.14 possède 31 mots-clés :

``False``, ``None``, ``True``, ``and``, ``as``, ``assert``,
``async``, ``await``, ``break``, ``class``, ``continue``, ``def``, ``del``,
``elif``, ``else``, ``except``, ``finally``, ``for``, ``from``, ``global``,
``if``, ``import``, ``in``, ``is``, ``lambda``, ``nonlocal``, ``not``, ``or``,
``pass``, ``raise``, ``return``, ``try``, ``while``, ``with`` et ``yield``.

Vous voudrez peut-être garder cette liste à portée de main.
Si l'interpréteur se plaint d'un de vos noms de variables et que vous ne
savez pas pourquoi, vérifiez s'il figure dans cette liste.
Vous pouvez aussi simplementdemander à l'interpréteur de vous la donner:

.. code:: python

    >>> import keyword
    >>> print(keyword.kwlist)
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Opérateurs et opérandes
-----------------------

Les opérateurs sont des symboles spéciaux qui représentent des calculs comme
l'addition et la multiplication. Les valeurs auxquelles l'opérateur est
appliqué s'appellent des opérandes.

Les opérateurs ``+``, ``-``, ``*``, ``/``, ``//`` et ``**`` effectuent
l'addition, la soustraction, la multiplication, la division,
la division entière, et l'exponentiation,
comme dans les exemples suivants :

.. code:: python

   20+32
   hour-1
   hour*60+minute
   minute/60
   5**2
   (5+9)*(15-7)

Dans d'autres langages, ``^`` est utilisé pour l'exponentiation,
mais en Python, c'est un opérateur bit à bit (XOR).

Expressions et instructions
---------------------------

Une expression est une combinaison de valeurs, de variables et d'opérateurs.
Une valeur seule est considérée comme une expression, de même qu'une variable,
donc ce qui suit sont toutes des expressions légales :

.. code:: python

   17
   x
   x + 17

Une instruction (*statement*) est une unité de code que l'interpréteur Python
peut exécuter.

Techniquement, une expression est aussi une instruction,
mais il est probablement plus simple de les considérer comme des choses
différentes. La différence importante est qu'une expression a une valeur ;
une instruction n'en a pas.


Mode interactif et mode script
------------------------------

L'un des avantages de travailler avec un langage interprété est que vous
pouvez tester des morceaux de code en mode interactif avant de les mettre
dans un script.

Par exemple, si vous utilisez Python comme calculatrice, vous pourriez taper :

.. code:: python

   >>> miles = 26.2
   >>> miles * 1.61
   42.182

La première ligne assigne une valeur à ``miles``, mais n'a pas d'effet
visible. La deuxième ligne est une expression, donc l'interpréteur l'évalue
et affiche le résultat. Nous apprenons donc qu'un marathon fait environ
42 kilomètres.

Mais si vous tapez le même code dans un script et l'exécutez,
vous n'obtenez aucune sortie du tout.
En mode script, une expression seule n'a aucun effet visible.
Python évalue l'expression, mais il n'affiche pas la valeur à moins
qu'on ne lui demande :

.. code:: python

   miles = 26.2
   print(miles * 1.61)

Ce comportement peut être déroutant au début.

Un script contient généralement une séquence d'instructions.
S'il y a plus d'une instruction, les résultats apparaissent un par un au
fur et à mesure de l'exécution.

Par exemple, le script :

.. code:: python

   print(1)
   x = 2
   print(x)

produit la sortie :

.. code:: text

   1
   2

L'instruction d'affectation ne produit aucune sortie.

.. topic:: Exercice 1

    Tapez les instructions suivantes dans l'interpréteur Python pour voir ce
    qu'elles font :

    .. code:: python

        5
        x = 5
        x + 1

    Maintenant, mettez ces mêmes instructions dans un script et exécutez-le.
    Quelle est la sortie ? Modifiez le script en transformant chaque expression
    en un appel à la fonction ``print``, puis exécutez-le à nouveau.

Ordre des opérations
--------------------

Lorsqu'il y a plus d'un opérateur dans une expression, l'ordre d'évaluation
dépend des règles de priorité.
Pour les opérateurs mathématiques,
Python suit la convention mathématique (PEMDAS) :

*   **Parenthèses** ont la plus haute priorité et peuvent être utilisées
    pour forcer une expression à s'évaluer dans l'ordre de votre choix.
*   **Exponentiation** a la priorité suivante.
*   **Multiplication** et **Division** ont la même priorité, qui est plus
    élevée que l'**Addition** et la **Soustraction** (qui ont également la
    même priorité entre elles).
*   Les opérateurs avec la même priorité sont évalués de gauche à droite
    (à l'exception de l'exponentiation).

Opérations sur les chaînes de caractères
----------------------------------------

En général, on ne peut pas effectuer d'opérations mathématiques sur les
chaînes de caractères, même si elles ressemblent à des nombres.

L'opérateur ``+`` fonctionne avec les chaînes, mais il effectue une
concaténation, ce qui signifie joindre les chaînes en les liant bout à bout.
Par exemple :

.. code:: python

   first = 'Paru'
   second = 'line'
   print(first + second)

La sortie de ce programme est ``Paruline``.

L'opérateur ``*`` fonctionne également sur les chaînes ;
il effectue la répétition. Par exemple, ``'Spam'*3`` donne ``'SpamSpamSpam'``.

Commentaires
------------

À mesure que les programmes deviennent plus gros et plus complexes,
ils deviennent plus difficiles à lire.
Pour cette raison, il est bon d'ajouter des notes à vos programmes pour
expliquer en langage naturel ce que fait le programme.
Ces notes s'appellent des commentaires,
et ils commencent par le symbole ``#`` :

.. code:: python

   # calcule le pourcentage de l'heure écoulée
   percentage = (minute * 100) / 60

Vous pouvez également mettre des commentaires à la fin d'une ligne :

.. code:: python

   percentage = (minute * 100) / 60  # pourcentage d'une heure

Tout ce qui va du ``#`` jusqu'à la fin de la ligne est ignoré.

Les commentaires sont très utiles pour expliquer les caractéristiques non
évidentes du code (le *pourquoi* plutôt que le *comment*).


Débogage
--------

À ce stade, l'erreur de syntaxe la plus probable que vous ferez est un nom
de variable illégal, comme l'utilisation de mots-clés ou de caractères interdits.

L'erreur d'exécution la plus probable est d'essayer d'utiliser une variable
avant de lui avoir assigné une valeur (une ``NameError``).
Cela peut arriver si vous orthographiez mal un nom de variable.
N'oubliez pas que les variables sont sensibles à la casse.

L'erreur sémantique la plus fréquente vient souvent de l'ordre des opérations.


Glossaire
---------

.. glossary::

    valeur
        L'une des unités de base des données qu'un programme manipule.

    type
        Une catégorie de valeurs.

    entier
    integer
        Un type qui représente des nombres entiers.

    virgule flottante
    float
        Un type qui représente des nombres avec des parties fractionnaires.

    chaîne de caractères
    string
        Un type qui représente des séquences de caractères.

    variable
        Un nom qui fait référence à une valeur.

    instruction
    statement
        Une section de code qui représente une commande ou une action.

    affectation
    assignment
        Une instruction qui assigne une valeur à une variable.

    diagramme d'état
    state diagram
        Une représentation graphique d'un ensemble de variables et des valeurs
        auxquelles elles font référence.

    mot-clé
    keyword
        Un mot réservé utilisé par le compilateur pour analyser un programme.

    opérateur
    operator
        Un symbole spécial qui représente un calcul simple.

    opérande
    operand
        L'une des valeurs sur lesquelles un opérateur agit.

    division entière
    floor division
        L'opération qui divise deux nombres et coupe la partie fractionnaire.

    expression
        Une combinaison de variables, d'opérateurs et de valeurs qui représente
        une valeur de résultat unique.

    évaluer
    evaluate
        Simplifier une expression en effectuant les opérations pour obtenir
        une valeur unique.

    règles de priorité
    rules of precedence
        L'ensemble des règles régissant l'ordre dans lequel les expressions
        sont évaluées.

    concaténer
    concatenate
        Joindre deux opérandes bout à bout.

    commentaire
    comment
        Information dans un programme destinée aux lecteurs du code source.

Exercices
---------

.. topic:: Exercice 2

    Supposons que nous exécutions les instructions d'affectation suivantes :

    .. code:: python

        width = 17
        height = 12.0
        delimiter = '.'

    Pour chacune des expressions suivantes, déterminez la valeur de
    l'expression et le type (de la valeur de l'expression) :

    1.  ``width/2``
    2.  ``width/2.0``
    3.  ``height/3``
    4.  ``1 + 2 * 5``
    5.  ``delimiter * 5``


.. topic:: Exercice 3

    Pratiquez l'utilisation de l'interpréteur Python comme calculatrice :

    1.  Le volume d'une sphère de rayon r est 4/3 π r³. Quel est le volume
        d'une sphère de rayon 5 ?

    2.  Supposons que le prix de couverture d'un livre soit de 24,95 $,
        mais que les librairies obtiennent une réduction de 40%.
        Les frais d'expédition sont de 3 $ pour le premier exemplaire et
        de 75 cents pour chaque exemplaire supplémentaire.
        Quel est le coût total de gros pour 60 exemplaires ?

    3.  Si je quitte ma maison à 6h52 et que je cours 1 mile à un rythme
        facile (8:15 par mile), puis 3 miles à un rythme soutenu
        (7:12 par mile) et 1 mile à un rythme facile à nouveau,
        à quelle heure rentré-je chez moi pour le petit-déjeuner ?
