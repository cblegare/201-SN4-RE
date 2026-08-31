Classes et objets
=================

Types définis par l'utilisateur
-------------------------------

Nous avons utilisé de nombreux types intégrés de Python ; nous allons maintenant définir un nouveau type. À titre d'exemple, nous allons créer un type appelé ``Point`` qui représente un point dans un espace à deux dimensions.

En notation mathématique, les points sont souvent écrits entre parenthèses avec une virgule séparant les coordonnées. Par exemple, ``(0,0)`` représente l'origine, et ``(x,y)`` représente le point situé à $x$ unités vers la droite et $y$ unités vers le haut par rapport à l'origine.

Il existe plusieurs façons de représenter des points en Python :

* Nous pourrions stocker les coordonnées séparément dans deux variables, ``x`` et ``y``.
* Nous pourrions stocker les coordonnées comme des éléments dans une liste ou un tuple.
* Nous pourrions créer un nouveau type pour représenter les points sous forme d'objets.

Créer un nouveau type est un peu plus compliqué que les autres options, mais cela présente des avantages qui apparaîtront bientôt.

Un type défini par l'utilisateur est également appelé une **classe**. Une définition de classe ressemble à ceci :

.. code:: python

    class Point(object):
        """Représente un point dans un espace 2D."""

Cet en-tête indique que la nouvelle classe est un ``Point``, qui est une sorte d'objet, qui est un type intégré.

Le corps est une chaîne de documentation (*docstring*) qui explique le rôle de la classe. Vous pouvez définir des variables et des fonctions à l'intérieur d'une définition de classe, mais nous y reviendrons plus tard.

Définir une classe nommée ``Point`` crée un objet classe.

.. code:: python

    >>> print Point
    <class '__main__.Point'>

Parce que ``Point`` est défini au niveau supérieur, son « nom complet » est ``__main__.Point``.

L'objet classe est comme une fabrique pour créer des objets. Pour créer un ``Point``, vous appelez ``Point`` comme s'il s'agissait d'une fonction :

.. code:: python

    >>> blank = Point()
    >>> print blank
    <__main__.Point instance at 0xb7e9d3ac>

La valeur de retour est une référence à un objet ``Point``, que nous affectons à ``blank``. Créer un nouvel objet s'appelle l'**instanciation**, et l'objet est une **instance** de la classe.

Lorsque vous affichez une instance, Python vous indique à quelle classe elle appartient et où elle est stockée en mémoire (le préfixe ``0x`` signifie que le nombre suivant est en hexadécimal).

Attributs
---------

Vous pouvez affecter des valeurs à une instance en utilisant la notation pointée :

.. code:: python

    >>> blank.x = 3.0
    >>> blank.y = 4.0

Cette syntaxe est similaire à la syntaxe pour sélectionner une variable dans un module, telle que ``math.pi`` ou ``string.whitespace``. Dans ce cas, cependant, nous affectons des valeurs à des éléments nommés d'un objet. Ces éléments sont appelés des **attributs**.

Le diagramme d'état qui montre un objet et ses attributs est appelé un diagramme d'objets.

La variable ``blank`` fait référence à un objet ``Point``, qui contient deux attributs. Chaque attribut fait référence à un nombre à virgule flottante.

Vous pouvez lire la valeur d'un attribut en utilisant la même syntaxe :

.. code:: python

    >>> print blank.y
    4.0
    >>> x = blank.x
    >>> print x
    3.0

L'expression ``blank.x`` signifie : « Va à l'objet auquel ``blank`` fait référence et récupère la valeur de ``x`` ». Dans ce cas, nous affectons cette valeur à une variable nommée ``x``. Il n'y a aucun conflit entre la variable ``x`` et l'attribut ``x``.

Vous pouvez utiliser la notation pointée dans le cadre de n'importe quelle expression. Par exemple :

.. code:: python

    >>> print '(%g, %g)' % (blank.x, blank.y)
    (3.0, 4.0)
    >>> distance = math.sqrt(blank.x**2 + blank.y**2)
    >>> print distance
    5.0

Vous pouvez passer une instance en argument de la manière habituelle. Par exemple :

.. code:: python

    def print_point(p):
        print '(%g, %g)' % (p.x, p.y)

``print_point`` prend un point en argument et l'affiche en notation mathématique. Pour l'invoquer, vous pouvez passer ``blank`` comme argument :

.. code:: python

    >>> print_point(blank)
    (3.0, 4.0)

