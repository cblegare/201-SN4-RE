Chaînes de caractères
=====================

Les chaînes de caractères (*strings*) ne sont pas comme des entiers, des nombres à virgule flottante ou des booléens. Une chaîne est une séquence (*sequence*), c'est-à-dire une collection ordonnée d'autres valeurs. Dans ce chapitre, vous verrez comment accéder aux caractères qui composent une chaîne et vous apprendrez certaines des méthodes proposées par les chaînes.

Une chaîne est une séquence
---------------------------

Une chaîne est une séquence de caractères. Vous pouvez accéder aux caractères un à la fois avec l'opérateur de crochet :

.. code:: python

    >>> fruit = 'banane'
    >>> lettre = fruit[1]

La seconde instruction sélectionne le caractère numéro 1 de ``fruit`` et l'affecte à ``lettre``.
L'expression entre crochets est appelée un indice (*index*). L'indice indique quel caractère de la séquence vous souhaitez (d'où son nom).
Mais vous pourriez ne pas obtenir ce que vous attendez :

.. code:: python

    >>> lettre
    'a'

Pour la plupart des gens, la première lettre de ``'banane'`` est ``b``, pas ``a``. Mais pour les informaticiens, l'indice est un décalage par rapport au début de la chaîne, et le décalage de la première lettre est zéro.

.. code:: python

    >>> lettre = fruit[0]
    >>> lettre
    'b'

Ainsi, ``b`` est la 0-ième lettre (« zéro-ième ») de ``'banane'``, ``a`` est la 1-ère lettre, et ``n`` est la 2-ème lettre.
Vous pouvez utiliser n'importe quelle expression, y compris des variables et des opérateurs, comme indice, mais la valeur de l'indice doit être un entier. Sinon, vous obtenez une exception :

.. code:: python

    >>> lettre = fruit[1.5]
    TypeError: string indices must be integers

``len``
-------

``len`` est une fonction intégrée qui renvoie le nombre de caractères dans une chaîne :

.. code:: python

    >>> fruit = 'banane'
    >>> len(fruit)
    6

Pour obtenir la dernière lettre d'une chaîne, vous pourriez être tenté d'essayer quelque chose comme ceci :

.. code:: python

    >>> longueur = len(fruit)
    >>> derniere = fruit[longueur]
    IndexError: string index out of range

La raison de cette erreur est qu'il n'y a pas de lettre à l'indice 6 dans ``'banane'``. Les indices vont de 0 à 5. Pour obtenir le dernier caractère, vous devez soustraire 1 à la longueur :

.. code:: python

    >>> derniere = fruit[longueur-1]
    >>> derniere
    'e'

Alternativement, vous pouvez utiliser des indices négatifs, qui comptent à rebours à partir de la fin de la chaîne. L'expression ``fruit[-1]`` donne la dernière lettre, ``fruit[-2]`` donne l'avant-dernière, et ainsi de suite.

Parcours avec une boucle ``for``
--------------------------------

Une grande partie des calculs implique le traitement d'une chaîne un caractère à la fois. Souvent, ils commencent au début, sélectionnent chaque caractère tour à tour, font quelque chose avec, et continuent jusqu'à la fin. Ce modèle de traitement est appelé un parcours (*traversal*). Une façon d'écrire un parcours est d'utiliser une boucle ``while`` :

.. code:: python

    indice = 0
    while indice < len(fruit):
        lettre = fruit[indice]
        print(lettre)
        indice = indice + 1

Cette boucle parcourt la chaîne et affiche chaque lettre sur une ligne à part. La condition de la boucle est ``indice < len(fruit)``, donc lorsque ``indice`` est égal à la longueur de la chaîne, la condition est fausse, et le corps de la boucle ne s'exécute pas.

Une autre façon d'écrire un parcours est d'utiliser une boucle ``for`` :

.. code:: python

    for lettre in fruit:
        print(lettre)

À chaque itération de la boucle, le caractère suivant de la chaîne est affecté à la variable ``lettre``. La boucle continue jusqu'à ce qu'il ne reste plus de caractères.

Tranches de chaînes
-------------------

Un segment d'une chaîne s'appelle une tranche (*slice*). La sélection d'une tranche est similaire à la sélection d'un caractère :

.. code:: python

    >>> s = 'Monty Python'
    >>> s[0:5]
    'Monty'
    >>> s[6:12]
    'Python'

L'opérateur ``[n:m]`` renvoie la partie de la chaîne du n-ième caractère au m-ième caractère, en incluant le premier mais en excluant le dernier.

Si vous omettez le premier indice, la tranche commence au début de la chaîne. Si vous omettez le second, la tranche va jusqu'à la fin de la chaîne :

.. code:: python

    >>> fruit = 'banane'
    >>> fruit[:3]
    'ban'
    >>> fruit[3:]
    'ane'

Si le premier indice est supérieur ou égal au second, le résultat est une chaîne vide, représentée par deux guillemets :

.. code:: python

    >>> fruit[3:3]
    ''

Une chaîne vide ne contient aucun caractère et a une longueur de 0, mais à part cela, c'est une chaîne comme une autre.

Les chaînes sont immuables
--------------------------

Il est tentant d'utiliser l'opérateur de crochet du côté gauche d'une affectation, avec l'intention de changer un caractère dans une chaîne. Par exemple :

.. code:: python

    >>> salut = 'Bonjour, monde !'
    >>> salut[0] = 'J'
    TypeError: 'str' object does not support item assignment

L'erreur indique que l'objet de type chaîne ne prend pas en charge l'affectation d'éléments.
La raison en est que les chaînes sont immuables (*immutable*), ce qui signifie que vous ne pouvez pas modifier une chaîne existante. Le mieux que vous puissiez faire est de créer une nouvelle chaîne qui est une variante de l'originale :

.. code:: python

    >>> salut = 'Bonjour, monde !'
    >>> nouveau_salut = 'J' + salut[1:]
    >>> nouveau_salut
    'Jonjour, monde !'

Recherche
---------

Que fait la fonction suivante ?

.. code:: python

    def trouver(mot, lettre):
        indice = 0
        while indice < len(mot):
            if mot[indice] == lettre:
                return indice
            indice = indice + 1
        return -1

Dans un sens, ``trouver`` est l'inverse de l'opérateur de crochet. Au lieu de prendre un indice et d'extraire le caractère correspondant, elle prend un caractère et trouve l'indice où ce caractère apparaît. Si le caractère n'est pas trouvé, la fonction renvoie ``-1``.

C'est le premier exemple que nous voyons d'une instruction ``return`` à l'intérieur d'une boucle. Si ``mot[indice] == lettre``, la fonction sort immédiatement de la boucle et retourne le résultat.
Si le caractère n'apparaît pas dans la chaîne, le programme parcourt normalement toute la boucle et retourne ``-1``.

Ce modèle de calcul, qui traverse une séquence et retourne un résultat lorsqu'il trouve ce qu'il cherche, est appelé une recherche (*search*).

Boucles et comptage
-------------------

Le programme suivant compte le nombre de fois que la lettre ``a`` apparaît dans une chaîne :

.. code:: python

    mot = 'banane'
    compteur = 0
    for lettre in mot:
        if lettre == 'a':
            compteur = compteur + 1
    print(compteur)

Ce programme démontre un autre modèle de calcul appelé un compteur (*counter*). La variable ``compteur`` est initialisée à 0 et est incrémentée à chaque fois qu'un ``a`` est trouvé. À la sortie de la boucle, ``compteur`` contient le résultat final.

Méthodes de chaînes de caractères
---------------------------------

Les chaînes de caractères fournissent des méthodes qui effectuent une variété d'opérations utiles. Une méthode (*method*) est similaire à une fonction : elle prend des arguments et retourne une valeur, mais la syntaxe est différente.

Par exemple, la méthode ``upper`` prend une chaîne et retourne une nouvelle chaîne avec toutes les lettres en majuscules.
Au lieu de la syntaxe de fonction ``upper(mot)``, elle utilise la syntaxe de méthode ``mot.upper()`` :

.. code:: python

    >>> mot = 'banane'
    >>> nouveau_mot = mot.upper()
    >>> nouveau_mot
    'BANANE'

Cette forme de notation avec un point indique le nom de la méthode, ``upper``, et le nom de la chaîne sur laquelle appliquer la méthode, ``mot``.
Un appel de méthode s'appelle une invocation (*invocation*) ; dans ce cas, nous pourrions dire que nous invoquons ``upper`` sur ``mot``.

En fait, il existe une méthode de chaîne nommée ``find`` qui est remarquablement similaire à la fonction ``trouver`` que nous avons écrite :

.. code:: python

    >>> mot = 'banane'
    >>> index = mot.find('a')
    >>> index
    1

L'opérateur ``in``
------------------

Le mot-clé ``in`` est un opérateur booléen qui prend deux chaînes et renvoie ``True`` si la première apparaît en tant que sous-chaîne dans la seconde :

.. code:: python

    >>> 'a' in 'banane'
    True
    >>> 'grain' in 'banane'
    False

Comparaison de chaînes
----------------------

L'opérateur relationnel fonctionne sur les chaînes de caractères. Pour voir si deux chaînes sont égales :

.. code:: python

    if mot == 'banane':
        print("D'accord, des bananes.")

Les autres opérations relationnelles sont utiles pour classer les mots par ordre alphabétique :

.. code:: python

    if mot < 'banane':
        print('Votre mot, ' + mot + ', vient avant banane.')
    elif mot > 'banane':
        print('Votre mot, ' + mot + ', vient après banane.')
    else:
        print("D'accord, des bananes.")

Python ne gère pas les majuscules et les minuscules de la même façon que les humains. Toutes les lettres majuscules viennent avant toutes les lettres minuscules, donc :

.. code:: text

    Votre mot, Ananas, vient avant banane.

Débogage
--------

Lorsque vous utilisez des indices pour parcourir les valeurs d'une séquence,
il est facile de se tromper sur le début et la fin de l'itération. Voici une fonction
qui est censée comparer deux mots et renvoyer ``True`` si l'un d'eux est
l'inverse de l'autre, mais elle contient deux erreurs :

.. code:: python

    def est_inverse(mot1, mot2):
        if len(mot1) != len(mot2):
            return False

        i = 0
        j = len(mot2)

        while j > 0:
            if mot1[i] != mot2[j]:
                return False
            i = i + 1
            j = j - 1

        return True

Si nous testons cette fonction avec les mots ``"pots"`` et ``"stop"``,
nous nous attendons à ce qu'elle renvoie ``True``, mais elle provoque une erreur ``IndexError`` :

.. code:: python

    >>> est_inverse('pots', 'stop')
    IndexError: string index out of range

Pour le débogage, il est judicieux d'insérer une instruction ``print(i, j)``
avant la ligne fautive pour afficher les indices. Dans ce cas, lors du
premier passage dans la boucle, la valeur de ``j`` est 4, ce qui
est hors limites pour la chaîne ``'stop'``. La bonne valeur de départ
est ``len(mot2) - 1``.

Si vous corrigez cela et lancez le programme à nouveau, il ne produit
plus d'erreur, mais il donne un résultat incorrect.
Je vous laisse trouver et corriger la deuxième erreur !

Glossaire
---------

.. glossary::

    séquence
    sequence
        Un ensemble ordonné, c'est-à-dire une collection de valeurs
        où chaque valeur est identifiée par un indice entier.

    élément
    item
        L'une des valeurs composant une séquence.

    indice
    index
        Une valeur entière utilisée pour sélectionner un élément
        d'une séquence, comme un caractère dans une chaîne.

    tranche
    slice
        Une partie d'une chaîne spécifiée par une plage d'indices.

    parcours
    traversal
        Itérer à travers les éléments d'une séquence, en effectuant
        une opération similaire sur chacun d'eux.

    immuable
    immutable
        La propriété d'une séquence dont les éléments ne peuvent pas
        être modifiés.

    recherche
    search
        Un modèle de parcours qui s'arrête lorsqu'il trouve ce qu'il cherche.

    compteur
    counter
        Une variable utilisée pour compter quelque chose, souvent
        initialisée à zéro puis incrémentée.

    invocation
    invocation
        Une instruction qui appelle une méthode.

    méthode
    method
        Une fonction associée à un objet et appelée en utilisant
        la notation pointée.


Exercices
---------

.. topic:: Exercice 1

    Lisez la documentation des méthodes de chaînes de caractères à l'adresse
    https://docs.python.org/3/library/stdtypes.html#string-methods.
    Expérimentez avec quelques-unes d'entre elles pour vous assurer de
    bien comprendre comment elles fonctionnent. ``strip`` et ``replace`` sont
    particulièrement utiles.

    La documentation utilise une syntaxe qui pourrait être source de confusion.
    Par exemple, dans ``find(sub[, start[, end]])``, les crochets
    indiquent des arguments optionnels. Ainsi, ``sub`` est obligatoire,
    mais ``start`` est facultatif, et si vous incluez ``start``, alors
    ``end`` est également facultatif.

.. topic:: Exercice 2

    Une tranche de chaîne peut accepter un troisième indice pour
    spécifier un "pas" (*step*), c'est-à-dire l'espacement entre
    les caractères consécutifs. Un pas de 2 signifie tous les deux caractères,
    et un pas de 3 signifie tous les trois caractères, etc.

    .. code:: python

        >>> fruit = 'banane'
        >>> fruit[0:5:2]
        'bnn'

    Un pas de -1 fait parcourir le mot à l'envers, de sorte que la tranche
    ``[::-1]`` génère une chaîne inversée.

    Utilisez cette fonctionnalité pour écrire une version raccourcie de
    ``est_palindrome`` (une fonction qui vérifie si un mot se lit de
    la même manière à l'endroit et à l'envers).

.. topic:: Exercice 3

    Les méthodes de chaînes suivantes sont toutes utiles : ``islower``,
    ``isupper``, et ``isalpha``.

    Écrivez une fonction nommée ``lettre_minuscule_presente`` qui prend
    une chaîne de caractères comme argument et qui retourne ``True``
    si la chaîne contient au moins une lettre minuscule, et ``False`` sinon.

.. topic:: Exercice 4

    Le chiffrement de César (ROT13) consiste à remplacer chaque lettre
    par la lettre se trouvant un certain nombre de places plus loin dans
    l'alphabet.

    Écrivez une fonction nommée ``tourner_mot`` qui prend une chaîne
    de caractères et un entier comme paramètres, et retourne une
    nouvelle chaîne contenant les lettres de la chaîne d'origine tournées
    du nombre de places spécifié par l'entier.

    *Indice : vous pourriez trouver les fonctions intégrées* ``ord``
    *et* ``chr`` *utiles pour convertir des caractères en valeurs
    numériques et inversement.*
