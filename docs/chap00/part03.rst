Fonctions
=========

Appels de fonctions
-------------------

Dans le contexte de la programmation, une fonction est une séquence
d'instructions nommée qui effectue un calcul. Lorsque vous définissez une
fonction, vous spécifiez son nom et la séquence d'instructions.
Plus tard, vous pouvez « appeler » la fonction par son nom.

Nous avons déjà vu un exemple d'appel de fonction :

.. code:: python

    >>> print(32)
    32

Le nom de la fonction est ``print``. L'expression entre parenthèses est appelée
l'argument de la fonction. Le résultat, pour cette fonction, est le type
de l'argument.

Il est courant de dire qu'une fonction « prend » un argument et « retourne »
un résultat. Le résultat est appelé la valeur de retour (*return value*).

Fonctions de conversion de type
-------------------------------

Python fournit des fonctions intégrées qui convertissent les valeurs d'un type
à un autre. La fonction ``int`` prend n'importe quelle valeur et la convertit
en entier, si elle le peut, ou signale une erreur sinon :

.. code:: python

    >>> int('32')
    32
    >>> int('Hello')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'Hello'

``int`` peut convertir des valeurs à virgule flottante en entiers, mais elle
n'arrondit pas ; elle coupe simplement la partie fractionnaire :

.. code:: python

    >>> int(3.99999)
    3
    >>> int(-2.3)
    -2

La fonction ``float`` convertit les entiers et les chaînes de caractères en
nombres à virgule flottante :

.. code:: python

    >>> float(32)
    32.0
    >>> float('3.14159')
    3.14159

Enfin, ``str`` convertit son argument en une chaîne de caractères :

.. code:: python

    >>> str(32)
    '32'
    >>> str(3.14159)
    '3.14159'

Fonctions mathématiques
-----------------------

Python possède un module :mod:`math` qui fournit la plupart des fonctions
mathématiques familières. Un module est un fichier qui contient une
collection de fonctions liées.

Avant de pouvoir utiliser les fonctions d'un module, nous devons l'importer
avec une instruction ``import`` :

.. code:: python

    >>> import math

Cette instruction crée un objet module nommé ``math``.
Pour accéder à l'une des fonctions, vous devez spécifier le nom du module
et le nom de la fonction, séparés par un point.
Ce format est appelé la notation pointée (*dot notation*).

.. code:: python

    >>> ratio = puissance_signal / puissance_bruit
    >>> decibels = 10 * math.log10(ratio)
    >>> radians = 0.7
    >>> hauteur = math.sin(radians)

Le premier exemple utilise :func:`math.log10` pour calculer un rapport signal/bruit
en décibels (en supposant que ``puissance_signal`` et ``puissance_bruit`` sont définies).
Le deuxième exemple trouve le sinus de ``radians``. Le nom de la variable
est un indice indiquant que ``sin`` et les autres fonctions trigonométriques
(``cos``, ``tan``, etc.) prennent des arguments en radians.

Pour convertir des degrés en radians, divisez par 180 et multipliez par π :

.. code:: python

    >>> degres = 45
    >>> radians = degres / 180.0 * math.pi
    >>> math.sin(radians)
    0.7071067811865476

L'expression ``math.pi`` récupère la variable ``pi`` depuis le module ``math``.
Sa valeur est une approximation de π à virgule flottante, précise à
environ 15 chiffres.

Composition
-----------

Jusqu'à présent, nous avons examiné les éléments d'un programme — variables,
expressions et instructions — de manière isolée, sans parler de la façon
de les combiner.

L'une des fonctionnalités les plus utiles des langages de programmation est
leur capacité à prendre de petits blocs de construction et à les composer.
Par exemple, l'argument d'une fonction peut être n'importe quel type d'expression,
y compris des opérateurs arithmétiques :

.. code:: python

    x = math.sin(degres / 360.0 * 2 * math.pi)

Et même des appels de fonction :

.. code:: python

    x = math.exp(math.log(x+1))

Presque partout où vous pouvez mettre une valeur, vous pouvez mettre
une expression arbitraire.

Ajout de nouvelles fonctions
----------------------------

Jusqu'à présent, nous n'avons utilisé que les fonctions intégrées à Python,
mais il est également possible d'ajouter de nouvelles fonctions.
Une définition de fonction spécifie le nom d'une nouvelle fonction et
la séquence d'instructions qui s'exécute lorsque la fonction est appelée.

Voici un exemple :

.. code:: python

    def afficher_paroles():
        print("Je suis un bûcheron, et je vais bien.")
        print("Je dors toute la nuit et je travaille toute la journée.")

``def`` est un mot-clé qui indique qu'il s'agit d'une définition de fonction.
Le nom de la fonction est ``afficher_paroles``. Les règles pour les noms de
fonctions sont les mêmes que pour les variables : les lettres, les chiffres et
le soulignement sont légaux, mais le premier caractère ne peut pas être un chiffre.

Les parenthèses vides après le nom indiquent que cette fonction ne prend aucun argument.

