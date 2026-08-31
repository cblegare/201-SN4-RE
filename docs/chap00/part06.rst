Fonctions productives
=====================

Valeurs de retour
-----------------

Certaines des fonctions intégrées que nous avons utilisées, telles que les
fonctions mathématiques, produisent des résultats. L'appel de la fonction
génère une valeur, que nous affectons généralement à une variable ou que
nous utilisons dans une expression.

.. code:: python

    e = math.exp(1.0)
    hauteur = rayon * math.sin(radians)

Mais jusqu'à présent, aucune des fonctions que nous avons écrites n'a retourné
de valeur.

Dans ce chapitre, nous allons écrire des fonctions productives
(*fruitful functions*).
Le premier exemple est ``aire``, qui retourne l'aire d'un cercle avec
le rayon donné :

.. code:: python

    import math

    def aire(rayon):
        a = math.pi * rayon**2
        return a

Nous avons vu l'instruction ``return`` auparavant, mais dans une fonction productive,
l'instruction ``return`` inclut une expression. Cette instruction signifie :
« Retourne immédiatement de cette fonction et utilise l'expression suivante
comme valeur de retour. » L'expression fournie peut être arbitrairement compliquée,
nous pourrions donc écrire cette fonction de manière plus concise :

.. code:: python

    def aire(rayon):
        return math.pi * rayon**2

D'un autre côté, les variables temporaires comme ``a`` peuvent rendre le
débogage plus facile.

Parfois, il est utile d'avoir plusieurs instructions de retour,
une dans chaque branche d'une condition :

.. code:: python

    def valeur_absolue(x):
        if x < 0:
            return -x
        else:
            return x

Puisque ces instructions ``return`` sont dans une condition alternative,
une seule d'entre elles sera exécutée.

Dès qu'une instruction de retour s'exécute, la fonction se termine
sans exécuter les instructions suivantes. Tout code qui apparaît
après une instruction ``return``, ou à tout autre endroit que le flux
d'exécution ne peut jamais atteindre, est appelé du code mort (*dead code*).

Dans une fonction productive, c'est une bonne idée de s'assurer que chaque
chemin possible à travers le programme atteint une instruction ``return``.
Par exemple :

.. code:: python

    def valeur_absolue(x):
        if x < 0:
            return -x
        if x > 0:
            return x

Cette fonction est incorrecte car si ``x`` se trouve être 0, aucune des
conditions n'est vraie, et la fonction se termine sans toucher à une instruction
``return``. Si le flux d'exécution atteint la fin d'une fonction,
la valeur de retour est ``None``, ce qui n'est pas la valeur absolue de 0.

.. code:: python

    >>> print(valeur_absolue(0))
    None

Développement incrémental
-------------------------

Au fur et à mesure que vous écrirez des fonctions plus grandes, vous constaterez
peut-être que vous passez plus de temps à déboguer.
Pour faire face à des programmes de plus en plus complexes, vous voudrez peut-être
essayer un processus appelé développement incrémental (*incremental development*).

L'objectif du développement incrémental est d'éviter les longues sessions
de débogage en ajoutant et en testant seulement une petite quantité de code à la fois.

À titre d'exemple, supposons que vous souhaitiez trouver la distance
entre deux points, donnés par leurs coordonnées (x\ :sub:`1`, y\ :sub:`1`)
et (x\ :sub:`2`, y\ :sub:`2`). Par le théorème de Pythagore, la distance est :

.. math::

    distance = \sqrt{(x_2 - x_1)^2 + (y_2) - Y_1)^2}

La première étape consiste à considérer à quoi devrait ressembler la fonction ``distance``
en Python. Autrement dit, quelles sont les entrées (paramètres) et quelle est la sortie
(valeur de retour) ?

Dans ce cas, les entrées sont deux points, que vous pouvez représenter à l'aide de
quatre nombres. La valeur de retour est la distance, qui est une valeur à
virgule flottante.

Vous pouvez déjà écrire le squelette de la fonction :

.. code:: python

    def distance(x1, y1, x2, y2):
        return 0.0

Évidemment, cette version ne calcule pas les distances ; elle retourne toujours zéro.
Mais elle est syntaxiquement correcte, et elle s'exécutera, ce qui signifie
que vous pouvez la tester avant de la rendre plus compliquée.

Pour tester la nouvelle fonction, appelez-la avec des exemples d'arguments :

.. code:: python

    >>> distance(1, 2, 4, 6)
    0.0

J'ai choisi ces valeurs pour que la distance horizontale soit 3 et la
distance verticale soit 4 ; de cette façon, le résultat est 5 (l'hypoténuse
d'un triangle 3-4-5). Lors du test d'une fonction, il est utile de
connaître la bonne réponse.

À ce stade, nous avons confirmé que la fonction est syntaxiquement
correcte, et nous pouvons commencer à ajouter du code. Après chaque
changement, nous testons à nouveau le programme. Si une erreur survient
à n'importe quel point, nous savons où elle se trouve : elle doit se trouver
dans la dernière ligne que nous avons ajoutée.

Une étape logique de calcul consiste à trouver les différences x\ :sub:`2` - x\ :sub:`1`
et y\ :sub:`2` - y\ :sub:`1`. Nous stockerons ces valeurs dans des
variables temporaires et les imprimerons :

.. code:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        print('dx est', dx)
        print('dy est', dy)
        return 0.0

Si la fonction fonctionne, elle devrait afficher ``dx est 3`` et ``dy est 4``.
Si c'est le cas, nous savons que la fonction obtient les bons arguments
et effectue le premier calcul correctement. Si ce n'est pas le cas,
il n'y a que quelques lignes à vérifier.

Ensuite, nous calculons la somme des carrés de ``dx`` et ``dy`` :

.. code:: python

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        carre_dx = dx**2
        carre_dy = dy**2
        print('carre_dx est', carre_dx)
        print('carre_dy est', carre_dy)
        return 0.0

Encore une fois, vous devez exécuter le programme à ce stade et vérifier la sortie
(qui devrait être 25).

Enfin, vous pouvez utiliser la fonction ``math.sqrt`` pour calculer et
retourner le résultat :

.. code:: python

    import math

    def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        carre_dx = dx**2
        carre_dy = dy**2
        resultat = math.sqrt(carre_dx + carre_dy)
        return resultat

Si cela fonctionne correctement, vous avez terminé.
Sinon, vous voudrez peut-être afficher la valeur de ``resultat`` avant l'instruction de retour.

La version finale de la fonction n'affiche rien lorsqu'elle est exécutée ;
elle retourne simplement une valeur. Les instructions ``print``
que nous avons écrites sont utiles pour le débogage, mais une fois
que vous avez vérifié que la fonction fonctionne, vous devez les supprimer.
Un code comme celui-ci est appelé code d'échafaudage (*scaffolding*) car il
est utile pour construire le programme mais ne fait pas partie du produit final.

Composition
-----------

Comme vous devriez vous y attendre à ce jour, vous pouvez appeler une fonction
à partir d'une autre. Cette capacité est appelée composition (*composition*).

À titre d'exemple, nous allons écrire une fonction qui prend deux points,
le centre du cercle et un point sur le périmètre, et qui calcule l'aire
du cercle.

Supposons que le point central est stocké dans les variables ``xc`` et ``yc``,
et le point de périmètre est dans ``xp`` et ``yp``.
La première étape consiste à trouver le rayon du cercle,
qui est la distance entre les deux points.
Nous venons d'écrire une fonction, ``distance``, qui fait cela :

.. code:: python

    rayon = distance(xc, yc, xp, yp)

La deuxième étape consiste à trouver l'aire d'un cercle avec ce rayon;
nous venons d'écrire cela aussi :

.. code:: python

    resultat = aire(rayon)

Encapsuler ces étapes dans une fonction produit ceci :

.. code:: python

    def aire_du_cercle(xc, yc, xp, yp):
        rayon = distance(xc, yc, xp, yp)
        resultat = aire(rayon)
        return resultat

Les variables temporaires ``rayon`` et ``resultat`` sont utiles
pour le développement et le débogage, mais une fois que le
programme fonctionne, nous pouvons le rendre plus concis
en composant les appels de fonctions :

.. code:: python

    def aire_du_cercle(xc, yc, xp, yp):
        return aire(distance(xc, yc, xp, yp))

Fonctions booléennes
--------------------

Les fonctions peuvent retourner des booléens,
ce qui est souvent pratique pour cacher des tests complexes
à l'intérieur de fonctions. Par exemple :

.. code:: python

    def est_divisible(x, y):
        if x % y == 0:
            return True
        else:
            return False

Il est courant de donner aux fonctions booléennes
des noms qui ressemblent à des questions par oui ou par non;
``est_divisible`` retourne ``True`` ou ``False``
pour indiquer si ``x`` est divisible par ``y``.

Voici un exemple :

.. code:: python

    >>> est_divisible(6, 4)
    False
    >>> est_divisible(6, 3)
    True

Le résultat de l'opérateur ``==`` est un booléen, nous pouvons
donc écrire la fonction de manière plus concise en le retournant
directement :

.. code:: python

    def est_divisible(x, y):
        return x % y == 0

Les fonctions booléennes sont souvent utilisées
dans des instructions conditionnelles :

.. code:: python

    if est_divisible(x, y):
        print('x est divisible par y')

Il peut être tentant d'écrire quelque chose comme :

.. code:: python

    if est_divisible(x, y) == True:
        print('x est divisible par y')

Mais la comparaison supplémentaire est inutile.

Glossaire
---------

.. glossary::

    variable temporaire
    temporary variable
        Une variable utilisée pour stocker une valeur intermédiaire
        dans un calcul complexe.

    code mort
    dead code
        Une partie d'un programme qui ne peut jamais être exécutée,
        souvent parce qu'elle apparaît après une instruction de retour.

    développement incrémental
    incremental development
        Un plan de développement de programme destiné à éviter
        le débogage en ajoutant et en testant seulement une petite
        quantité de code à la fois.

    code d'échafaudage
    scaffolding
        Code qui est utilisé pendant le développement du programme
        mais qui ne fait pas partie du produit final.

    fonction booléenne
    boolean function
        Une fonction qui retourne un booléen.

Exercices
---------

.. topic:: Exercice 1

    Écrivez une fonction ``compare`` qui prend deux valeurs, ``x`` et ``y``,
    et qui retourne ``1`` si ``x > y``, ``0`` si ``x == y``, et ``-1`` si ``x < y``.

.. topic:: Exercice 2

    Utilisez un développement incrémental pour écrire une fonction
    nommée ``hypotenuse`` qui retourne la longueur de l'hypoténuse
    d'un triangle rectangle, étant donné la longueur des deux
    autres côtés. Enregistrez chaque étape du processus de développement
    au fur et à mesure que vous avancez.

.. topic:: Exercice 3

    Écrivez une fonction booléenne ``est_entre(x, y, z)`` qui
    retourne ``True`` si ``x ≤ y ≤ z`` et ``False`` sinon.
