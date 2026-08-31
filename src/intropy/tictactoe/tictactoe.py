"""Tic Tac Toe Player."""

from __future__ import annotations


from typing import Literal

X = "X"
O = "O"
EMPTY = " "
_ = " "

Mark = Literal["X", "O", " "]
Player = Literal["X", "O", " "]
I = Literal[0, 1, 2]
J = Literal[0, 1, 2]
Board = tuple[tuple[Mark, Mark, Mark], tuple[Mark, Mark, Mark], tuple[Mark, Mark, Mark]]
Action = tuple[I, J]


def initial_state() -> Board:
    """Returns starting state of the board."""
    return ((_, _, _), (_, _, _), (_, _, _))


def player(board: Board) -> Player:
    """Returns player who has the next turn on a board."""

    x = 0
    o = 0

    for line in board:
        for mark in line:
            if mark == X:
                x += 1
            elif mark == O:
                o += 1

    return X if x <= o else O


def actions(board: Board) -> list[Action]:
    """Returns set of all possible actions (i, j) available on the board."""
    


def result(board: Board, action: Action) -> Board:
    """Returns the board that results from making move (i, j) on the board."""
    raise NotImplementedError


def winner(board: Board) -> Player:
    """Returns the winner of the game, if there is one."""
    raise NotImplementedError


def terminal(board: Board) -> bool:
    """Returns True if game is over, False otherwise."""
    raise NotImplementedError


def utility(board: Board):
    """Returns 1 if X has won the game, -1 if O has won, 0 otherwise."""
    raise NotImplementedError


def minimax(board: Board):
    """Returns the optimal action for the current player on the board."""
    raise NotImplementedError
