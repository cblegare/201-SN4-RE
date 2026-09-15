Travail pratique: Tic tac toe
=============================

Dans ce travail pratique, vous devez implémenter une IA qui cherche le
meilleur prochain coup à jouer au Tic tac toe!


Bien commencer
--------------

*   Télécharger les sources (avec `git clone ...`)

*   Dans le dossier,

    ```shell
    cd projects/tictactoe
    ```

    exécutez la commande suivant pour installer toutes les dépendances:

    ```shell
    uv sync
    ```
    
*   Lancez le jeu avec

    ```shell
    uv run tictactoe
    ```

*   Exécutez les script de formattages et vérification avec

    ```shell
    uv run nox -t tictactoe
    ```


Présentation
------------

Il y a deux fichiers principaux dans ce projet : runner.py et game.py. 
Le fichier game.py contient toute la logique pour jouer la partie et 
pour déterminer les coups optimaux. 
Le fichier runner.py a déjà été implémenté pour vous et contient tout le 
code permettant d'exécuter l'interface graphique du jeu. 
Une fois que vous aurez complété toutes les fonctions requises dans game.py, 
vous devriez pouvoir exécuter python runner.py pour jouer contre votre IA !

Ouvrons game.py pour bien comprendre ce qui vous est fourni. 
En premier lieu, nous définissons trois variables : X, O et EMPTY, 
pour représenter les valeurs possibles sur le plateau.

La fonction initial_state retourne l'état de départ du plateau. 
Pour ce problème, nous avons choisi de représenter le plateau sous la 
forme d'une liste de trois listes (représentant les trois rangées du plateau), 
où chaque liste interne contient trois valeurs qui sont soit X, O ou EMPTY.

Ce qui suit correspond aux fonctions que nous vous laissons le soin 
d'implémenter !


Spécifications
--------------

La cohérence du formattage du code, la clareté du code, le choix de structures
de données et d'algorithmes optimaux et les principes des bonnes pratiques
de programmation (S.O.L.I.D., par exemple) sont évalués.

Le code qui échoue les vérifiations automatiques sera systématiquement
pénalisés. Pour exécuter les vérifications automatiques, lancez la commande

```shell
uv run nox -t tictactoe
```

Complétez l'implémentation de `player`, `actions`, `result`, `winner`,
`terminal`, `utility` et `minimax`.


### `player`

La fonction `player` prend en entrée un état du plateau et retourne le joueur
dont c'est le tour (`X` ou `O`).

*   Dans l'état initial du jeu, `X` joue le premier coup. Ensuite, le joueur
    alterne à chaque coup supplémentaire.

*   Si le plateau fourni est dans un état terminal (partie terminée), n'importe
    quelle valeur de retour est acceptable.


### `actions`

La fonction `actions` doit retourner un ensemble (`set`) de toutes les actions
possibles sur un plateau donné.

*   Chaque action doit être représentée sous la forme d'un tuple `(i, j)`
    où `i` correspond à la ligne du coup (`0`, `1` ou `2`) et `j` à la 
    cellule de cette ligne (`0`, `1` ou `2`).

*   Les coups possibles correspondent à toutes les cellules du plateau qui 
    ne contiennent pas déjà un `X` ou un `O`.


### `result`

La fonction `result` prend un plateau et une action en entrée, puis retourne
un nouvel état du plateau, sans modifier le plateau d'origine.

*   Si l'action n'est pas valide pour ce plateau, votre programme doit lever
    une exception.

*   Le plateau retourné doit correspondre au résultat obtenu en appliquant
    le coup du joueur actif à la cellule indiquée par l'action.

*   **Important :** Le plateau original ne doit pas être modifié. Comme Minimax
    évalue de nombreux états possibles lors de ses calculs, modifier directement
    une cellule du plateau fourni est incorrect. Vous devrez probablement faire
    une copie profonde (*deep copy*) du plateau avant d'y apporter des
    modifications.


### `winner`

La fonction `winner` accepte un plateau en entrée et retourne le gagnant de la
partie, s'il y en a un.

*   Si le joueur `X` a gagné, la fonction retourne `X`. Si le joueur `O` a
    gagné, elle retourne `O`.

*   Un joueur gagne en alignant trois de ses symboles horizontalement,
    verticalement ou en diagonale.

*   Vous pouvez supposer qu'il y aura au maximum un seul gagnant (aucun plateau
    ne contiendra deux alignements de trois symboles simultanés, ce qui serait un
    état invalide).

*   S'il n'y a pas de gagnant (partie en cours ou égalité), la fonction doit
    retourner `None`.


### `terminal`

La fonction `terminal` accepte un plateau en entrée et retourne un booléen
indiquant si la partie est terminée.

*   Si la partie est terminée, soit parce qu'un joueur a gagné, soit parce 
    que toutes les cellules sont remplies sans gagnant, la fonction retourne 
    `True`.

*   Sinon, si la partie est toujours en cours, elle retourne `False`.


### `utility`

La fonction `utility` accepte un plateau terminal en entrée et retourne son
utilité (son score).

*   Si `X` a gagné, l'utilité est `1`.

*   Si `O` a gagné, l'utilité est `-1`.

*   Si la partie s'est terminée par une égalité, l'utilité est `0`.


### `minimax`

La fonction `minimax` prend un plateau en entrée et retourne le coup optimal
pour le joueur dont c'est le tour.

*   Le coup retourné doit être l'action optimale `(i, j)` parmi les actions
    autorisées sur le plateau. Si plusieurs coups sont tout aussi optimaux,
    chacun d'eux est acceptable.

*   Si le plateau est terminal, la fonction `minimax` doit retourner `None`.


### Remarques

Pour toutes les fonctions acceptant un plateau en entrée, vous pouvez partir
du principe qu'il s'agit d'un plateau valide (une liste contenant trois 
lignes, chacune comportant trois valeurs : `X`, `O` ou `EMPTY`). 
Vous ne devez pas modifier les déclarations de fonctions fournies 
(l'ordre ou le nombre d'arguments).


Conseils
--------

*   Si vous souhaitez tester vos fonctions dans un autre fichier Python, 
    vous pouvez les importer avec : `from tictactoe.game import initial_state`.

    N'hésitez pas à utiliser le répertoire `test` pour ce faire! 

*   Vous êtes libre d'ajouter des fonctions auxiliaires (*helper functions*)
    dans `game.py`, à condition que leurs noms n'entrent pas en collision
    avec les noms de fonctions ou de variables déjà existants.

*   L'élagage alpha-bêta (*alpha-beta pruning*) est optionnel, mais il 
    permettra à votre IA de s'exécuter de manière beaucoup plus efficace !

*   Si vous utilisez *PyCharm*, une configuration de déboguage devrait être 
    fournie.