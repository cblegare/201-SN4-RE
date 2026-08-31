Classes et fonctions
====================

Temps
-----

Comme autre exemple de type défini par l'utilisateur, nous allons définir une classe appelée ``Time`` qui enregistre l'heure de la journée. La définition de classe ressemble à ceci :

.. code:: python

    class Time(object):
        """Représente l'heure de la journée.

        attributes: hour, minute, second
        """

Nous pouvons créer un nouvel objet ``Time`` et lui assigner des attributs pour les heures, les minutes et les secondes :

.. code:: python

    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30

.. topic:: Exercice

    Écrivez une fonction appelée ``print_time`` qui prend un objet ``Time`` et l'affiche sous la forme heure:minute:seconde.
    *Indice :* la séquence de format ``'%.2d'`` affiche un entier en utilisant au moins deux chiffres, incluant un zéro non significatif si nécessaire.

.. topic:: Exercice

    Écrivez une fonction booléenne appelée ``is_after`` qui prend deux objets ``Time``, ``t1`` et ``t2``, et renvoie ``True`` si ``t1`` suit ``t2`` chronologiquement, et ``False`` sinon. Défi : n'utilisez pas d'instruction ``if``.

Fonctions pures
---------------

Dans les sections suivantes, nous allons écrire deux fonctions qui additionnent des valeurs temporelles. Elles démontrent deux types de fonctions : les fonctions pures et les modificateurs. Elles illustrent également un plan de développement que j'appellerai « prototype et correctif » (*prototype and patch*), qui consiste à aborder un problème complexe en commençant par un prototype simple et en traitant les complications de manière incrémentielle.

Voici un prototype simple de ``add_time`` :

.. code:: python

    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second
        return sum

La fonction crée un nouvel objet ``Time``, initialise ses attributs et renvoie une référence vers ce nouvel objet. C'est ce qu'on appelle une **fonction pure** car elle ne modifie aucun des objets qui lui sont passés en arguments et n'a aucun effet (comme afficher une valeur ou obtenir une entrée de l'utilisateur) autre que de renvoyer une valeur.

Pour tester cette fonction, je vais créer deux objets ``Time`` : ``start`` contient l'heure de début d'un film, et ``duration`` contient la durée du film.

Le résultat ``10:80:00`` n'est peut-être pas celui que vous espériez. Le problème est que cette fonction ne gère pas les cas où le nombre de secondes ou de minutes dépasse soixante.

Voici une version améliorée :

.. code:: python

    def add_time(t1, t2):
        sum = Time()
        sum.hour = t1.hour + t2.hour
        sum.minute = t1.minute + t2.minute
        sum.second = t1.second + t2.second

        if sum.second >= 60:
            sum.second -= 60
            sum.minute += 1

        if sum.minute >= 60:
            sum.minute -= 60
            sum.hour += 1

        return sum

Bien que cette fonction soit correcte, elle commence à devenir volumineuse.

Modificateurs
-------------

Il est parfois utile qu'une fonction modifie les objets qu'elle reçoit en paramètres. Dans ce cas, les modifications sont visibles pour l'appelant. Les fonctions qui fonctionnent de cette manière sont appelées des **modificateurs**.

``increment``, qui ajoute un nombre donné de secondes à un objet ``Time``, peut s'écrire naturellement comme un modificateur :

.. code:: python

    def increment(time, seconds):
        time.second += seconds

        if time.second >= 60:
            time.second -= 60
            time.minute += 1

        if time.minute >= 60:
            time.minute -= 60
            time.hour += 1

Que se passe-t-il si le paramètre ``seconds`` est bien supérieur à soixante ? Dans ce cas, il ne suffit pas de reporter la retenue une seule fois. Une solution consiste à remplacer les instructions ``if`` par des boucles ``while``, mais cela rendrait la fonction inefficace.

.. topic:: Exercice

    Écrivez une version correcte de ``increment`` qui ne contient aucune boucle.

