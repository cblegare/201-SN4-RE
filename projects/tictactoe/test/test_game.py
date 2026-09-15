from __future__ import annotations

from tictactoe.game import EMPTY, initial_state


def test_initial_state() -> None:
    assert initial_state() == (
        (EMPTY, EMPTY, EMPTY),
        (EMPTY, EMPTY, EMPTY),
        (EMPTY, EMPTY, EMPTY),
    )