À l'intérieur de la fonction, ``p`` est un alias de ``blank``, donc si la fonction modifie ``p``, ``blank`` change.

.. topic:: Exercice

    Écrivez une fonction appelée ``distance_between_points`` qui prend deux ``Points`` en arguments et renvoie la distance qui les sépare.

Rectangles
----------

Parfois, les attributs d'un objet sont évidents, mais à d'autres moments, vous devez faire des choix. Par exemple, imaginez que vous concevez une classe pour représenter des rectangles. Quels attributs utiliseriez-vous pour spécifier l'emplacement et la taille d'un rectangle ? Vous pouvez ignorer l'angle ; pour simplifier, supposez que le rectangle est soit vertical, soit horizontal.

Il y a au moins deux possibilités :

* Vous pourriez spécifier un coin du rectangle (ou le centre), la largeur et la hauteur.
* Vous pourriez spécifier deux coins opposés.

Voici la définition de la classe :

.. code:: python

    class Rectangle(object):
        """Représente un rectangle.

        attributes: width, height, corner.
        """

La chaîne de documentation énumère les attributs : ``width`` (largeur) et ``height`` (hauteur) sont des nombres ; ``corner`` (coin) est un objet ``Point`` qui spécifie le coin inférieur gauche.

Pour représenter un rectangle, vous devez instancier un objet ``Rectangle`` et affecter des valeurs aux attributs :

.. code:: python

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

L'expression ``box.corner.x`` signifie : « Va à l'objet auquel ``box`` fait référence et sélectionne l'attribut nommé ``corner`` ; puis va à cet objet et sélectionne l'attribut nommé ``x`` ».

Un objet qui est un attribut d'un autre objet est dit **imbriqué** (*embedded*).

Instances comme valeurs de retour
--------------------------------

Les fonctions peuvent retourner des instances. Par exemple, ``find_center`` prend un ``Rectangle`` en argument et renvoie un ``Point`` qui contient les coordonnées du centre du ``Rectangle`` :

.. code:: python

    def find_center(rect):
        p = Point()
        p.x = rect.corner.x + rect.width/2.0
        p.y = rect.corner.y + rect.height/2.0
        return p

Voici un exemple qui passe ``box`` en argument et affecte le ``Point`` résultant à ``center`` :

.. code:: python

    >>> center = find_center(box)
    >>> print_point(center)
    (50.0, 100.0)

Les objets sont mutables
------------------------

Vous pouvez modifier l'état d'un objet en effectuant une affectation sur l'un de ses attributs. Par exemple, pour modifier la taille d'un rectangle sans changer sa position, vous pouvez modifier les valeurs de ``width`` et ``height`` :

.. code:: python

    box.width = box.width + 50
    box.height = box.width + 100

Vous pouvez également écrire des fonctions qui modifient des objets. Par exemple, ``grow_rectangle`` prend un objet ``Rectangle`` et deux nombres, ``dwidth`` et ``dheight``, et ajoute ces nombres à la largeur et à la hauteur du rectangle :

.. code:: python

    def grow_rectangle(rect, dwidth, dheight):
        rect.width += dwidth
        rect.height += dheight

À l'intérieur de la fonction, ``rect`` est un alias de ``box``, donc si la fonction modifie ``rect``, ``box`` change.

.. topic:: Exercice

    Écrivez une fonction nommée ``move_rectangle`` qui prend un ``Rectangle`` et deux nombres nommés ``dx`` et ``dy``. Elle doit modifier l'emplacement du rectangle en ajoutant ``dx`` à la coordonnée ``x`` de ``corner`` et ``dy`` à la coordonnée ``y`` de ``corner``.

Copie
-----

Le crénelage (*aliasing*) peut rendre un programme difficile à lire car les modifications apportées à un endroit peuvent avoir des effets inattendus ailleurs. Copier un objet est souvent une alternative au crénelage.

Le module ``copy`` contient une fonction appelée ``copy`` qui peut dupliquer n'importe quel objet :

.. code:: python

    >>> p1 = Point()
    >>> p1.x = 3.0
    >>> p1.y = 4.0

    >>> import copy
    >>> p2 = copy.copy(p1)

``p1`` et ``p2`` contiennent les mêmes données, mais ce ne sont pas le même ``Point`` :

.. code:: python

    >>> print_point(p1)
    (3.0, 4.0)
    >>> print_point(p2)
    (3.0, 4.0)
    >>> p1 is p2
    False
    >>> p1 == p2
    False

L'opérateur ``is`` indique que ``p1`` et ``p2`` ne sont pas le même objet, ce qui était attendu. Pour les instances, le comportement par défaut de l'opérateur ``==`` est le même que celui de l'opérateur ``is`` ; il vérifie l'identité de l'objet, et non son équivalence.

Si vous utilisez ``copy.copy`` pour dupliquer un ``Rectangle``, vous constaterez qu'il copie l'objet ``Rectangle`` mais pas le ``Point`` imbriqué :

.. code:: python

    >>> box2 = copy.copy(box)
    >>> box2 is box
    False
    >>> box2.corner is box.corner
    True

Cette opération est appelée une **copie superficielle** (*shallow copy*) car elle copie l'objet et toutes les références qu'il contient, mais pas les objets imbriqués.

Heureusement, le module ``copy`` contient une méthode nommée ``deepcopy`` qui copie non seulement l'objet mais aussi les objets auxquels il fait référence, et les objets auxquels ils font référence, et ainsi de suite. Cette opération est appelée une **copie profonde** (*deep copy*) :

.. code:: python

    >>> box3 = copy.deepcopy(box)
    >>> box3 is box
    False
    >>> box3.corner is box.corner
    False

``box3`` et ``box`` sont des objets complètement séparés.

.. topic:: Exercice

    Écrivez une version de ``move_rectangle`` qui crée et renvoie un nouveau ``Rectangle`` au lieu de modifier l'ancien.

Débogage
--------

Lorsque vous commencez à travailler avec des objets, vous risquez de rencontrer de nouvelles exceptions. Si vous essayez d'accéder à un attribut qui n'existe pas, vous obtenez une ``AttributeError`` :

.. code:: python

    >>> p = Point()
    >>> print p.z
    AttributeError: Point instance has no attribute 'z'

Si vous n'êtes pas sûr du type d'un objet, vous pouvez demander :

.. code:: python

    >>> type(p)
    <type '__main__.Point'>

Si vous n'êtes pas sûr qu'un objet possède un attribut particulier, vous pouvez utiliser la fonction intégrée ``hasattr`` :

.. code:: python

    >>> hasattr(p, 'x')
    True
    >>> hasattr(p, 'z')
    False

Le premier argument peut être n'importe quel objet ; le second argument est une chaîne qui contient le nom de l'attribut.

Glossaire
---------

.. glossary::

    classe
    class
        Un type défini par l'utilisateur. Une définition de classe crée un nouvel objet classe.

    objet classe
    class object
        Un objet qui contient des informations sur un type défini par l'utilisateur. L'objet classe peut être utilisé pour créer des instances du type.

    instance
    instance
        Un objet qui appartient à une classe.

    attribut
    attribute
        L'une des valeurs nommées associées à un objet.

    imbriqué (objet)
    embedded (object)
        Un objet qui est stocké en tantattribut d'un autre objet.

    copie superficielle
    shallow copy
        Copier le contenu d'un objet, y compris toutes les références à des objets imbriqués ; mis en œuvre par la fonction ``copy`` dans le module ``copy``.

    copie profonde
    deep copy
        Copier le contenu d'un objet ainsi que tous les objets imbriqués, et tous les objets imbriqués en eux, etc. ; mis en œuvre par la fonction ``deepcopy`` dans le module ``copy``.

    diagramme d'objets
    object diagram
        Un diagramme qui montre des objets, leurs attributs et les valeurs de ces attributs.

Exercices
---------

.. topic:: Exercice

    Écrivez une fonction appelée ``draw_rectangle`` qui prend un ``Canvas`` et un ``Rectangle`` en arguments et dessine une représentation du ``Rectangle`` sur le ``Canvas``.
    Ajoutez un attribut nommé ``color`` à vos objets ``Rectangle`` et modifiez ``draw_rectangle`` pour qu'il utilise l'attribut ``color`` comme couleur de remplissage.
    Écrivez une fonction appelée ``draw_point`` qui prend un ``Canvas`` et un ``Point`` en arguments et dessine une représentation du ``Point`` sur le ``Canvas``.
    Définissez une nouvelle classe appelée ``Circle`` avec des attributs appropriés et instanciez quelques objets ``Circle``. Écrivez une fonction appelée ``draw_circle`` qui dessine des cercles sur le canevas.
    Écrivez un programme qui dessine le drapeau national de la République tchèque.
    Solution : http://thinkpython.com/code/color_list.py.