La première ligne de la définition de la fonction est appelée l'en-tête (*header*) ;
le reste est appelé le corps (*body*). Le corps doit être indenté.
Par convention, l'indentation est toujours de quatre espaces.

La syntaxe pour appeler la nouvelle fonction est la même que pour les
fonctions intégrées :

.. code:: python

    >>> afficher_paroles()
    Je suis un bûcheron, et je vais bien.
    Je dors toute la nuit et je travaille toute la journée.

Une fois que vous avez défini une fonction, vous pouvez l'utiliser à l'intérieur
d'une autre fonction.

.. code:: python

    def repeter_paroles():
        afficher_paroles()
        afficher_paroles()

Définitions et utilisations
---------------------------

Rassemblez les fragments de code de la section précédente et l'ensemble du
programme ressemblera à ceci :

.. code:: python

    def afficher_paroles():
        print("Je suis un bûcheron, et je vais bien.")
        print("Je dors toute la nuit et je travaille toute la journée.")

    def repeter_paroles():
        afficher_paroles()
        afficher_paroles()

    repeter_paroles()

Ce programme contient deux définitions de fonctions : ``afficher_paroles`` et
``repeter_paroles``. Les définitions de fonctions sont exécutées comme d'autres
instructions, mais l'effet est de créer des objets fonctions.
Les instructions à l'intérieur de la fonction ne sont pas exécutées tant
que la fonction n'est pas appelée.

Comme vous pouvez vous y attendre, vous devez créer une fonction avant de
pouvoir l'exécuter. Autrement dit, la définition de la fonction doit être
exécutée avant la première fois qu'elle est appelée.

Flux d'exécution
----------------

Pour s'assurer qu'une fonction est définie avant sa première utilisation,
il faut connaître l'ordre dans lequel les instructions sont exécutées,
ce qu'on appelle le flux d'exécution (*flow of execution*).

L'exécution commence toujours par la première instruction du programme.
Les instructions sont exécutées une à la fois, de haut en bas.

Les définitions de fonctions ne modifient pas le flux d'exécution, mais rappelez-vous
que les instructions à l'intérieur d'une fonction ne sont pas exécutées tant
que la fonction n'est pas appelée.

Paramètres et arguments
-----------------------

Certaines des fonctions intégrées que nous avons vues nécessitent des arguments.
Par exemple, lorsque vous appelez :func:`math.sin`, vous passez un nombre comme argument.
Certaines fonctions prennent plus d'un argument : :func:`math.pow` prend deux
arguments, la base et l'exposant.

À l'intérieur de la fonction, les arguments sont affectés à des variables
appelées paramètres.
Voici un exemple d'une fonction définie par l'utilisateur qui prend un argument :

.. code:: python

    def imprimer_deux_fois(bruce):
        print(bruce)
        print(bruce)

