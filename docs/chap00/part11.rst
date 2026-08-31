Fichiers
========

Persistance
-----------

La plupart des programmes que nous avons vus jusqu'à présent sont éphémères dans le sens où ils s'exécutent pendant un court moment et produisent un certain résultat, mais lorsqu'ils se terminent, leurs données disparaissent. Si vous relancez le programme, il repart sur une feuille blanche[cite: 1].

D'autres programmes sont persistants : ils s'exécutent longtemps (ou en continu) ; ils conservent au moins une partie de leurs données dans un stockage permanent (un disque dur, par exemple) ; et s'ils s'arrêtent et redémarrent, ils reprennent là où ils s'étaient arrêtés. Des exemples de programmes persistants sont les systèmes d'exploitation, qui s'exécutent à peu près chaque fois qu'un ordinateur est allumé, et les serveurs web, qui fonctionnent en permanence en attendant que des requêtes arrivent sur le réseau[cite: 1].

L'un des moyens les plus simples pour les programmes de conserver leurs données consiste à lire et à écrire des fichiers texte. Nous avons déjà vu des programmes qui lisent des fichiers texte ; dans ce chapitre, nous verrons des programmes qui en écrivent[cite: 1].

Une alternative est de stocker l'état du programme dans une base de données. Dans ce chapitre, je présenterai une base de données simple et un module, ``pickle``, qui facilite le stockage des données de programmes[cite: 1].

Lecture et écriture
-------------------

Un fichier texte est une séquence de caractères stockée sur un support permanent comme un disque dur, une mémoire flash ou un cédérom. Nous avons vu comment ouvrir et lire un fichier à la section 9.1[cite: 1].

Pour écrire dans un fichier, vous devez l'ouvrir avec le mode ``'w'`` comme second paramètre[cite: 1] :

.. code:: python

    >>> fout = open('output.txt', 'w')
    >>> print fout
    <open file 'output.txt', mode 'w' at 0xb7eb2410>

Si le fichier existe déjà, l'ouvrir en mode écriture efface les anciennes données et repart à neuf, alors soyez prudent ! Si le fichier n'existe pas, un nouveau est créé[cite: 1].

La méthode ``write`` place des données dans le fichier[cite: 1] :

.. code:: python

    >>> line1 = "This here's the wattle,\n"
    >>> fout.write(line1)

Encore une fois, l'objet fichier garde une trace de sa position, donc si vous appelez ``write`` à nouveau, il ajoute les nouvelles données à la fin[cite: 1].

.. code:: python

    >>> line2 = "the emblem of our land.\n"
    >>> fout.write(line2)

Lorsque vous avez fini d'écrire, vous devez fermer le fichier[cite: 1] :

.. code:: python

    >>> fout.close()

Opérateur de formatage
----------------------

L'argument de ``write`` doit être une chaîne de caractères, donc si nous voulons placer d'autres valeurs dans un fichier, nous devons les convertir en chaînes. Le moyen le plus simple d'y parvenir est d'utiliser ``str``[cite: 1] :

.. code:: python

    >>> x = 52
    >>> fout.write(str(x))

Une alternative consiste à utiliser l'opérateur de formatage, ``%``. Lorsqu'il est appliqué à des entiers, ``%`` est l'opérateur modulo. Mais lorsque le premier opérande est une chaîne, ``%`` est l'opérateur de formatage[cite: 1].

Le premier opérande est la chaîne de format, qui contient une ou plusieurs séquences de format spécifiant comment le second opérande est formaté. Le résultat est une chaîne de caractères[cite: 1].

Par exemple, la séquence de format ``'%d'`` signifie que le second opérande doit être formaté en tant qu'entier (le « d » signifie « décimal »)[cite: 1] :

.. code:: python

    >>> camels = 42
    >>> '%d' % camels
    '42'

Le résultat est la chaîne ``'42'``, à ne pas confondre avec la valeur entière 42[cite: 1].

Une séquence de format peut apparaître n'importe où dans la chaîne, ce qui vous permet d'intégrer une valeur dans une phrase[cite: 1] :

.. code:: python

    >>> camels = 42
    >>> 'I have spotted %d camels.' % camels
    'I have spotted 42 camels.'

