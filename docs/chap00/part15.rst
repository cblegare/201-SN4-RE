==========
 Héritage
==========

--------------
 Objets Carte
--------------

Il y a cinquante-deux cartes dans un jeu, dont chacune appartient à l'une des
quatre couleurs et l'une des treize valeurs. Pour représenter une carte à jouer,
les attributs évidents sont la valeur (*rank*) et la couleur (*suit*). Une
alternative pour les représenter consiste à utiliser des entiers pour encoder
les valeurs et les couleurs, ce qui permet de comparer facilement les cartes.

La définition de la classe ``Card`` ressemble à ceci :

.. code-block:: python

    class Card(object):
        """Représente une carte à jouer standard."""

        def __init__(self, suit=0, rank=2):
            self.suit = suit
            self.rank = rank

---------------------
 Attributs de classe
---------------------

Pour afficher les objets ``Card`` d'une manière lisible, nous pouvons utiliser
des attributs de classe définis à l'intérieur de la classe mais en dehors de
toute méthode :

.. code-block:: python

    # à l'intérieur de la classe Card :

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [
        None,
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]


    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

Les variables comme ``suit_names`` et ``rank_names`` sont appelées des
**attributs de classe** car elles sont associées à l'objet classe ``Card``,
tandis que ``suit`` et ``rank`` sont des attributs d'instance.

-----------------------
 Comparaison de cartes
-----------------------

Pour les types intégrés, les opérateurs relationnels comparent les valeurs. Pour
les types définis par l'utilisateur, nous pouvons redéfinir ce comportement en
fournissant une méthode nommée ``__cmp__`` qui prend deux paramètres, ``self``
et ``other``.

En Python 3, la méthode ``__cmp__`` n'est pas prise en charge et il convient
plutôt de fournir ``__lt__``.

----------------
 Jeux de cartes
----------------

Puisqu'un jeu de cartes (*deck*) est composé de cartes, il est naturel qu'il
contienne une liste de cartes comme attribut. La méthode d'initialisation crée
l'attribut ``cards`` et génère les cinquante-deux cartes standard :

.. code-block:: python

    class Deck(object):

        def __init__(self):
            self.cards = []
            for suit in range(4):
                for rank in range(1, 14):
                    card = Card(suit, rank)
                    self.cards.append(card)

------------------------------------
 Ajout, suppression, mélange et tri
------------------------------------

Pour distribuer des cartes, nous pouvons utiliser la méthode de liste ``pop``
pour retirer une carte du jeu :

.. code-block:: python

    # à l'intérieur de la classe Deck :


    def pop_card(self):
        return self.cards.pop()

Pour ajouter une carte, nous pouvons utiliser la méthode ``append`` :

.. code-block:: python

    # à l'intérieur de la classe Deck :


    def add_card(self, card):
        self.cards.append(card)

Une méthode de ce type qui utilise une autre fonction sans effectuer de travail
complexe est parfois appelée un **placage** (*veneer*). Nous pouvons également
écrire une méthode de mélange (*shuffle*) en utilisant la fonction ``shuffle``
du module ``random`` :

.. code-block:: python

    # à l'intérieur de la classe Deck :


    def shuffle(self):
        random.shuffle(self.cards)

----------
 Héritage
----------

La fonctionnalité de langage la plus souvent associée à la programmation
orientée objet est l'**héritage**, qui est la capacité de définir une nouvelle
classe constituant une version modifiée d'une classe existante. La classe
existante est appelée la **classe parente** et la nouvelle classe est appelée la
**classe enfant** ou sous-classe.

Par exemple, pour représenter une « main » de cartes détenue par un joueur, nous
pouvons créer une classe ``Hand`` qui hérite de ``Deck`` :

.. code-block:: python

    class Hand(Deck):
        """Représente une main de cartes à jouer."""

Cette définition indique que ``Hand`` hérite de ``Deck``, ce qui signifie que
nous pouvons utiliser des méthodes comme ``pop_card`` et ``add_card`` pour les
mains ainsi que pour les jeux. Si nous fournissons une méthode ``__init__`` dans
la classe ``Hand``, elle remplace celle de la classe ``Deck`` :

.. code-block:: python

    # à l'intérieur de la classe Hand :


    def __init__(self, label=""):
        self.cards = []
        self.label = label

-----------------------
 Diagrammes de classes
-----------------------

Un **diagramme de classes** est une représentation plus abstraite de la
structure d'un programme qui montre les classes et leurs relations :

* **Relation HAS-A (a un)** : les objets d'une classe contiennent des références
  à des objets d'une autre classe (par exemple, chaque ``Deck`` contient des
  références à de nombreuses ``Cards``).
* **Relation IS-A (est un)** : une classe hérite d'une autre (par exemple, un
  ``Hand`` est une sorte de ``Deck``).

La multiplicité (comme une étoile ``*`` près de la tête de flèche) indique le
nombre d'instances concernées dans une relation.

----------
 Débogage
----------

L'héritage peut représenter un défi pour le débogage car lorsqu'une méthode est
invoquée sur un objet, il n'est parfois pas évident de savoir quelle
implémentation sera exécutée. La fonction ``find_defining_class`` permet de
trouver la classe qui fournit la définition d'une méthode en inspectant l'ordre
de résolution des méthodes (MRO).

---------------------------
 Encapsulation des données
---------------------------

De la même manière que nous avons découvert des interfaces de fonctions par
l'encapsulation et la généralisation, nous pouvons découvrir des interfaces de
classes par l'**encapsulation des données**. Le processus de refactorisation
consiste à transformer un ensemble de variables globales et de fonctions
associées en attributs et méthodes d'une nouvelle classe.

-----------
 Glossaire
-----------

.. glossary::

    encoder
    encode
        Représenter un ensemble de valeurs en utilisant un autre ensemble de valeurs en construisant une correspondance entre eux.

    attribut de classe
    class attribute
        Un attribut associé à un objet classe, défini à l'intérieur d'une définition de classe mais en dehors de toute méthode.

    attribut d'instance
    instance attribute
        Un attribut associé à une instance spécifique d'une classe.

    placage
    veneer
        Une méthode ou une fonction qui fournit une interface différente pour une autre fonction sans effectuer de calculs complexes.

    héritage
    inheritance
        La capacité de définir une nouvelle classe qui est une version modifiée d'une classe définie précédemment.

    classe parente
    parent class
        La classe à partir de laquelle une classe enfant hérite.

    classe enfant
    child class
        Une nouvelle classe créée en héritant d'une classe existante ; également appelée « sous-classe ».

    relation IS-A
    IS-A relationship
        La relation entre une classe enfant et sa classe parente.

    relation HAS-A
    HAS-A relationship
        La relation entre deux classes où les instances d'une classe contiennent des références à des instances de l'autre.

    diagramme de classes
    class diagram
        Un diagramme qui montre les classes d'un programme et les relations entre elles.

    multiplicité
    multiplicity
        Une notation dans un diagramme de classes qui indique, pour une relation HAS-A, le nombre de références vers des instances d'une autre classe.
