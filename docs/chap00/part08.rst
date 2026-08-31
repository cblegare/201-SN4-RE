Listes
======

Une liste est une séquence
---------------------------

Comme une chaîne de caractères, une **liste** est une séquence de valeurs. Dans une chaîne, les valeurs sont des caractères ; dans une liste, elles peuvent être de n'importe quel type. Les valeurs qui composent une liste sont appelées des **éléments** (*items* ou *elements*).

Il y a plusieurs façons de créer une nouvelle liste ; la plus simple consiste à placer les éléments entre crochets (``[`` et ``]``) :

.. code:: python

    devoirs = ['maths', 'programmation', 'physique']
    nombres = [17, 123]
    vide = []

La première liste contient trois chaînes. La deuxième contient deux entiers. La liste vide ne contient aucun élément.

Une liste à l'intérieur d'une autre liste est dite **imbriquée** (*nested*).

.. code:: python

    elements = ['spam', 2.0, 5, [10, 20]]

Les listes sont mutables
------------------------

La syntaxe pour accéder aux éléments d'une liste est la même que pour les chaînes de caractères : l'opérateur de crochet. L'indice indique quel élément vous voulez (rappelez-vous que les indices commencent à 0) :

.. code:: python

    >>> devoirs[0]
    'maths'

Contrairement aux chaînes de caractères, les listes sont **mutables** (*mutable*), car vous pouvez modifier l'ordre des éléments d'une liste ou réassigner un élément particulier. En utilisant l'opérateur de crochet du côté gauche d'une affectation, vous pouvez mettre à jour un élément :

.. code:: python

    >>> nombres = [17, 123]
    >>> nombres[1] = 5
    >>> nombres
    [17, 5]

L'élément de ``nombres`` qui se trouvait à l'indice 1, qui était ``123``, est maintenant ``5``.

Vous pouvez également penser à une liste comme à une relation entre les indices et les éléments. Cette correspondance est appelée une **séquence** ; c'est pourquoi les listes sont des séquences.

L'opérateur ``in`` fonctionne également avec les listes :

.. code:: python

    >>> devoirs = ['maths', 'programmation', 'physique']
    >>> 'maths' in devoirs
    True
    >>> 'chimie' in devoirs
    False

Parcours d'une liste
--------------------

La boucle ``for`` est un moyen élégant de parcourir les éléments d'une liste. La syntaxe est la même que pour les chaînes de caractères :

.. code:: python

    for devoir in devoirs:
        mettre_a_jour(devoir)

Cela fonctionne bien si vous avez seulement besoin de lire les éléments de la liste. Mais si vous voulez écrire ou mettre à jour les éléments, vous avez besoin des indices. Une façon courante de le faire est d'utiliser les fonctions intégrées ``range`` et ``len`` :

.. code:: python

    for i in range(len(nombres)):
        nombres[i] = nombres[i] * 2

Cette boucle parcourt la liste et met à jour chaque élément. ``len`` renvoie le nombre d'éléments de la liste. ``range`` renvoie une liste d'indices de 0 à $n-1$, où $n$ est la longueur de la liste. À chaque itération, ``i`` prend l'indice de l'élément suivant. L'instruction d'affectation dans le corps utilise ``i`` pour lire l'ancien élément et lui assigner le nouveau.

Une boucle ``for`` sur une liste vide ne s'exécute jamais :

.. code:: python

    for x in []:
        print Ceci ne s'exécute jamais.

Opérations sur les listes
-------------------------

L'opérateur ``+`` concatène les listes :

.. code:: python

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> c = a + b
    >>> c
    [1, 2, 3, 4, 5, 6]

L'opérateur ``*`` répète une liste un nombre donné de fois :

.. code:: python

    >>> [0] * 4
    [0, 0, 0, 0]
    >>> [1, 2, 3] * 3
    [1, 2, 3, 1, 2, 3]

Tranches de listes
------------------

L'opérateur de tranche (*slice*) fonctionne également sur les listes :

.. code:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3]
    ['b', 'c']
    >>> t[:4]
    ['a', 'b', 'c', 'd']
    >>> t[3:]
    ['d', 'e', 'f']

Si vous omettez le premier indice, la tranche commence au début. Si vous omettez le second, elle va jusqu'à la fin. Si vous omettez les deux, la tranche est une copie de toute la liste :

.. code:: python

    >>> t[:]
    ['a', 'b', 'c', 'd', 'e', 'f']

Puisque les listes sont mutables, il est souvent utile de faire une copie avant de les modifier.