Cette fonction affecte l'argument à un paramètre nommé ``bruce``.
Lorsque la fonction est appelée, elle imprime la valeur du paramètre
(quel qu'il soit) à deux reprises.

.. code:: python

    >>> imprimer_deux_fois('Spam')
    Spam
    Spam
    >>> imprimer_deux_fois(17)
    17
    17
    >>> imprimer_deux_fois(math.pi)
    3.141592653589793
    3.141592653589793

Les variables et paramètres sont locaux
---------------------------------------

Lorsque vous créez une variable à l'intérieur d'une fonction, elle est locale,
ce qui signifie qu'elle n'existe qu'à l'intérieur de cette fonction.
Par exemple :

.. code:: python

    def concatener_deux_fois(partie1, partie2):
        chat = partie1 + partie2
        imprimer_deux_fois(chat)

Cette fonction prend deux arguments, les concatène et affiche le résultat deux fois.

.. code:: python

    >>> ligne1 = 'Bing tiddle '
    >>> ligne2 = 'tiddle bang.'
    >>> concatener_deux_fois(ligne1, ligne2)
    Bing tiddle tiddle bang.
    Bing tiddle tiddle bang.

Lorsque la fonction se termine, la variable ``chat`` est détruite. Si nous essayons
de l'imprimer depuis l'extérieur de la fonction, nous obtenons une exception :

.. code:: python

    >>> print(chat)
    NameError: name 'chat' is not defined

Les paramètres sont également locaux. À l'extérieur de ``imprimer_deux_fois``,
il n'y a pas de variable telle que ``bruce``.

Fonctions productives et fonctions à effet de bord
--------------------------------------------------

Certaines des fonctions que nous utilisons, telles que les fonctions mathématiques,
retournent des résultats ; faute d'un meilleur terme, je les appelle
des fonctions productives (*fruitful functions*).
D'autres fonctions, comme ``imprimer_deux_fois``, effectuent une action mais
ne retournent pas de valeur. Elles sont appelées fonctions nulles ou
fonctions à effet de bord (*void functions*).

Si vous appelez une fonction productive en mode script ou dans un programme,
la valeur de retour est généralement ignorée, à moins que vous ne l'affectiez
à une variable :

.. code:: python

    math.cos(radians)
    x = math.cos(radians)

Les fonctions *void* peuvent afficher quelque chose à l'écran ou avoir un autre
effet, mais leur valeur de retour est une valeur spéciale appelée ``None``.

.. code:: python

    >>> resultat = imprimer_deux_fois('Bing')
    Bing
    Bing
    >>> print(resultat)
    None

La valeur ``None`` n'est pas la même chose que la chaîne de caractères ``'None'``.
C'est une valeur spéciale qui a son propre type :

.. code:: python

    >>> type(None)
    <class 'NoneType'>

Pourquoi des fonctions ?
------------------------

Il n'est pas toujours clair au premier abord pourquoi il vaut la peine de
diviser un programme en fonctions. Voici quelques raisons :

*   La création d'une nouvelle fonction vous donne l'opportunité de nommer
    un groupe d'instructions, ce qui rend votre programme plus facile à lire
    et à déboguer.

*   Les fonctions peuvent rendre un programme plus petit en éliminant le
    code répétitif. Plus tard, si vous apportez un changement, vous n'aurez
    à le faire qu'à un seul endroit.

*   La division d'un long programme en fonctions vous permet de déboguer
    les parties une à la fois, puis de les assembler dans un tout fonctionnel.

*   Les fonctions bien conçues sont souvent utiles pour de nombreux programmes.
    Une fois que vous en avez écrit et débogué une, vous pouvez la réutiliser.

Débogage
--------

L'une des compétences les plus importantes que vous allez acquérir est le
débogage (*debugging*).
Si votre programme comporte une erreur d'exécution, Python imprimera un
message d'erreur (*traceback*), qui contient des informations utiles.
Il indique où se trouve l'erreur, le type de l'erreur, et quelles fonctions
étaient en cours d'exécution au moment de l'erreur.

Glossaire
---------

.. glossary::

    fonction
    function
        Une séquence nommée d'instructions qui effectue une opération utile.
        Les fonctions peuvent ou non prendre des arguments,
        et peuvent ou non produire un résultat.

    définition de fonction
    function definition
        Une instruction qui crée une nouvelle fonction, en spécifiant son nom,
        ses paramètres et les instructions qu'elle exécute.

    en-tête
    header
        La première ligne d'une définition de fonction.

    corps
    body
        La séquence d'instructions à l'intérieur d'une définition de fonction.

    paramètre
    parameter
        Un nom utilisé à l'intérieur d'une fonction pour faire référence à
        la valeur passée comme argument.

    appel de fonction
    function call
        Une instruction qui exécute une fonction. Elle se compose du nom de
        la fonction suivi d'une liste d'arguments entre parenthèses.

    argument
        Une valeur fournie à une fonction lorsque la fonction est appelée.
        Cette valeur est assignée au paramètre correspondant.

    variable locale
    local variable
        Une variable définie à l'intérieur d'une fonction. Une variable locale
        ne peut être utilisée qu'à l'intérieur de sa fonction.

    valeur de retour
    return value
        Le résultat d'une fonction.

    fonction productive
    fruitful function
        Une fonction qui retourne une valeur.

    fonction nulle
    void function
        Une fonction qui ne retourne aucune valeur (elle retourne toujours ``None``).

    module
        Un fichier qui contient une collection de fonctions et d'autres définitions.

    notation pointée
    dot notation
        La syntaxe pour appeler une fonction dans un autre module, en spécifiant
        le nom du module suivi d'un point et du nom de la fonction.

    flux d'exécution
    flow of execution
        L'ordre dans lequel les instructions sont exécutées lors du fonctionnement
        d'un programme.

Exercices
---------

.. topic:: Exercice 1

    Écrivez une fonction nommée ``right_justify`` qui prend une chaîne de
    caractères nommée ``s`` comme paramètre et imprime la chaîne avec
    suffisamment d'espaces de début pour que la dernière lettre de la chaîne
    se trouve dans la colonne 70 de l'affichage.

    .. code:: python

        >>> right_justify('monty')
                                                                         monty

    *Indice : Utilisez la concaténation de chaînes et la répétition.
    De plus, Python fournit une fonction intégrée appelée len qui
    renvoie la longueur d'une chaîne, donc la valeur de len('monty') est 5.*

.. topic:: Exercice 2

    Un objet de fonction est une valeur que vous pouvez affecter à une variable
    ou passer comme argument.
    Par exemple, ``do_twice`` est une fonction qui prend un objet de fonction
    comme argument et l'appelle à deux reprises :

    .. code:: python

        def do_twice(f):
            f()
            f()

    Voici un exemple qui utilise ``do_twice`` pour appeler une fonction
    nommée ``print_spam`` à deux reprises.

    .. code:: python

        def print_spam():
            print('spam')

        do_twice(print_spam)

    1.  Tapez cet exemple dans un script et testez-le.
    2.  Modifiez ``do_twice`` afin qu'elle prenne deux arguments, un objet
        fonction et une valeur, et appelle la fonction deux fois, en passant
        la valeur comme argument.
