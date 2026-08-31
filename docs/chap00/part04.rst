Conditionnelles et récursivité
==============================

Division entière et modulo
--------------------------

L'opérateur de division entière (*floor division*), ``//``, divise deux nombres
et arrondit le résultat à l'entier inférieur. Par exemple, supposons que
le temps d'exécution d'un programme soit de 105 minutes. Vous pourriez
vouloir savoir combien d'heures et de minutes cela représente.
La division entière renvoie le nombre entier d'heures, en ignorant le reste :

.. code:: python

    >>> minutes = 105
    >>> minutes // 60
    1

Pour obtenir le reste, vous pouvez soustraire une heure, ou utiliser
l'opérateur modulo, ``%``, qui divise deux nombres et renvoie le reste :

.. code:: python

    >>> reste = minutes % 60
    >>> reste
    45

L'opérateur modulo est très utile. Par exemple, vous pouvez vérifier si un nombre
est divisible par un autre : si ``x % y`` donne zéro, alors ``x`` est
divisible par ``y``.

Vous pouvez également extraire le chiffre le plus à droite d'un nombre.
Par exemple, ``x % 10`` renvoie le chiffre des unités de ``x`` (en base 10).

Expressions booléennes
----------------------

Une expression booléenne est une expression qui est soit vraie (``True``), soit
fausse (``False``). Les valeurs suivantes sont de type ``bool`` :

.. code:: python

    >>> type(True)
    <class 'bool'>
    >>> type(False)
    <class 'bool'>

L'opérateur ``==`` compare deux opérandes et produit ``True`` s'ils sont égaux,
et ``False`` sinon. Les autres opérateurs de comparaison relationnelle sont :

.. code:: python

    x != y               # x n'est pas égal à y
    x > y                # x est strictement supérieur à y
    x < y                # x est strictement inférieur à y
    x >= y               # x est supérieur ou égal à y
    x <= y               # x est inférieur ou égal à y

Opérateurs logiques
-------------------

Il existe trois opérateurs logiques : ``and``, ``or`` et ``not``.
Leur signification s'apparente à leur sens en anglais.
Par exemple, ``x > 0 and x < 10`` est vrai uniquement si ``x`` est strictement
supérieur à 0 *et* strictement inférieur à 10.

L'expression ``n % 2 == 0 or n % 3 == 0`` est vraie si *l'une* des
conditions est vraie, c'est-à-dire si le nombre est divisible par 2 *ou* par 3.

Enfin, l'opérateur ``not`` inverse l'expression booléenne. Ainsi,
``not (x > y)`` est vrai si ``x > y`` est faux (donc si ``x`` est inférieur
ou égal à ``y``).

Exécution conditionnelle
------------------------

Pour écrire des programmes utiles, nous avons presque toujours besoin de vérifier
des conditions et de modifier le comportement du programme en conséquence.
Les instructions conditionnelles (*conditional statements*) nous en donnent
la capacité. La forme la plus simple est l'instruction ``if`` :

.. code:: python

    if x > 0:
        print('x est positif')

L'expression booléenne après le ``if`` est appelée la condition.
Si elle est vraie, l'instruction indentée s'exécute. Si elle est fausse,
rien ne se passe.

Les instructions ``if`` ont la même structure que les définitions de fonctions :
un en-tête suivi d'un corps indenté. Il n'y a pas de limite au nombre
d'instructions pouvant apparaître dans le corps, mais il doit y en avoir
au moins une.
Parfois, il est utile d'avoir un corps sans instruction (comme espace
réservé pour du code que vous n'avez pas encore écrit). Dans ce cas, vous pouvez
utiliser l'instruction ``pass``, qui ne fait rien :

.. code:: python

    if x < 0:
        pass  # TODO: gérer les valeurs négatives

Exécution alternative
---------------------

Une deuxième forme de l'instruction ``if`` est l'exécution alternative,
dans laquelle il y a deux possibilités et la condition détermine
laquelle s'exécute. La syntaxe ressemble à ceci :

.. code:: python

    if x % 2 == 0:
        print('x est pair')
    else:
        print('x est impair')

Si le reste de la division de ``x`` par 2 est 0, alors nous savons
que ``x`` est pair. Si la condition est fausse, la deuxième série d'instructions
s'exécute. Étant donné que la condition doit être soit vraie soit fausse,
exactement l'une des alternatives s'exécutera.
Ces alternatives sont appelées des branches (*branches*).

Conditionnelles enchaînées
--------------------------

Parfois, il y a plus de deux possibilités et nous avons besoin de plus de
deux branches. Une façon d'exprimer un tel calcul est d'utiliser
une conditionnelle enchaînée (*chained conditional*) :

.. code:: python

    if x < y:
        print('x est inférieur à y')
    elif x > y:
        print('x est supérieur à y')
    else:
        print('x et y sont égaux')

