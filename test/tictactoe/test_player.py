from __future__ import annotations

from intropy.tictactoe import tictactoe

x = X = "X"
o = O = "O"
_ = EMPTY = " "

expected =  {
    (
        (_, _, _),
        (_, _, _),
        (_, _, _),
    ): x,
    (
        (x, _, _),
        (_, _, _),
        (_, _, _),
    ): o,
}


def test_player_initial():
    initial_player = tictactoe.player(
        board=(
            (tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY),
            (tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY),
            (tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY),
        )
    )

    assert initial_player == tictactoe.X

def test_player():
    for board, expected_player in expected.items():
        assert tictactoe.player(board) == expected_player