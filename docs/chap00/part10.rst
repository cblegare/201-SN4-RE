Tuples
======

Un tuple est immuable
----------------------

Un **tuple** est une séquence de valeurs qui, tout comme une liste, peut contenir des éléments de n'importe quel type, indexés par des entiers. La grande différence est que les tuples sont **immuables** (*immutable*).

Syntaxiquement, un tuple est une liste de valeurs séparées par des virgules :

.. code:: python

    >>> t = 'a', 'b', 'c', 'd', 'e'

Bien que ce ne soit pas obligatoire, il est courant de placer les tuples entre parenthèses :

.. code:: python

    >>> t = ('a', 'b', 'c', 'd', 'e')

Pour créer un tuple avec un seul élément, vous devez inclure une virgule finale :

.. code:: python

    >>> t1 = ('a',)
    >>> type(t1)
    <class 'tuple'>

Sans la virgule, Python traite ``('a')`` comme une simple chaîne entre parenthèses :

.. code:: python

    >>> t2 = ('a')
    >>> type(t2)
    <class 'str'>

Pour créer un tuple vide, vous utilisez des parenthèses vides :

.. code:: python

    >>> t = ()
    >>> type(t)
    <class 'tuple'>

Vous pouvez également utiliser la fonction intégrée ``tuple`` pour créer un tuple à partir d'une séquence :

.. code:: python

    >>> t = tuple('lump')
    >>> t
    ('l', 'u', 'm', 'p')

La plupart des opérateurs de listes fonctionnent également sur les tuples. L'opérateur de crochet indexe un élément, et l'opérateur de tranche extrait une section :

.. code:: python

    >>> t = ('a', 'b', 'c', 'd', 'e')
    >>> t[0]
    'a'
    >>> t[1:3]
    ('b', 'c')

Cependant, si vous essayez de modifier l'un des éléments du tuple, vous obtiendrez une erreur, car les tuples sont immuables :

.. code:: python

    >>> t[0] = 'A'
    TypeError: 'tuple' object does not support item assignment

Bien que vous ne puissiez pas modifier les éléments d'un tuple, vous pouvez remplacer un tuple par un autre :

.. code:: python

    >>> t = ('A',) + t[1:]
    >>> t
    ('A', 'b', 'c', 'd', 'e')

Assignation de tuples
---------------------

Il est souvent utile de permuter les valeurs de deux variables. Dans les langages traditionnels, vous devez utiliser une variable temporaire. En Python, l'affectation de tuples permet une syntaxe élégante :

.. code:: python

    >>> x, y = y, x

Le côté gauche est une séquence de variables ; le côté droit est une séquence de expressions. Chaque valeur du côté droit est assignée à la variable correspondante du côté gauche. Toutes les expressions du côté droit sont évaluées avant toute affectation.

Le nombre de variables à gauche et le nombre de valeurs à droite doivent être égaux :

.. code:: python

    >>> x, y = 1, 2, 3
    ValueError: too many values to unpack

Plus généralement, l'affectation de tuples fonctionne avec n'importe quelle séquence.

Les tuples comme valeurs de retour
----------------------------------

Une fonction ne peut retourner qu'une seule valeur, mais si cette valeur est un tuple, l'effet est le même que de retourner plusieurs valeurs. Par exemple, la fonction ``divmod`` prend deux entiers et renvoie un tuple de deux valeurs : le quotient et le reste.

.. code:: python

    >>> t = divmod(7, 3)
    >>> t
    (2, 1)

Vous pouvez également utiliser l'affectation de tuples pour stocker les éléments séparément :

.. code:: python

    >>> quotient, reste = divmod(7, 3)
    >>> quotient
    2
    >>> reste
    1

Un autre exemple est la fonction ``min_max``, qui trouve à la fois la plus petite et la plus grande valeur d'une séquence :

.. code:: python

    def min_max(t):
        return min(t), max(t)

Tuples à longueur variable d'arguments
--------------------------------------

Les fonctions peuvent prendre un nombre variable d'arguments. Un paramètre commençant par un astérisque (``*``) **rassemble** les arguments en un tuple. Par exemple, ``somme_tous`` prend un nombre quelconque d'arguments et calcule leur somme :

.. code:: python

    def somme_tous(*args):
        return sum(args)

    >>> somme_tous(1, 2, 3)
    6

À l'inverse, l'opérateur ``*`` peut être utilisé pour **répartir** une séquence en tant qu'arguments d'une fonction :

.. code:: python

    >>> t = (7, 3)
    >>> divmod(*t)
    (2, 1)

Listes et tuples
----------------

La fonction ``zip`` prend deux ou plusieurs séquences et les combine en un itérateur de tuples, où chaque tuple contient un élément de chaque séquence.

.. code:: python

    >>> s = 'abc'
    >>> t = [1, 2, 3]
    >>> zip(s, t)
    <zip object at 0x...>

Pour utiliser le résultat de ``zip``, vous pouvez le convertir en liste de tuples ou utiliser une boucle ``for`` :

.. code:: python

    >>> list(zip(s, t))
    [('a', 1), ('b', 2), ('c', 3)]

Si les longueurs des séquences sont différentes, le résultat s'arrête à la longueur de la plus courte.

Vous pouvez parcourir les éléments d'une liste de tuples en utilisant une affectation de tuples dans une boucle ``for`` :

.. code:: python

    t = [('a', 1), ('b', 2), ('c', 3)]
    for lettre, nombre in t:
        print(nombre, lettre)

Dictionnaires et tuples
-----------------------

Les dictionnaires possèdent une méthode appelée ``items`` qui renvoie une séquence de paires clé-valeur sous forme de tuples.

.. code:: python

    >>> d = {'a': 0, 'b': 1, 'c': 2}
    >>> t = list(d.items())
    >>> t
    [('a', 0), ('c', 2), ('b', 1)]

À l'inverse, vous pouvez utiliser une liste de tuples pour initialiser un nouveau dictionnaire :

.. code:: python

    >>> d = dict([('a', 0), ('b', 1), ('c', 2)])
    >>> d
    {'a': 0, 'b': 1, 'c': 2}

La combinaison de ``dict`` et ``zip`` permet de créer rapidement des dictionnaires :

.. code:: python

    >>> d = dict(zip('abc', range(3)))
    >>> d
    {'a': 0, 'b': 1, 'c': 2}

Glossaire
---------

.. glossary::

    tuple
    tuple
        Une séquence immuable d'éléments.

    affectation de tuples
    tuple assignment
        Une affectation qui associe un tuple de valeurs à une séquence de variables.

    rassembler
    gather
        Le processus de regroupement d'arguments à longueur variable dans un tuple.

    répartir
    scatter
        Le processus de traitement d'une séquence de valeurs en tant qu'arguments de fonction.


Exercices
---------

.. topic:: Exercice 1

    Écrivez une fonction appelée ``somme_tous`` qui prend un nombre quelconque de nombres en arguments et renvoie leur somme.

.. topic:: Exercice 2

    Modifiez un programme de tri de mots de sorte qu'il trie les mots par longueur, du plus long au plus court, et que les mots de même longueur soient triés par ordre alphabétique.

.. topic:: Exercice 3

    Écrivez une fonction appelée ``frequence_lettres`` qui prend une chaîne de caractères et renvoie un dictionnaire des lettres comptées, triées par ordre décroissant de fréquence.

.. topic:: Exercice 4

    Un anagramme est un mot formé en réorganisant les lettres d'un autre mot. Écrivez un programme qui lit une liste de mots à partir d'un fichier et imprime tous les ensembles de mots qui sont des anagrammes entre eux.