S'il y a plus d'une séquence de format dans la chaîne, le second argument doit être un tuple. Chaque séquence de format correspond à un élément du tuple, dans l'ordre[cite: 1].

L'exemple suivant utilise ``'%d'`` pour formater un entier, ``'%g'`` pour formater un nombre à virgule flottante (ne demandez pas pourquoi), et ``'%s'`` pour formater une chaîne[cite: 1] :

.. code:: python

    >>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
    'In 3 years I have spotted 0.1 camels.'

Le nombre d'éléments dans le tuple doit correspondre au nombre de séquences de format dans la chaîne. De plus, les types des éléments doivent correspondre aux séquences de format[cite: 1] :

.. code:: python

    >>> '%d %d %d' % (1, 2)
    TypeError: not enough arguments for format string
    >>> '%d' % 'dollars'
    TypeError: illegal argument type for built-in operation

Dans le premier exemple, il n'y a pas assez d'éléments ; dans le second, l'élément est du mauvais type[cite: 1].

L'opérateur de formatage est puissant, mais il peut s'avérer difficile à utiliser. Vous pouvez en lire davantage à son sujet sur http://docs.python.org/2/library/stdtypes.html#string-formatting[cite: 1].

Noms de fichiers et chemins
--------------------------

Les fichiers sont organisés en répertoires (également appelés « dossiers »). Chaque programme en cours d'exécution possède un « répertoire courant », qui est le répertoire par défaut pour la plupart des opérations[cite: 1].

Par exemple, lorsque vous ouvrez un fichier en lecture, Python le recherche dans le répertoire courant[cite: 1].

Le module ``os`` fournit des fonctions pour travailler avec les fichiers et les répertoires (« os » signifie « operating system »). ``os.getcwd`` renvoie le nom du répertoire courant[cite: 1] :

.. code:: python

    >>> import os
    >>> cwd = os.getcwd()
    >>> print cwd
    /home/dinsdale

``cwd`` signifie « current working directory » (répertoire de travail courant). Le résultat dans cet exemple est ``/home/dinsdale``, qui est le répertoire personnel d'un utilisateur nommé ``dinsdale``[cite: 1].

Une chaîne comme ``cwd`` qui identifie un fichier est appelée un **chemin** (*path*). Un chemin relatif part du répertoire courant ; un chemin absolu part du répertoire le plus haut du système de fichiers[cite: 1].

Les chemins que nous avons vus jusqu'à présent sont de simples noms de fichiers, ils sont donc relatifs au répertoire courant. Pour trouver le chemin absolu d'un fichier, vous pouvez utiliser ``os.path.abspath``[cite: 1] :

.. code:: python

    >>> os.path.abspath('memo.txt')
    '/home/dinsdale/memo.txt'

``os.path.exists`` vérifie si un fichier ou un répertoire existe[cite: 1] :

.. code:: python

    >>> os.path.exists('memo.txt')
    True

S'il existe, ``os.path.isdir`` vérifie s'il s'agit d'un répertoire[cite: 1] :

.. code:: python

    >>> os.path.isdir('memo.txt')
    False
    >>> os.path.isdir('music')
    True

De même, ``os.path.isfile`` vérifie s'il s'agit d'un fichier[cite: 1].

``os.listdir`` renvoie une liste des fichiers (et autres répertoires) dans le répertoire donné[cite: 1] :

.. code:: python

    >>> os.listdir(cwd)
    ['music', 'photos', 'memo.txt']

Pour illustrer ces fonctions, l'exemple suivant « parcourt » (*walks*) un répertoire, affiche les noms de tous les fichiers et s'appelle lui-même de manière récursive sur tous les répertoires[cite: 1].

.. code:: python

    def walk(dirname):
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)

            if os.path.isfile(path):
                print path
            else:
                walk(path)

``os.path.join`` prend un répertoire et un nom de fichier et les combine pour former un chemin complet[cite: 1].

.. topic:: Exercice

    Le module ``os`` fournit une fonction appelée ``walk`` qui est similaire à celle-ci mais plus polyvalente. Lisez la documentation et utilisez-la pour afficher les noms des fichiers dans un répertoire donné et ses sous-répertoires[cite: 1].
    Solution : http://thinkpython.com/code/walk.py[cite: 1].

