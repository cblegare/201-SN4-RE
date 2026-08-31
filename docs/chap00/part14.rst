Classes et méthodes
===================

Fonctionnalités orientées objet
-------------------------------

Python est un langage de programmation orienté objet, ce qui signifie qu'il fournit des fonctionnalités qui prennent en charge la programmation orientée objet[cite: 1].

Il n'est pas facile de définir la programmation orientée objet, mais nous en avons déjà vu certaines caractéristiques :

* Les programmes sont constitués de définitions d'objets et de fonctions, et la plus grande partie du calcul s'exprime en termes d'opérations sur les objets[cite: 1].
* Chaque définition d'objet correspond à un objet ou à un concept du monde réel, et les fonctions qui opèrent sur cet objet correspondent aux manières dont les objets du monde réel interagissent[cite: 1].

Jusqu'à présent, nous n'avons pas profité des fonctionnalités que Python fournit pour prendre en charge la programmation orientée objet[cite: 1]. Ces fonctionnalités ne sont pas strictement nécessaires ; la plupart d'entre elles fournissent une syntaxe alternative pour des choses que nous avons déjà faites[cite: 1]. Mais dans de nombreux cas, l'alternative est plus concise et exprime plus précisément la structure du programme[cite: 1].

Une méthode est une fonction qui est associée à une classe particulière[cite: 1]. Les méthodes sont sémantiquement identiques aux fonctions, mais il y existe deux différences syntaxiques[cite: 1] :

* Les méthodes sont définies à l'intérieur d'une définition de classe afin de rendre explicite la relation entre la classe et la méthode[cite: 1].
* La syntaxe pour invoquer une méthode est différente de la syntaxe pour appeler une fonction[cite: 1].

Impression d'objets
-------------------

Pour transformer une fonction en méthode, tout ce que nous avons à faire est de déplacer la définition de la fonction à l'intérieur de la définition de la classe[cite: 1]. Par convention, le premier paramètre d'une méthode est appelé ``self``[cite: 1].

Dans la programmation orientée objet, les objets sont les agents actifs[cite: 1]. Une invocation de méthode comme ``start.print_time()`` signifie « Hé start ! S'il te plaît, affiche-toi »[cite: 1].

.. topic:: Exercice

    Réécrivez ``time_to_int`` (de la section 16.4) sous forme de méthode[cite: 1].

Un autre exemple
----------------

Voici une version de ``increment`` (de la section 16.3) réécrite sous forme de méthode[cite: 1] :

.. code:: python

    # à l'intérieur de la classe Time :

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

Le sujet, ``start``, est affecté au premier paramètre, ``self``[cite: 1]. L'argument, ``1337``, est affecté au second paramètre, ``seconds``[cite: 1].

Un exemple plus compliqué
-------------------------

``is_after`` est légèrement plus compliqué car il prend deux objets ``Time`` comme paramètres[cite: 1]. Dans ce cas, il est conventionnel de nommer le premier paramètre ``self`` et le second paramètre ``other``[cite: 1] :

.. code:: python

    # à l'intérieur de la classe Time :

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

La méthode ``init``
-------------------

La méthode ``init`` (abréviation d'« initialisation ») est une méthode spéciale qui est invoquée lorsqu'un objet est instancié[cite: 1]. Son nom complet est ``__init__``[cite: 1].

Une méthode ``init`` pour la classe ``Time`` pourrait ressembler à ceci[cite: 1] :

.. code:: python

    # à l'intérieur de la classe Time :

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

Les paramètres sont optionnels, donc si vous appelez ``Time`` sans arguments, vous obtenez les valeurs par défaut[cite: 1].

.. topic:: Exercice

    Écrivez une méthode ``init`` pour la classe ``Point`` qui prend ``x`` et ``y`` comme paramètres optionnels et les affecte aux attributs correspondants[cite: 1].

La méthode ``__str__``
----------------------

``__str__`` est une méthode spéciale, comme ``__init__``, qui est censée renvoyer une représentation sous forme de chaîne de caractères d'un objet[cite: 1].

.. code:: python

    # à l'intérieur de la classe Time :

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

Lorsque vous affichez un objet, Python invoque la méthode ``str``[cite: 1].

.. topic:: Exercice

    Écrivez une méthode ``str`` pour la classe ``Point``. Créez un objet ``Point`` et affichez-le[cite: 1].

Surcharge des opérateurs
-------------------------

En définissant d'autres méthodes spéciales, vous pouvez spécifier le comportement des opérateurs sur les types définis par l'utilisateur[cite: 1]. Par exemple, si vous définissez une méthode nommée ``__add__`` pour la classe ``Time``, vous pouvez utiliser l'opérateur ``+`` sur les objets ``Time``[cite: 1].

.. code:: python

    # à l'intérieur de la classe Time :

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

Modifier le comportement d'un opérateur pour qu'il fonctionne avec des types définis par l'utilisateur s'appelle la **surcharge des opérateurs**[cite: 1].

.. topic:: Exercice

    Écrivez une méthode ``add`` pour la classe ``Point``[cite: 1].

Répartition basée sur le type
------------------------------

La fonction intégrée ``isinstance`` prend une valeur et un objet classe, et renvoie ``True`` si la valeur est une instance de la classe[cite: 1].

Cette opération est appelée une **répartition basée sur le type** (*type-based dispatch*) parce qu'elle répartit le calcul vers différentes méthodes en fonction du type des arguments[cite: 1].

La méthode spéciale ``__radd__`` signifie « addition côté droit » (*right-side add*)[cite: 1]. Cette méthode est invoquée lorsqu'un objet ``Time`` apparaît du côté droit de l'opérateur ``+``[cite: 1].

.. topic:: Exercice

    Écrivez une méthode ``add`` pour les points qui fonctionne soit avec un objet ``Point``, soit avec un tuple[cite: 1].

Polymorphisme
-------------

Les fonctions qui peuvent fonctionner avec plusieurs types sont dites **polymorphes**[cite: 1]. Le polymorphisme peut faciliter la réutilisation du code[cite: 1].

En général, si toutes les opérations à l'intérieur d'une fonction fonctionnent avec un type donné, alors la fonction fonctionne avec ce type[cite: 1].

Débogage
--------

Une autre façon d'accéder aux attributs d'un objet est d'utiliser l'attribut spécial ``__dict__``, qui est un dictionnaire qui associe des noms d'attributs (sous forme de chaînes) et des valeurs[cite: 1].

La fonction intégrée ``getattr`` prend un objet et un nom d'attribut (sous forme de chaîne) et renvoie la valeur de l'attribut[cite: 1].

Interface et implémentation
---------------------------

Un principe de conception qui aide à atteindre l'objectif de maintenabilité est de **garder les interfaces séparées des implémentations**[cite: 1]. Pour les objets, cela signifie que les méthodes fournies par une classe ne doivent pas dépendre de la façon dont les attributs sont représentés[cite: 1].

Garder l'interface séparée de l'implémentation signifie que vous devez cacher les attributs. Le code dans les autres parties du programme doit utiliser des méthodes pour lire et modifier l'état de l'objet, sans accéder directement aux attributs[cite: 1]. Ce principe est appelé **masquage de l'information** (*information hiding*)[cite: 1].

.. topic:: Exercice

    Téléchargez le code de ce chapitre (http://thinkpython.com/code/Time2.py). Modifiez les attributs de ``Time`` pour qu'ils soient un seul entier représentant les secondes depuis minuit[cite: 1]. Modifiez ensuite les méthodes (et la fonction ``int_to_time``) pour qu'elles fonctionnent avec la nouvelle implémentation[cite: 1].

Glossaire
---------

.. glossary::

    langage orienté objet
    object-oriented language
        Un langage qui fournit des fonctionnalités, telles que des classes définies par l'utilisateur et une syntaxe de méthode, qui facilitent la programmation orientée objet[cite: 1].

    programmation orientée objet
    object-oriented programming
        Un style de programmation dans lequel les données et les opérations qui les manipulent sont organisées en classes et en méthodes[cite: 1].

    méthode
    method
        Une fonction qui est définie à l'intérieur d'une définition de classe et est invoquée sur des instances de cette classe[cite: 1].

    sujet
    subject
        L'objet sur lequel une méthode est invoquée[cite: 1].

    surcharge des opérateurs
    operator overloading
        Modifier le comportement d'un opérateur comme ``+`` pour qu'il fonctionne avec un type défini par l'utilisateur[cite: 1].

    répartition basée sur le type
    type-based dispatch
        Un modèle de programmation qui vérifie le type d'un opérande et invoque différentes fonctions pour différents types[cite: 1].

    polymorphe
    polymorphic
        Relatif à une fonction qui peut fonctionner avec plus d'un type[cite: 1].

    masquage de l'information
    information hiding
        Le principe selon lequel l'interface fournie par un objet ne doit pas dépendre de son implémentation, en particulier de la représentation de ses attributs[cite: 1].

Exercices
---------

.. topic:: Exercice

    Écrivez une définition pour une classe nommée ``Kangaroo`` avec les méthodes suivantes : une méthode ``__init__`` qui initialise un attribut nommé ``pouch_contents`` à une liste vide ; une méthode nommée ``put_in_pouch`` qui ajoute un objet à la poche ; et une méthode ``__str__`` pour afficher le kangourou et le contenu de sa poche[cite: 1].

.. topic:: Exercice

    Le module ``Visual`` fournit des graphiques 3D[cite: 1]. Modifiez le programme pour que chaque sphère dans un cube ait la couleur qui correspond à sa position dans l'espace RGB[cite: 1].
