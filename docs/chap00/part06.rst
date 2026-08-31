Itération
=========

Réaffectation
-------------

Comme vous l'avez peut-être déjà découvert, il est légal d'effectuer plus
d'une affectation sur la même variable. Une nouvelle affectation fait en
sorte qu'une variable existante se réfère à une nouvelle valeur (et cesse de
se référer à l'ancienne).

.. code:: python

    >>> x = 5
    >>> x
    5
    >>> x = 7
    >>> x
    7

La première fois que nous affichons ``x``, sa valeur est 5 ;
la deuxième fois, sa valeur est 7.

L'une des sources de confusion les plus courantes lors de l'apprentissage de
la programmation est la différence entre l'affectation et l'égalité. En
mathématiques, le signe égal indique que deux éléments sont égaux et le
resteront. En Python, une instruction d'affectation utilise le signe égal (``=``),
mais ce n'est pas une affirmation d'égalité.

Par exemple, si vous écrivez ``a = b``, vous affirmez que ``a`` et ``b``
ont actuellement la même valeur, mais ils ne sont pas obligés de rester égaux
indéfiniment :

.. code:: python

    a = 5
    b = a    # a et b sont maintenant égaux
    a = 3    # a et b ne sont plus égaux

Mise à jour de variables
------------------------

Un des types de réaffectation les plus courants est la mise à jour
(*update*), où la nouvelle valeur de la variable dépend de l'ancienne.

.. code:: python

    x = x + 1

Cela signifie « récupère la valeur actuelle de ``x``, ajoute 1, et met ensuite
à jour ``x`` avec la nouvelle valeur. »

Si vous essayez de mettre à jour une variable qui n'existe pas, vous
obtenez une erreur, car Python évalue le côté droit avant d'affecter
la valeur à ``x`` :

.. code:: python

    >>> x = x + 1
    NameError: name 'x' is not defined

Avant de pouvoir mettre à jour une variable, vous devez l'initialiser
(*initialize*), généralement par une affectation simple :

.. code:: python

    >>> x = 0
    >>> x = x + 1

La mise à jour d'une variable par l'ajout de 1 s'appelle une incrémentation
(*increment*) ; la soustraction de 1 s'appelle une décrémentation (*decrement*).

L'instruction ``while``
-----------------------

Les ordinateurs sont souvent utilisés pour automatiser des tâches répétitives.
Répéter des tâches identiques ou similaires sans faire d'erreurs est une chose
que les ordinateurs font bien et que les humains font mal. En programmation,
la répétition est aussi appelée itération (*iteration*).

Python fournit une instruction ``while`` pour faciliter l'itération.
Voici une version de ``compte_a_rebours`` qui utilise une instruction ``while`` :

.. code:: python

    def compte_a_rebours(n):
        while n > 0:
            print(n)
            n = n - 1
        print('Décollage !')

Vous pouvez lire l'instruction ``while`` presque comme de l'anglais.
Elle signifie : « Tant que ``n`` est strictement supérieur à 0, affiche
la valeur de ``n`` et diminue la valeur de ``n`` de 1.
Une fois que tu as terminé, affiche le mot Décollage ! »

Plus formellement, voici le flux d'exécution pour une instruction ``while`` :

1. Déterminez si la condition est vraie ou fausse.
2. Si la condition est fausse, quittez l'instruction ``while`` et continuez
   l'exécution à la prochaine instruction.
3. Si la condition est vraie, exécutez le corps de la boucle et retournez à
   l'étape 1.

Ce type de flux est appelé une boucle (*loop*).
Si la condition est fausse dès le départ, le corps de la boucle ne s'exécute jamais.

Le corps de la boucle doit changer la valeur d'une ou plusieurs variables
pour qu'à un moment donné, la condition devienne fausse et que la boucle
se termine. Si la condition ne devient jamais fausse, la boucle se répétera
pour toujours, ce qu'on appelle une boucle infinie (*infinite loop*).

L'instruction ``break``
-----------------------

Parfois, vous ne savez pas qu'il est temps de terminer une boucle avant
d'être au milieu du corps de la boucle.
Dans ce cas, vous pouvez utiliser l'instruction ``break`` pour sortir de
la boucle immédiatement.

Par exemple, supposons que vous souhaitiez demander une saisie à l'utilisateur
jusqu'à ce qu'il tape ``'fin'``. Vous pourriez écrire :

.. code:: python

    while True:
        ligne = input('> ')
        if ligne == 'fin':
            break
        print(ligne)
    print('Terminé !')

La condition de la boucle est ``True``, ce qui est toujours vrai, donc
la boucle s'exécutera jusqu'à ce qu'elle rencontre l'instruction ``break``.
À chaque itération, elle invite l'utilisateur avec un chevron. Si
l'utilisateur tape ``fin``, l'instruction ``break`` quitte la boucle.
Sinon, le programme affiche ce que l'utilisateur a tapé et retourne
au début de la boucle.

Racines carrées
---------------

Les boucles sont souvent utilisées dans les programmes qui calculent
des résultats numériques en commençant par une réponse approximative et
en l'améliorant de manière itérative.

Par exemple, l'une des façons de calculer les racines carrées est la méthode
de Newton. Supposons que vous souhaitiez connaître la racine carrée de $a$.
Si vous commencez avec une estimation quelconque, $x$, vous pouvez calculer une meilleure
estimation avec la formule suivante :

  $y = \frac{x + a / x}{2}$

Par exemple, si $a$ vaut 4 et $x$ vaut 3 :

.. code:: python

    >>> a = 4
    >>> x = 3
    >>> y = (x + a/x) / 2
    >>> y
    2.1666666666666665