Capture d'exceptions
--------------------

Beaucoup de choses peuvent mal tourner lorsque vous essayez de lire et d'écrire des fichiers. Si vous essayez d'ouvrir un fichier qui n'existe pas, vous obtenez une ``IOError``[cite: 1] :

.. code:: python

    >>> fin = open('bad_file')
    IOError: [Errno 2] No such file or directory: 'bad_file'

Si vous n'avez pas la permission d'accéder à un fichier[cite: 1] :

.. code:: python

    >>> fout = open('/etc/passwd', 'w')
    IOError: [Errno 13] Permission denied: '/etc/passwd'

Et si vous essayez d'ouvrir un répertoire en lecture, vous obtenez[cite: 1] :

.. code:: python

    >>> fin = open('/home')
    IOError: [Errno 21] Is a directory

Pour éviter ces erreurs, vous pourriez utiliser des fonctions comme ``os.path.exists`` et ``os.path.isfile``, mais cela prendrait beaucoup de temps et de code pour vérifier toutes les possibilités (si « Errno 21 » est un indice, il y a au moins 21 choses qui peuvent mal tourner)[cite: 1].

Il vaut mieux foncer et essayer — et gérer les problèmes s'ils surviennent —, ce qui est précisément ce que fait l'instruction ``try``. La syntaxe est similaire à une instruction ``if``[cite: 1] :

.. code:: python

    try:
        fin = open('bad_file')
        for line in fin:
            print line
        fin.close()
    except:
        print 'Something went wrong.'

Python commence par exécuter la clause ``try``. Si tout se passe bien, il ignore la clause ``except`` et continue. Si une exception se produit, il sort de la clause ``try`` et exécute la clause ``except``[cite: 1].

Gérer une exception avec une instruction ``try`` s'appelle **capturer** (*catch*) une exception. Dans cet exemple, la clause ``except`` affiche un message d'erreur qui n'est pas très utile. En général, capturer une exception vous donne l'opportunité de résoudre le problème, de réessayer, ou du moins de quitter le programme proprement[cite: 1].

.. topic:: Exercice

    Écrivez une fonction appelée ``sed`` qui prend comme arguments une chaîne modèle, une chaîne de remplacement et deux noms de fichiers ; elle doit lire le premier fichier et écrire le contenu dans le second fichier (en le créant si nécessaire). Si la chaîne modèle apparaît n'importe où dans le fichier, elle doit être remplacée par la chaîne de remplacement[cite: 1].
    Si une erreur se produit lors de l'ouverture, de la lecture, de l'écriture ou de la fermeture de fichiers, votre programme doit capturer l'exception, afficher un message d'erreur et se terminer[cite: 1].
    Solution : http://thinkpython.com/code/sed.py[cite: 1].

Bases de données
----------------

Une base de données est un fichier organisé pour stocker des données. La plupart des bases de données sont organisées comme un dictionnaire en ce sens qu'elles associent des clés à des valeurs. La plus grande différence est que la base de données se trouve sur le disque (ou un autre stockage permanent), de sorte qu'elle persiste après la fin du programme[cite: 1].

Le module ``anydbm`` fournit une interface pour créer et mettre à jour des fichiers de bases de données. À titre d'exemple, je vais créer une base de données qui contient des légendes pour des fichiers d'images[cite: 1].

L'ouverture d'une base de données est similaire à l'ouverture d'autres fichiers[cite: 1] :

.. code:: python

    >>> import anydbm
    >>> db = anydbm.open('captions.db', 'c')

Le mode ``'c'`` signifie que la base de données doit être créée si elle n'existe pas déjà. Le résultat est un objet base de données qui peut être utilisé (pour la plupart des opérations) comme un dictionnaire[cite: 1].

Si vous créez un nouvel élément, ``anydbm`` met à jour le fichier de la base de données[cite: 1] :

.. code:: python

    >>> db['cleese.png'] = 'Photo of John Cleese.'

Lorsque vous accédez à l'un des éléments, ``anydbm`` lit le fichier[cite: 1] :

.. code:: python

    >>> print db['cleese.png']
    Photo of John Cleese.

Si vous effectuez une autre affectation sur une clé existante, ``anydbm`` remplace l'ancienne valeur[cite: 1] :