Une tranche du côté gauche d'une affectation peut modifier plusieurs éléments à la fois :

.. code:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3] = ['x', 'y']
    >>> t
    ['a', 'x', 'y', 'd', 'e', 'f']

Méthodes de listes
------------------

Python fournit des méthodes qui s'appliquent aux listes. Par exemple, ``append`` ajoute un nouvel élément à la fin d'une liste :

.. code:: python

    >>> t = ['a', 'b', 'c']
    >>> t.append('d')
    >>> t
    ['a', 'b', 'c', 'd']

``extend`` prend une liste comme argument et ajoute tous ses éléments :

.. code:: python

    >>> t1 = ['a', 'b', 'c']
    >>> t2 = ['d', 'e']
    >>> t1.extend(t2)
    >>> t1
    ['a', 'b', 'c', 'd', 'e']

``sort`` trie les éléments de la liste par ordre croissant :

.. code:: python

    >>> t = ['d', 'c', 'e', 'b', 'a']
    >>> t.sort()
    >>> t
    ['a', 'b', 'c', 'd', 'e']

La plupart des méthodes de listes modifient l'argument et retournent ``None`` ; elles sont conçues pour modifier des listes en place et non pour créer de nouvelles listes.

Suppression d'éléments
----------------------

Il existe plusieurs façons de supprimer des éléments d'une liste. Si vous connaissez l'indice de l'élément que vous voulez supprimer, vous pouvez utiliser ``pop`` :

.. code:: python

    >>> t = ['a', 'b', 'c']
    >>> x = t.pop(1)
    >>> t
    ['a', 'c']
    >>> x
    'b'

``pop` modifie la liste et renvoie l'élément qui a été supprimé. Si vous ne fournissez pas d'indice, il supprime et renvoie le dernier élément.

Si vous ne connaissez pas l'indice mais que vous connaissez l'élément à supprimer, vous pouvez utiliser ``remove`` :

.. code:: python

    >>> t = ['a', 'b', 'c']
    >>> t.remove('b')
    >>> t
    ['a', 'c']

La valeur de retour de ``remove`` est ``None``.

Pour supprimer plus d'un élément, vous pouvez utiliser une tranche avec une liste vide :

.. code:: python

    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> t[1:3] = []
    >>> t
    ['a', 'd', 'e', 'f']

Listes et chaînes
-----------------

Une chaîne de caractères est une séquence de caractères et une liste est une séquence de valeurs, mais une liste de caractères n'est pas la même chose qu'une chaîne. Pour convertir une chaîne en une liste de caractères, vous pouvez utiliser ``list`` :

.. code:: python

    >>> s = "spam"
    >>> t = list(s)
    >>> t
    ['s', 'p', 'a', 'm']

La fonction ``list`` sépare une chaîne en lettres individuelles. Si vous voulez diviser une chaîne en mots, vous pouvez utiliser la méthode ``split`` :

.. code:: python

    >>> s = "compter les mots de cette phrase"
    >>> t = s.split()
    >>> t
    ['compter', 'les', 'mots', 'de', 'cette', 'phrase']

À l'inverse, ``join`` est l'opposé de ``split``. Elle prend une liste de chaînes et concatène les éléments :

.. code:: python

    >>> t = ['compter', 'les', 'mots', 'de', 'cette', 'phrase']
    >>> delimiteur = ' '
    >>> delimiteur.join(t)
    'compter les mots de cette phrase'

Objets et valeurs
-----------------

Si nous exécutons ces affectations :

.. code:: python

    a = "banane"
    b = "banane"

Nous savons que ``a`` et ``b`` font référence à une chaîne de caractères, mais nous ne savons pas si elles font référence à la **même** chaîne. Il y a deux états possibles :

D'un côté, ``a`` et ``b`` peuvent se référer à deux objets différents qui ont la même valeur. De l'autre, ils peuvent se référer au même objet.

Pour vérifier si deux variables font référence au même objet, vous pouvez utiliser l'opérateur ``is`` :

.. code:: python

    >>> a = "banane"
    >>> b = "banane"
    >>> a is b
    True

Dans cet exemple, Python ne crée qu'une seule chaîne de caractères, et ``a`` et ``b`` font référence au même objet. Mais lorsque vous créez deux listes, vous obtenez deux objets :

.. code:: python

    >>> a = [1, 2, 3]
    >>> b = [1, 2, 3]
    >>> a is b
    False

Dans ce cas, on dit que les listes sont **équivalentes** (elles ont les mêmes valeurs), mais pas **identiques** (elles ne sont pas le même objet).

Le crénelage (Aliasing)
-----------------------

Si ``a`` fait référence à un objet et que vous assignez ``b = a``, alors les deux variables font référence au même objet :

.. code:: python

    >>> a = [1, 2, 3]
    >>> b = a
    >>> b is a
    True

L'association d'une variable à un objet est appelée une **référence**. Si un objet a plus d'une référence, il a plus d'un nom, et on dit que l'objet est **crénelé** (*aliased*).

Si l'objet crénelé est mutable, les modifications apportées à l'un des alias affectent l'autre :

.. code:: python

    >>> b[0] = 42
    >>> a
    [42, 2, 3]

Bien que ce comportement puisse être utile, il est source d'erreurs. De manière générale, il est plus sûr d'éviter le crénelage lors de la manipulation de listes mutables.

Arguments de listes
-------------------

Lorsque vous passez une liste à une fonction, la fonction reçoit une référence à la liste. Si la fonction modifie un paramètre de la liste, la modification est visible par l'appelant. Par exemple, ``supprimer_premier`` supprime le premier élément d'une liste :

.. code:: python

    def supprimer_premier(t):
        del t[0]

    lettres = ['a', 'b', 'c']
    supprimer_premier(lettres)
    print(lettres)
    ['b', 'c']

Débogage
--------

L'utilisation insouciante des listes (et d'autres objets mutables) peut entraîner de longues heures de débogage. Voici quelques pièges courants et des moyens de les éviter :

1. La plupart des méthodes de listes modifient l'argument et retournent ``None``. C'est l'inverse des méthodes de chaînes, qui retournent une nouvelle chaîne et laissent l'originale intacte.
2. Choisissez un style de conception et tenez-s'y. Certaines fonctions modifient les objets en argument, d'autres créent de nouveaux objets. Essayez de combiner ces approches avec prudence.
3. Faites des copies à l'aide de tranches (``t[:]``) si vous souhaitez modifier une liste tout en gardant l'originale intacte.

Glossaire
---------

.. glossary::

    liste
    list
        Une séquence de valeurs.

    élément
    item
        L'une des valeurs d'une liste (ou d'une autre séquence).

    mutable
    mutable
        La propriété d'une séquence dont les éléments peuvent être modifiés.

    crénelage
    aliasing
        Le fait que deux ou plusieurs variables fassent référence au même objet.

    délimiteur
    delimiter
        Un caractère ou une chaîne utilisée pour indiquer où une chaîne doit être divisée.


Exercices
---------

.. topic:: Exercice 1

    Écrivez une fonction appelée ``somme_cumulee`` qui prend une liste de nombres et renvoie la somme cumulée ; c'est-à-dire une nouvelle liste où le $i$-ème élément est la somme des premiers $i+1$ éléments de la liste originale. Par exemple, la somme cumulée de ``[1, 2, 3]`` est ``[1, 3, 6]``.

.. topic:: Exercice 2

    Écrivez une fonction nommée ``centre`` qui prend une liste et renvoie une nouvelle liste sans le premier et le dernier éléments. Par exemple, si vous passez ``[1, 2, 3, 4]``, elle doit renvoyer ``[2, 3]``.

.. topic:: Exercice 3

    Écrivez une fonction appelée ``est_trie`` qui prend une liste en paramètre et renvoie ``True`` si la liste est triée par ordre croissant, et ``False`` sinon. Par exemple, ``est_trie([1, 2, 2])`` devrait renvoyer ``True`` et ``est_trie(['b', 'a'])`` devrait renvoyer ``False``.

.. topic:: Exercice 4

    Écrivez une fonction appelée ``est_anagramme`` qui prend deux chaînes de caractères et renvoie ``True`` si elles sont des anagrammes (si elles contiennent les mêmes lettres avec les mêmes fréquences).

.. topic:: Exercice 5

    Écrivez une fonction appelée ``contient_doublons`` qui prend une liste et renvoie ``True`` si il y a un élément qui apparaît plus d'une fois. Elle ne doit pas modifier la liste originale.

.. topic:: Exercice 6

    Cet exercice est basé sur le fameux « Paradoxe des anniversaires ». Écrivez une fonction qui génère 23 dates aléatoires (représentées par des entiers entre 1 et 365) et vérifie s'il y a des doublons. En exécutant cela des milliers de fois, estimez la probabilité qu'il y ait au moins deux personnes nées le même jour dans un groupe de 23 personnes.