Le résultat est plus proche de la bonne réponse ($\sqrt{4} = 2$). Si nous répétons
le processus avec la nouvelle estimation, le résultat s'améliore encore :

.. code:: python

    >>> x = y
    >>> y = (x + a/x) / 2
    >>> y
    2.0064102564102564

Lorsque $y == x$, vous pouvez arrêter le calcul. Vous pouvez exprimer cela
dans une boucle :

.. code:: python

    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y

Pour la plupart des valeurs de $a$, cela fonctionne bien, mais de manière
générale, tester l'égalité stricte des nombres à virgule flottante est
dangereux. Plutôt que de vérifier si ``x`` et ``y`` sont exactement
égaux, il est plus sûr d'utiliser la fonction intégrée ``abs`` pour calculer
la valeur absolue de leur différence :

.. code:: python

    if abs(y - x) < epsilon:
        break

où ``epsilon`` a une valeur petite comme ``0.0000001`` qui détermine
la précision requise.

Algorithmes
-----------

La méthode de Newton est un exemple d'algorithme (*algorithm*) : c'est
un processus mécanique pour résoudre une catégorie de problèmes
(dans ce cas, calculer des racines carrées).

Pour comprendre ce qu'est un algorithme, il peut être utile de commencer par
ce qui n'en est pas un. L'arithmétique de base que vous avez apprise
n'est généralement pas algorithmique. Mais si vous avez appris la division
longue, vous avez appris un algorithme. Un algorithme est une suite d'étapes
systématiques, sans nécessiter d'intelligence ni d'intuition pour les exécuter.

Débogage
--------

À mesure que vous commencez à écrire des programmes plus longs, vous
pourriez vous retrouver à passer plus de temps à déboguer.
Réduire la quantité de code que vous ajoutez avant de tester (développement
incrémental) peut aider.

Une autre technique utile est la division par deux de la recherche
(*bisection*). Si vous avez 100 lignes de code et qu'il y a une erreur,
vous pouvez placer une instruction ``print`` au milieu pour vérifier
si l'état du programme est correct.
S'il l'est, l'erreur se trouve dans la seconde moitié ; sinon, elle est
dans la première. En coupant à chaque fois la zone de recherche en deux,
vous trouverez plus vite le problème.

Glossaire
---------

.. glossary::

    réaffectation
    reassignment
        Le fait d'assigner une nouvelle valeur à une variable qui
        existait déjà.

    mise à jour
    update
        Une affectation où la nouvelle valeur de la variable dépend de
        l'ancienne.

    initialisation
    initialization
        Une affectation qui donne une valeur initiale à une variable qui
        sera mise à jour par la suite.

    incrémenter
    increment
        Une mise à jour qui augmente la valeur d'une variable (souvent de 1).

    décrémenter
    decrement
        Une mise à jour qui diminue la valeur d'une variable.

    itération
    iteration
        L'exécution répétée d'un ensemble d'instructions en utilisant soit une
        fonction récursive, soit une boucle.

    boucle infinie
    infinite loop
        Une boucle dont la condition de terminaison n'est jamais satisfaite.

    algorithme
    algorithm
        Un processus général pour résoudre une catégorie de problèmes.

Exercices
---------

.. topic:: Exercice 1

    Copiez la boucle de la section sur les racines carrées et
    encapsulez-la dans une fonction appelée ``ma_racine(a)``.

    Pour tester votre fonction, écrivez une fonction nommée
    ``tester_racine_carree`` qui affiche un tableau semblable à celui-ci :

    .. code:: text

        a   ma_racine(a)      math.sqrt(a)   diff
        -   ------------      ------------   ----
        1.0 1.0               1.0            0.0
        2.0 1.41421356237     1.41421356237  2.22044604925e-16
        3.0 1.73205081001     1.73205081001  0.0
        4.0 2.0               2.0            0.0

    La première colonne correspond aux nombres de 1 à 9. La deuxième
    colonne est le résultat calculé par votre fonction ``ma_racine``.
    La troisième est le résultat de ``math.sqrt``, et la quatrième
    colonne est la différence absolue entre les deux.


.. topic:: Exercice 2

    La fonction intégrée ``eval`` prend une chaîne de caractères et
    l'évalue à l'aide de l'interpréteur Python. Par exemple :

    .. code:: python

        >>> eval('1 + 2 * 3')
        7
        >>> import math
        >>> eval('math.sqrt(5)')
        2.2360679774997898
        >>> eval('type(math.pi)')
        <class 'float'>

    Écrivez une fonction appelée ``eval_loop`` qui invite itérativement
    l'utilisateur à entrer une saisie, prend la saisie, et l'évalue
    en utilisant ``eval``, pour finalement afficher le résultat.

    Elle devrait continuer ainsi jusqu'à ce que l'utilisateur tape
    ``'done'``, et elle devrait ensuite retourner la valeur de la dernière
    expression évaluée.

.. topic:: Exercice 3

    Le brillant mathématicien Srinivasa Ramanujan a découvert une série infinie
    permettant de calculer une approximation de $\pi$ :

    $$ \frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103 + 26390k)}{(k!)^4 396^{4k}} $$

    Écrivez une fonction appelée ``estimer_pi`` qui utilise cette formule pour
    calculer et retourner une estimation de $\pi$. Elle doit utiliser une boucle
    ``while`` pour calculer les termes de la somme jusqu'à ce que le dernier
    terme calculé soit strictement inférieur à ``1e-15`` (soit la notation
    scientifique de Python pour $10^{-15}$). Vous pourrez vérifier votre
    résultat en le comparant à ``math.pi``.
