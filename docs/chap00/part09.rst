Dictionnaires
=============

Un **dictionnaire** est un type de données intégré à Python qui ressemble à une liste, mais il est plus général. Dans une liste, les indices doivent être des entiers ; dans un dictionnaire, les indices peuvent être de presque n'importe quel type.

Un dictionnaire contient une collection de **indices**, appelés **clés**, et chaque clé est associée à une **valeur**. L'association d'une clé et d'une valeur est appelée une **paire clé-valeur** ou un élément.

La fonction ``dict`` crée un nouveau dictionnaire sans aucun élément. Comme les crochets pour les listes, les accolades (``{`` et ``}``) représentent un dictionnaire littéral.

.. code:: python

    >>> anglais_francais = dict()
    >>> anglais_francais
    {}
    >>> eng2fr = {'un': 'one', 'deux': 'two', 'trois': 'three'}
    >>> eng2fr
    {'un': 'one', 'deux': 'two', 'trois': 'three'}

L'ordre des paires clé-valeur n'est pas prévisible. Pour afficher un élément, vous utilisez une clé entre crochets :

.. code:: python

    >>> print(eng2fr['deux'])
    'two'

Si la clé n'est pas dans le dictionnaire, vous obtenez une exception :

.. code:: python

    >>> print(eng2fr['quatre'])
    KeyError: 'quatre'

La fonction ``len`` renvoie le nombre de paires clé-valeur :

.. code:: python

    >>> len(eng2fr)
    3

L'opérateur ``in`` vous indique si une clé apparaît dans le dictionnaire :

.. code:: python

    >>> 'un' in eng2fr
    True
    >>> 'one' in eng2fr
    False

L'opérateur ``in`` recherche parmi les clés, pas les valeurs. Pour vérifier si une valeur apparaît dans un dictionnaire, vous pouvez utiliser la méthode ``values``, qui renvoie les valeurs sous forme de collection, puis utiliser l'opérateur ``in`` :

.. code:: python

    >>> valeurs = eng2fr.values()
    >>> 'one' in valeurs
    True

Le dictionnaire comme ensemble de compteurs
------------------------------------------

Supposons que vous receviez une chaîne de caractères et que vous souhaitiez compter combien de fois chaque lettre y apparaît. Une façon de faire est de créer un dictionnaire avec les lettres comme clés et les compteurs comme valeurs.

.. code:: python

    def histogramme(s):
        d = dict()
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

La fonction ``histogramme`` prend une chaîne de caractères et renvoie un dictionnaire contenant les caractères uniques comme clés et leurs fréquences comme valeurs.

Les dictionnaires possèdent une méthode appelée ``get`` qui prend une clé et une valeur par défaut. Si la clé est dans le dictionnaire, ``get`` renvoie la valeur correspondante ; sinon, elle renvoie la valeur par défaut. Par exemple :

.. code:: python

    def histogramme(s):
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        return d

Boucles et dictionnaires
------------------------

Si vous utilisez une instruction ``for`` avec un dictionnaire, elle parcourt les clés du dictionnaire. Par exemple, cette fonction imprime chaque clé et sa valeur associée :

.. code:: python

    def imprimer_histogramme(h):
        for c in h:
            print(c, h[c])

Les clés ne sont pas dans un ordre trié. Pour parcourir les clés dans un ordre trié, vous pouvez utiliser la fonction ``sorted`` :

.. code:: python

    for c in sorted(h):
        print(c, h[c])

Recherche inversée
------------------

Étant donné un dictionnaire ``d`` et une clé ``k``, il est facile de trouver la valeur correspondante : ``v = d[k]``. C'est une **recherche**.

Mais que faire si vous avez une valeur et que vous voulez trouver la clé correspondante ? C'est une **recherche inversée** (*reverse lookup*).

.. code:: python

    def recherche_inverse(d, v):
        for k in d:
            if d[k] == v:
                return k
            raise LookupError('La valeur ne redevient pas une clé dans le dictionnaire.')

Dictionnaires et listes
-----------------------

Les listes peuvent apparaître comme des valeurs dans un dictionnaire. Par exemple, si vous voulez inverser un histogramme (obtenir un dictionnaire qui associe des fréquences à des listes de lettres ayant cette fréquence), vous pouvez écrire :

.. code:: python

    def inverser_dictionnaire(d):
        inverse = dict()
        for k in d:
            v = d[k]
            if v not in inverse:
                inverse[v] = [k]
            else:
                inverse[v].append(k)
        return inverse

Les listes peuvent être des valeurs dans un dictionnaire, mais **les listes ne peuvent pas être des clés**. Les clés doivent être **hachables** (*hashable*), ce qui signifie qu'elles possèdent une fonction de hachage immuable. Les types mutables comme les listes ne sont pas hachables.

Mémoïsation
-----------

Si vous avez exécuté la fonction de Fibonacci récursive, vous avez peut-être remarqué que plus le nombre grandit, plus le temps de calcul explose. Cela est dû au fait que la fonction recalcule les mêmes valeurs encore et encore.

Une solution consiste à stocker les résultats déjà calculés dans un dictionnaire, souvent appelé **mémo** (*memo*). Un dictionnaire utilisé de cette façon est un exemple de **mémoïsation** (*memoization*) :

.. code:: python

    connnu = {0: 0, 1: 1}

    def fibonacci(n):
        if n in connu:
            return connu[n]
        res = fibonacci(n-1) + fibonacci(n-2)
        connnu[n] = res
        return res

Variables globales
----------------

Dans l'exemple ci-dessus, la variable ``connu`` est créée en dehors de la fonction, ce qui en fait une **variable globale** (*global variable*). Vous pouvez lire les variables globales à l'intérieur d'une fonction, mais si vous voulez les modifier ou leur réassigner une valeur, vous devez utiliser le mot-clé ``global`` :

.. code:: python

    compteur = 0

    def evaluer():
        global compteur
        compteur += 1

Glossaire
---------

.. glossary::

    dictionnaire
    dictionary
        Une collection de paires clé-valeur qui associe des clés à des valeurs.

    clé
    key
        Un objet qui apparaît dans un dictionnaire associé à une valeur.

    paire clé-valeur
    key-value pair
        La représentation d'un élément dans un dictionnaire.

    table de hachage
    hash table
        L'algorithme sous-jacent utilisé pour implémenter les dictionnaires en Python.

    hachable
    hashable
        Un type qui possède une fonction de hachage. Les types immuables sont hachables.

    mémo
    memo
        Un dictionnaire utilisé pour stocker les résultats de calculs déjà effectués afin d'éviter le double travail.

    variable globale
    global variable
        Une variable définie en dehors de toutes les fonctions, accessible partout.


Exercices
---------

.. topic:: Exercice 1

    Écrivez une fonction qui lit les mots d'un fichier et les stocke comme clés dans un dictionnaire. Utilisez ensuite l'opérateur ``in`` pour vérifier rapidement et efficacement si un mot est présent dans le dictionnaire.

.. topic:: Exercice 2

    Utilisez la méthode ``setdefault`` pour écrire une version plus concise de la fonction ``histogramme`` présentée dans ce chapitre.

.. topic:: Exercice 3

    Modifiez la fonction ``inverser_dictionnaire`` pour qu'elle utilise ``setdefault`` au lieu d'une instruction conditionnelle.

.. topic:: Exercice 4

    Si vous avez une fonction qui prend une liste et utilise la méthode ``in`` pour trouver les doublons, la complexité temporelle augmente rapidement. Écrivez une version plus rapide qui utilise un dictionnaire pour éliminer les doublons d'une liste de manière efficace.