.. code:: python

    >>> db['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
    >>> print db['cleese.png']
    Photo of John Cleese doing a silly walk.

De nombreuses méthodes de dictionnaires, comme ``keys`` et ``items``, fonctionnent également avec les objets de bases de données. L'itération avec une instruction ``for`` fonctionne de même[cite: 1].

.. code:: python

    for key in db:
        print key

Comme avec les autres fichiers, vous devez fermer la base de données lorsque vous avez terminé[cite: 1] :

.. code:: python

    >>> db.close()

Sérialisation (Pickling)
------------------------

Une limitation de ``anydbm`` est que les clés et les valeurs doivent être des chaînes de caractères. Si vous essayez d'utiliser un autre type, vous obtenez une erreur[cite: 1].

Le module ``pickle`` peut aider. Il traduit presque n'importe quel type d'objet en une chaîne adaptée au stockage dans une base de données, puis retransforme les chaînes en objets[cite: 1].

``pickle.dumps`` prend un objet en paramètre et renvoie une représentation sous forme de chaîne (« dumps » est l'abréviation de « dump string »)[cite: 1] :

.. code:: python

    >>> import pickle
    >>> t = [1, 2, 3]
    >>> pickle.dumps(t)
    '(lp0\nI1\naI2\naI3\na.'

Le format n'est pas évident pour les lecteurs humains ; il est conçu pour être facilement interprété par ``pickle``. ``pickle.loads`` (« load string ») reconstitue l'objet[cite: 1] :

.. code:: python

    >>> t1 = [1, 2, 3]
    >>> s = pickle.dumps(t1)
    >>> t2 = pickle.loads(s)
    >>> print t2
    [1, 2, 3]

Bien que le nouvel objet ait la même valeur que l'ancien, ce n'est (en général) pas le même objet[cite: 1] :

.. code:: python

    >>> t1 == t2
    True
    >>> t1 is t2
    False

En d'autres termes, sérialiser puis désérialiser (*pickling and unpickling*) a le même effet que copier l'objet[cite: 1].

Vous pouvez utiliser ``pickle`` pour stocker des types autres que des chaînes dans une base de données. En fait, cette combinaison est si courante qu'elle a été encapsulée dans un module appelé ``shelve``[cite: 1].

.. topic:: Exercice

    Si vous téléchargez ma solution à l'Exercice 4 depuis http://thinkpython.com/code/anagram_sets.py, vous verrez qu'elle crée un dictionnaire qui associe une chaîne triée de lettres à la liste des mots qui peuvent être épelés avec ces lettres. Par exemple, ``'opst'`` est associé à la liste ``['opts', 'post', 'pots', 'spot', 'stop', 'tops']``[cite: 1].
    Écrivez un module qui importe ``anagram_sets`` et fournit deux nouvelles fonctions : ``store_anagrams`` devrait stocker le dictionnaire d'anagrammes dans un « shelf » ; ``read_anagrams`` devrait rechercher un mot et renvoyer la liste de ses anagrammes[cite: 1].
    Solution : http://thinkpython.com/code/anagram_db.py[cite: 1].

Pipes
-----

La plupart des systèmes d'exploitation fournissent une interface en ligne de commande, également connue sous le nom de *shell*. Les shells fournissent généralement des commandes pour naviguer dans le système de fichiers et lancer des applications. Par exemple, sous Unix, vous pouvez changer de répertoire avec ``cd``, afficher le contenu d'un répertoire avec ``ls``, et lancer un navigateur web en tapant (par exemple) ``firefox``[cite: 1].

N'importe quel programme que vous pouvez lancer depuis le shell peut également être lancé depuis Python en utilisant un **pipe**. Un pipe est un objet qui représente un programme en cours d'exécution[cite: 1].

Par exemple, la commande Unix ``ls -l`` affiche normalement le contenu du répertoire courant (en format long). Vous pouvez lancer ``ls`` avec ``os.popen``[cite: 1] :

.. code:: python

    >>> cmd = 'ls -l'
    >>> fp = os.popen(cmd)

L'argument est une chaîne qui contient une commande shell. La valeur de retour est un objet qui se comporte exactement comme un fichier ouvert. Vous pouvez lire la sortie du processus ``ls`` une ligne à la fois avec ``readline`` ou récupérer l'ensemble en une seule fois avec ``read``[cite: 1] :

.. code:: python

    >>> res = fp.read()

Lorsque vous avez terminé, vous fermez le pipe comme un fichier[cite: 1] :

.. code:: python

    >>> stat = fp.close()
    >>> print stat
    None

La valeur de retour est le statut final du processus ``ls`` ; ``None`` signifie qu'il s'est terminé normalement (sans erreurs)[cite: 1].

Par exemple, la plupart des systèmes Unix fournissent une commande appelée ``md5sum`` qui lit le contenu d'un fichier et calcule une « somme de contrôle » (*checksum*). Vous pouvez lire à propos de MD5 sur http://en.wikipedia.org/wiki/Md5. Cette commande fournit un moyen efficace de vérifier si deux fichiers ont le même contenu. La probabilité que des contenus différents produisent la même somme de contrôle est très faible (c'est-à-dire peu probable de se produire avant la fin de l'univers)[cite: 1].

Vous pouvez utiliser un pipe pour exécuter ``md5sum`` depuis Python et obtenir le résultat[cite: 1] :

.. code:: python

    >>> filename = 'book.tex'
    >>> cmd = 'md5sum ' + filename
    >>> fp = os.popen(cmd)
    >>> res = fp.read()
    >>> stat = fp.close()
    >>> print res
    1e0033f0ed0656636de0d75144ba32e0  book.tex
    >>> print stat
    None

.. topic:: Exercice

    Dans une large collection de fichiers MP3, il peut y avoir plus d'une copie de la même chanson, stockée dans des répertoires différents ou avec des noms de fichiers différents. Le but de cet exercice est de rechercher les doublons[cite: 1].
    Écrivez un programme qui recherche dans un répertoire et tous ses sous-répertoires, de manière récursive, et renvoie une liste de chemins complets pour tous les fichiers avec un suffixe donné (comme ``.mp3``)[cite: 1].
    *Indice :* ``os.path`` fournit plusieurs fonctions utiles pour manipuler les noms de fichiers et de chemins[cite: 1].
    Pour reconnaître les doublons, vous pouvez utiliser ``md5sum`` pour calculer une somme de contrôle pour chaque fichier. Si deux fichiers ont la même somme de contrôle, ils ont probablement le même contenu. Pour vérifier à deux reprises, vous pouvez utiliser la commande Unix ``diff``[cite: 1].
    Solution : http://thinkpython.com/code/find_duplicates.py[cite: 1].

Écriture de modules
-------------------

N'importe quel fichier qui contient du code Python peut être importé en tant que module. Par exemple, supposons que vous ayez un fichier nommé ``wc.py`` avec le code suivant[cite: 1] :

.. code:: python

    def linecount(filename):
        count = 0
        for line in open(filename):
            count += 1
        return count

    print linecount('wc.py')

Si vous exécutez ce programme, il se lit lui-même et affiche le nombre de lignes dans le fichier, qui est 7[cite: 1].

Vous pouvez également l'importer de cette façon[cite: 1] :

.. code:: python

    >>> import wc
    7

Vous disposez désormais d'un objet module ``wc``[cite: 1] :

.. code:: python

    >>> print wc
    <module 'wc' from 'wc.py'>

Qui fournit une fonction appelée ``linecount``[cite: 1] :

.. code:: python

    >>> wc.linecount('wc.py')
    7

C'est donc ainsi que l'on écrit des modules en Python[cite: 1].

Le seul problème avec cet exemple est que lorsque vous importez le module, il exécute le code de test en bas. Normalement, lorsque vous importez un module, il définit de nouvelles fonctions mais il ne les exécute pas[cite: 1].

Les programmes qui seront importés comme modules utilisent souvent l'idiome suivant[cite: 1] :

.. code:: python

    if __name__ == '__main__':
        print linecount('wc.py')

``__name__`` est une variable intégrée qui est définie au démarrage du programme. Si le programme s'exécute en tant que script, ``__name__`` a la valeur ``__main__`` ; dans ce cas, le code de test est exécuté. Sinon, si le module est en cours d'importation, le code de test est ignoré[cite: 1].

.. topic:: Exercice

    Tapez cet exemple dans un fichier nommé ``wc.py`` et exécutez-le en tant que script. Ensuite, lancez l'interpréteur Python et faites ``import wc``. Quelle est la valeur de ``__name__`` lorsque le module est en cours d'importation ?[cite: 1]
    *Avertissement :* Si vous importez un module qui a déjà été importé, Python ne fait rien. Il ne relit pas le fichier, même s'il a changé. Si vous souhaitez recharger un module, vous pouvez utiliser la fonction intégrée ``reload``, mais cela peut être délicat, donc la chose la plus sûre à faire est de redémarrer l'interpréteur puis d'importer à nouveau le module[cite: 1].

Débogage
--------

Lorsque vous lisez et écrivez des fichiers, vous pourriez rencontrer des problèmes avec les espaces blancs. Ces erreurs peuvent être difficiles à déboguer parce que les espaces, les tabulations et les retours à la ligne sont normalement invisibles[cite: 1] :

.. code:: python

    >>> s = '1 2\t 3\n 4'
    >>> print s
    1 2  3
     4

La fonction intégrée ``repr`` peut aider. Elle prend n'importe quel objet comme argument et renvoie une représentation sous forme de chaîne de l'objet. Pour les chaînes, elle représente les caractères d'espacement avec des séquences d'antislash[cite: 1] :

.. code:: python

    >>> print repr(s)
    '1 2\t 3\n 4'

Cela peut être utile pour le débogage[cite: 1].

Un autre problème que vous pourriez rencontrer est que différents systèmes utilisent des caractères différents pour indiquer la fin d'une ligne. Certains systèmes utilisent un saut de ligne, représenté par ``\n``. D'autres utilisent un caractère de retour, représenté par ``\r``. Certains utilisent les deux[cite: 1].

Si vous déplacez des fichiers entre différents systèmes, ces incohérences pourraient causer des problèmes. Pour la plupart des systèmes, il existe des applications pour convertir d'un format à un autre. Vous pouvez les trouver (et en lire plus sur ce problème) à l'adresse http://en.wikipedia.org/wiki/Newline. Ou, bien sûr, vous pourriez en écrire un vous-même[cite: 1].

Glossaire
---------

.. glossary::

    persistant
    persistent
        Relatif à un programme qui s'exécute indéfiniment et conserve au moins une partie de ses données dans un stockage permanent[cite: 1].

    opérateur de formatage
    format operator
        Un opérateur, ``%``, qui prend une chaîne de format et un tuple et génère une chaîne incluant les éléments du tuple formatés tel que spécifié par la chaîne de format[cite: 1].

    chaîne de format
    format string
        Une chaîne, utilisée avec l'opérateur de formatage, qui contient des séquences de format[cite: 1].

    séquence de format
    format sequence
        Une séquence de caractères dans une chaîne de format, comme ``%d``, qui spécifie comment une valeur doit être formatée[cite: 1].

    fichier texte
    text file
        Une séquence de caractères stockée dans un stockage permanent comme un disque dur[cite: 1].

    répertoire
    directory
        Une collection nommée de fichiers, également appelée dossier[cite: 1].

    chemin
    path
        Une chaîne qui identifie un fichier[cite: 1].

    chemin relatif
    relative path
        Un chemin qui part du répertoire courant[cite: 1].

    chemin absolu
    absolute path
        Un chemin qui part du répertoire le plus haut du système de fichiers[cite: 1].

    capturer
    catch
        Empêcher une exception de terminer un programme en utilisant les instructions ``try`` et ``except``[cite: 1].

    base de données
    database
        Un fichier dont le contenu est organisé comme un dictionnaire avec des clés qui correspondent à des valeurs[cite: 1].

Exercices
---------

.. topic:: Exercice

    Le module ``urllib`` fournit des méthodes pour manipuler les URL et télécharger des informations depuis le web. Le code suivant télécharge et affiche un message secret provenant de thinkpython.com[cite: 1] :

    .. code:: python

        import urllib

        conn = urllib.urlopen('http://thinkpython.com/secret.html')
        for line in conn:
            print line.strip()

    Exécutez ce code et suivez les instructions que vous y voyez[cite: 1].
    Solution : http://thinkpython.com/code/zip_code.py[cite: 1].