En général, je vous recommande d'écrire des fonctions pures chaque fois que c'est raisonnable et de recourir aux modificateurs uniquement s'il y a un avantage incontestable. Cette approche peut être qualifiée de **style de programmation fonctionnelle**.

.. topic:: Exercice

    Écrivez une version « pure » de ``increment`` qui crée et renvoie un nouvel objet ``Time`` plutôt de modifier le paramètre.

Prototypage versus planification
---------------------------------

Le plan de développement présenté est le « prototype et correctif ». Une alternative est le **développement planifié**, où une compréhension globale du problème peut grandement faciliter la programmation.

L'observation clé est qu'un objet ``Time`` est en réalité un nombre à trois chiffres en base 60. L'attribut ``second`` est la colonne des « unités », l'attribut ``minute`` est la colonne des « soixantaines », et l'attribut ``hour`` est la colonne des « trente-six centaines ».

Cela suggère une autre approche : nous pouvons convertir les objets ``Time`` en entiers, effectuer l'arithmétique, puis reconvertir.

Voici la fonction qui convertit les objets ``Time`` en entiers :

.. code:: python

    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

Et voici la fonction qui convertit les entiers en objets ``Time`` :

.. code:: python

    def int_to_time(seconds):
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

Une fois convaincu de leur exactitude, vous pouvez les utiliser pour réécrire ``add_time`` :

.. code:: python

    def add_time(t1, t2):
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

Cette version est plus courte que l'originale et plus facile à vérifier.

.. topic:: Exercice

    Réécrivez ``increment`` en utilisant ``time_to_int`` et ``int_to_time``.

Débogage
--------

Un objet ``Time`` est bien formé si les valeurs de ``minute`` et ``second`` sont comprises entre 0 et 60 (inclus mais excluant 60) et si ``hour`` est positif. De telles conditions sont appelées des **invariants** car elles doivent toujours être vraies.

Écrire du code pour vérifier vos invariants peut vous aider à détecter les erreurs :

.. code:: python

    def valid_time(time):
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

Vous pouvez utiliser une instruction ``assert`` pour vérifier un invariant et lever une exception en cas d'échec :

.. code:: python

    def add_time(t1, t2):
        assert valid_time(t1) and valid_time(t2)
        seconds = time_to_int(t1) + time_to_int(t2)
        return int_to_time(seconds)

Glossaire
---------

.. glossary::

    prototype et correctif
    prototype and patch
        Un plan de développement qui consiste à écrire un premier brouillon d'un programme, à le tester et à corriger les erreurs au fur et à mesure qu'elles sont découvertes.

    développement planifié
    planned development
        Un plan de développement qui implique une vision globale du problème et davantage de planification qu'un développement incrémentiel.

    fonction pure
    pure function
        Une fonction qui ne modifie aucun des objets qu'elle reçoit en arguments.

    modificateur
    modifier
        Une fonction qui change un ou plusieurs des objets qu'elle reçoit en arguments.

    style de programmation fonctionnelle
    functional programming style
        Un style de conception de programme dans lequel la majorité des fonctions sont pures.

    invariant
    invariant
        Une condition qui doit toujours être vraie pendant l'exécution d'un programme.

Exercices
---------

.. topic:: Exercice

    Écrivez une fonction appelée ``mul_time`` qui prend un objet ``Time`` et un nombre, et renvoie un nouvel objet ``Time`` contenant le produit du temps initial et du nombre.
    Utilisez ensuite ``mul_time`` pour écrire une fonction qui prend le temps d'arrivée d'une course et la distance, et renvoie le rythme moyen (temps par mile).

.. topic:: Exercice

    Le module ``datetime`` fournit des objets de date et d'heure similaires aux objets de ce chapitre. Lisez la documentation sur http://docs.python.org/2/library/datetime.html et utilisez ce module pour écrire un programme qui obtient la date courante et affiche le jour de la semaine, un programme calculant l'âge et le temps restant avant le prochain anniversaire, ainsi qu'un programme calculant le « Double Jour » où une personne a deux fois l'âge d'une autre.