``elif`` est une abréviation de « else if ». Là encore, une seule branche
sera exécutée. Il n'y a pas de limite au nombre d'instructions ``elif``.
S'il y a une clause ``else``, elle doit figurer à la fin, mais
elle n'est pas obligatoire.

Chaque condition est vérifiée dans l'ordre. Si la première est fausse,
la suivante est vérifiée, et ainsi de suite.
Si l'une d'elles est vraie, la branche correspondante s'exécute et
l'instruction se termine. Même si plusieurs conditions sont vraies,
seule la première branche vraie s'exécute.

Conditionnelles imbriquées
--------------------------

Une conditionnelle peut également être imbriquée dans une autre.
Nous aurions pu écrire l'exemple précédent de cette façon :

.. code:: python

    if x == y:
        print('x et y sont égaux')
    else:
        if x < y:
            print('x est inférieur à y')
        else:
            print('x est supérieur à y')

La conditionnelle externe contient deux branches. La première contient
une instruction simple. La deuxième branche contient une autre instruction
``if``, qui possède à son tour deux branches. Ces deux branches sont de simples
instructions, bien qu'elles auraient pu être des instructions conditionnelles
elles aussi.

Bien que l'indentation rende la structure évidente, les conditionnelles
imbriquées deviennent rapidement difficiles à lire.
Il est conseillé de les éviter quand vous le pouvez.

Les opérateurs logiques fournissent souvent un moyen de simplifier
les instructions conditionnelles imbriquées.
Par exemple, nous pouvons réécrire le code suivant en utilisant
une seule condition :

.. code:: python

    if 0 < x:
        if x < 10:
            print('x est un nombre positif à un chiffre.')

L'instruction ``print`` s'exécute uniquement si nous passons les deux tests,
nous pouvons donc obtenir le même effet avec l'opérateur ``and`` :

.. code:: python

    if 0 < x and x < 10:
        print('x est un nombre positif à un chiffre.')

Récursivité
-----------

Il est légal pour une fonction d'appeler une autre fonction ;
il est également légal pour une fonction de s'appeler elle-même.
L'exemple suivant illustre ce concept, appelé récursivité (*recursion*) :

.. code:: python

    def compte_a_rebours(n):
        if n <= 0:
            print('Décollage !')
        else:
            print(n)
            compte_a_rebours(n - 1)

Si ``n`` est inférieur ou égal à 0, la fonction affiche le mot « Décollage ! ».
Sinon, elle affiche ``n``, puis appelle une fonction nommée ``compte_a_rebours``
(elle-même), en lui passant ``n - 1`` comme argument.

Une fonction qui s'appelle elle-même est dite récursive ;
le processus d'exécution de cette fonction s'appelle la récursivité.

Diagrammes de pile pour les fonctions récursives
------------------------------------------------

Au chapitre précédent, nous avons utilisé un diagramme de pile
pour représenter l'état d'un programme pendant un appel de fonction.
Le même type de diagramme peut aider à interpréter une fonction récursive.

À chaque fois qu'une fonction est appelée, Python crée un nouveau contexte local
(un cadre ou *frame*), qui contient les variables et paramètres locaux de la fonction.
Pour une fonction récursive, il peut y avoir plusieurs cadres simultanément
sur la pile, chacun correspondant à un appel différent de la fonction, avec
sa propre valeur de ``n``.

Récursivité infinie
-------------------

Si une récursivité n'atteint jamais de cas de base, elle s'exécute pour
toujours, et le programme ne se termine jamais. C'est ce qu'on appelle
une récursivité infinie (*infinite recursion*).

Dans la plupart des environnements de programmation, un programme avec
une récursivité infinie ne s'exécute pas réellement pour toujours.
Python signale un message d'erreur lorsque la profondeur de récursivité
maximale est atteinte (généralement une ``RecursionError``).

Saisie au clavier
-----------------

Les programmes que nous avons écrits jusqu'à présent n'acceptent
aucune saisie de l'utilisateur. Ils effectuent le même calcul
à chaque fois. Python fournit une fonction intégrée appelée ``input``
qui met l'exécution du programme en pause et attend que l'utilisateur
tape quelque chose.

.. code:: python

    >>> texte = input()
    Quelque chose
    >>> print(texte)
    Quelque chose

Avant d'obtenir une saisie, il est judicieux d'afficher une invite
indiquant à l'utilisateur ce qu'il doit entrer.
Vous pouvez passer une chaîne de caractères à ``input`` pour qu'elle s'affiche
avant la mise en pause :

.. code:: python

    >>> nom = input('Quel est votre nom ?\n')
    Quel est votre nom ?
    Arthur
    >>> print(nom)
    Arthur

La séquence ``\n`` à la fin de la chaîne représente une nouvelle ligne,
ce qui place l'entrée de l'utilisateur sur la ligne en dessous de l'invite.

