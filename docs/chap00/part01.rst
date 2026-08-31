====================
 Python, le langage
====================

Le langage de programmation que vous apprendrez est Python.

.. graphviz::

    digraph CPython_Architecture {
        // Disposition horizontale
        rankdir=LR;

        // Style par défaut des nœuds
        node [shape=box, style=filled, fillcolor="#f8f9fa", color="#343a40", fontname="Arial"];

        // Définition des nœuds
        Source [label="Code Source\n(.py)", fillcolor="#e3f2fd"];
        Parser [label="Analyseur\n(lexer & parser)"];
        AST [label="Arbre syntaxique\nabstrait (AST)"];
        Compiler [label="Compilateur"];
        Bytecode [label="Bytecode"];
        PVM [label="Machine Virtuelle\nPython", fillcolor="#fff3cd"];
        Output [label="Résultat\nExécuté", shape=oval, fillcolor="#d4edda"];

        // Connexions
        Source -> Parser [label=" Texte"];
        Parser -> AST [label=" Tokens"];
        AST -> Compiler;
        Compiler -> Bytecode;
        Bytecode -> PVM;
        PVM -> Output;
    }

Il y a deux façons d'utiliser le Interprète: mode interactif et mode script.
Dans mode interactif, vous tapez des programmes Python et l'interpréteur affiche
le résultat:

.. code-block:: python

    >>> 1 + 1
    2

Les chevrons, ``>>>``, sont l'**invite** de commande que l'interprèteur utilise
pour indiquer qu'il est prêt. Si vous tapez ``1 + 1``, Python répond 2.

Alternativement, vous pouvez stocker du code dans un fichier et utiliser
l'interpréteur pour exécuter le contenu du fichier, qui est appelé un
**script**. Par convention, les scripts Python ont des noms qui se terminent par
`.py`.

Pour exécuter le script, vous devez indiquer à l'interpréteur l'emplacement du
fichier. Si vous avez un script nommé ``monscript.py``, vous l'exécutez avec la
commande ``python monscript.py``.

Travailler en mode interactif est pratique pour tester de petits morceaux de
code car vous pouvez les taper et les exécuter immédiatement. Pour quoi que ce
soit de plus que quelques lignes, vous devriez enregistrer votre code en tant
que script pour que vous puissiez le modifier et l'exécuter plus tard.

------------------------------
 Langages naturels et formels
------------------------------

Les langues naturelles sont les langues que les gens parlent, comme l'anglais,
l'espagnol et le français. Ils n'ont pas été conçus par les gens (bien que les
gens essaient de leur imposer un ordre); Ils ont évolué naturellement.

Les langues formelles sont des langues conçues par des personnes pour
applications spécifiques. Par exemple, la notation que les mathématiciens
L'utilisation est un langage formel qui est particulièrement bon pour désigner
relations entre les nombres et les symboles. Les chimistes utilisent un formel
langage pour représenter la structure chimique des molécules. Et Le plus
important:
