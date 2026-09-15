"""Joueur de Tic-Tac-Toe."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Final, Literal

if TYPE_CHECKING:
    from collections.abc import Callable

I = Literal[0, 1, 2]  # noqa: E741 # Pas ambigu dans cette situation
J = Literal[0, 1, 2]

Mark = Literal["X", "O", " "]
Player = Literal["X", "O"]

Action = tuple[I, J]

Board = tuple[
    tuple[Mark, Mark, Mark],
    tuple[Mark, Mark, Mark],
    tuple[Mark, Mark, Mark],
]


X: Final[Mark] = "X"
O: Final[Mark] = "O"  # noqa: E741 # Pas ambigu dans cette situation
_: Final[Mark] = " "
EMPTY: Final[Mark] = " "


MAX_DEPTH = 1000000

log = logging.getLogger(__name__)


def log_board(log_fun: Callable[..., None], board: Board) -> None:
    """
    Affiche l'état du plateau dans les journaux d'événements.

    Args:
        log_fun: Fonction de journalisation à utiliser (ex: log.debug).
        board: Le plateau de jeu sous forme de n-uplet de n-uplets.

    """
    log_fun("Board: ")
    for row in board:
        log_fun("  > %s", row)


def initial_state() -> Board:
    """
    Retourne l'état initial du plateau de jeu.

    Returns:
        Un plateau de jeu vide sous forme de n-uplet 3x3.

    """
    # fmt: off
    board = (
        (_, _, _),
        (_, _, _),
        (_, _, _),
    )
    # fmt: on

    log.debug("Création d'un plateau de jeu neuf")
    log_board(log.debug, board)
    return board


def player(board: Board) -> Player:
    """
    Détermine le joueur dont c'est le tour sur le plateau donné.

    Args:
        board: L'état actuel du plateau de jeu.

    Returns:
        Le joueur actif ("X" ou "O").

    """
    raise NotImplementedError


def actions(board: Board) -> list[Action]:
    """
    Retourne l'ensemble des actions (i, j) disponibles sur le plateau.

    Args:
        board: L'état actuel du plateau de jeu.

    Returns:
        Une liste de tuples (i, j) représentant les cases vides.

    """
    raise NotImplementedError


def result(board: Board, action: Action) -> Board:
    """
    Retourne le nouveau plateau résultant de l'exécution d'une action.

    Args:
        board: L'état actuel du plateau de jeu.
        action: Le coup à jouer sous la forme d'un tuple (i, j).

    Returns:
        Un nouveau plateau mis à jour sans modifier l'original.

    """
    raise NotImplementedError


def winner(board: Board) -> Player | None:
    """
    Identifie le gagnant de la partie, s'il y en a un.

    Args:
        board: L'état actuel du plateau de jeu.

    Returns:
        Le symbole du gagnant ("X" ou "O"), ou None s'il n'y a pas de gagnant.

    """
    raise NotImplementedError


def terminal(board: Board) -> bool:
    """
    Indique si la partie est terminée.

    Args:
        board: L'état actuel du plateau de jeu.

    Returns:
        True si la partie est terminée (victoire ou égalité), False sinon.

    """
    raise NotImplementedError


def utility(board: Board) -> int:
    """
    Calcule l'utilité (le score) d'un plateau terminal.

    Args:
        board: L'état actuel du plateau de jeu terminal.

    Returns:
        1 si X a gagné, -1 si O a gagné, 0 en cas d'égalité.

    """
    raise NotImplementedError


def minimax(board: Board) -> Action | None:
    """
    Calcule le coup optimal pour le joueur actif sur le plateau.

    Args:
        board: L'état actuel du plateau de jeu.

    Returns:
        L'action optimale (i, j) à exécuter.

    """
    raise NotImplementedError