Si vous attendez un entier, vous pouvez essayer de convertir la valeur
de retour avec ``int()`` :

.. code:: python

    >>> invite = 'Quelle est la vitesse de vol d\'une hirondelle à vide ?\n'
    >>> vitesse = input(invite)
    Quelle est la vitesse de vol d'une hirondelle à vide ?
    42
    >>> int(vitesse)
    42

Débogage
--------

Les messages d'erreur et les traces d'exécution (*tracebacks*) de Python
indiquent où s'est produite l'erreur, mais ne disent généralement
pas pourquoi. Si une fonction s'appelle elle-même trop souvent,
la trace peut devenir extrêmement longue et difficile à lire.

Lorsque vous écrivez des conditions complexes, assurez-vous de bien
tester les différents chemins d'exécution (les cas extrêmes,
les nombres négatifs, les zéros). Ajouter des instructions ``print``
temporaires peut grandement faciliter la compréhension du chemin
réellement emprunté par votre programme.

Glossaire
---------

.. glossary::


    opérateur modulo
    modulus operator
        Un opérateur, noté avec un signe de pourcentage (``%``), qui opère
        sur des entiers et donne le reste lorsqu'un nombre est divisé par un autre.

    expression booléenne
    boolean expression
        Une expression dont la valeur est soit ``True``, soit ``False``.

    opérateur relationnel
    relational operator
        L'un des opérateurs qui compare ses opérandes :
        ``==``, ``!=``, ``>``, ``<``, ``>=`` et ``<=``.

    opérateur logique
    logical operator
        L'un des opérateurs qui combine des expressions booléennes :
        ``and``, ``or`` et ``not``.

    instruction conditionnelle
    conditional statement
        Une instruction qui contrôle le flux d'exécution en fonction d'une condition.

    condition
        L'expression booléenne dans une instruction conditionnelle
        qui détermine quelle branche s'exécute.

    branche
    branch
        L'une des séquences alternatives d'instructions dans une conditionnelle.

    conditionnelle enchaînée
    chained conditional
        Une instruction conditionnelle comportant une série d'alternatives (``elif``).

    conditionnelle imbriquée
    nested conditional
        Une instruction conditionnelle qui apparaît dans l'une des branches
        d'une autre instruction conditionnelle.

    récursivité
    recursion
        Le processus d'appel de la fonction qui est elle-même en cours d'exécution.

    cas de base
    base case
        Une branche conditionnelle dans une fonction récursive
        qui n'effectue pas d'appel récursif.

    récursivité infinie
    infinite recursion
        Une récursivité qui n'a pas de cas de base, ou ne l'atteint jamais.
        Finit par provoquer une erreur d'exécution.

Exercices
---------

.. topic:: Exercice 1

    Le dernier théorème de Fermat stipule qu'il n'existe aucun entier
    strictement positif *a*, *b* et *c* tel que :

    *a*\ :sup:`n` + *b*\ :sup:`n` = *c*\ :sup:`n`

    pour toutes valeurs de *n* strictement supérieures à 2.

    1. Écrivez une fonction nommée ``verifier_fermat`` qui prend quatre paramètres
       ``a``, ``b``, ``c`` et ``n``, et qui vérifie si le théorème de Fermat est vrai.
       Si *n* est plus grand que 2 et que l'équation est vraie, le programme
       doit afficher « Bon sang, Fermat avait tort ! ».
       Sinon, le programme doit afficher « Non, cela ne fonctionne pas. »
    2. Écrivez une fonction qui invite l'utilisateur à saisir des valeurs pour
       ``a``, ``b``, ``c`` et ``n``, les convertit en entiers, et utilise
       ``verifier_fermat`` pour vérifier si elles violent le théorème de Fermat.

.. topic:: Exercice 2

    Si l'on vous donne trois bâtons, vous pouvez ou non être en mesure de les
    disposer en triangle. Par exemple, si l'un des bâtons a une longueur
    de 12 pouces et que les deux autres font 1 pouce chacun,
    vous ne pourrez pas faire se rencontrer les petits bâtons au milieu.
    Pour tout ensemble de trois longueurs, il existe un test simple
    pour vérifier s'il est possible de former un triangle :

    *Si l'une des trois longueurs est supérieure à la somme des deux autres,
    alors vous ne pouvez pas former de triangle. Sinon, vous le pouvez.*

    1. Écrivez une fonction nommée ``est_un_triangle`` qui prend trois entiers
       comme arguments, et qui affiche « Oui » ou « Non », selon que vous pouvez ou non
       former un triangle à partir de bâtons possédant les longueurs données.
    2. Écrivez une fonction qui invite l'utilisateur à saisir trois longueurs
       de bâton, les convertit en entiers, et utilise ``est_un_triangle`` pour
       vérifier si des bâtons de ces longueurs peuvent former un triangle.
