from __future__ import annotations

import importlib.resources
import logging.config
import sys
import time
from pathlib import Path

import click
import pygame

import tictactoe
import tictactoe.game
from tictactoe.log import logging_configuration

log = logging.getLogger(__name__)


WIDTH, HEIGHT = 600, 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TILE_SIZE = 80


class TicTacToeApp:
    """Gère l'interface graphique et la boucle principale du jeu."""

    def __init__(self) -> None:
        log.info("Initialisation de PyGame")
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        font_file = importlib.resources.files("tictactoe").joinpath(
            "data/OpenSans-Regular.ttf"
        )

        self.medium_font = pygame.font.Font(font_file, 28)
        self.large_font = pygame.font.Font(font_file, 40)
        self.move_font = pygame.font.Font(font_file, 60)

        self.user: str | None = None
        self.board = tictactoe.game.initial_state()
        self.ai_turn = False
        self.tiles: list[list[pygame.Rect]] = []

    def run(self) -> None:
        """Boucle principale du jeu."""
        while True:
            self.handle_events()
            self.update_ai_state()
            self.draw_screen()
            pygame.display.flip()

    def handle_events(self) -> None:
        """Traite les événements pygame et les clics de souris."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log.info("Événement QUIT reçu")
                sys.exit()

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse_pos = pygame.mouse.get_pos()
            log.info("Clic reçu!")
            if self.user is None:
                log.info("Joueur n'Est pas sélectionné, gestion du menu déclenchée")
                self.handle_menu_click(mouse_pos)
            else:
                log.info("Joueur sélectionné, gestion du jeu déclenchée")
                self.handle_game_click(mouse_pos)

    def handle_menu_click(self, mouse_pos: tuple[int, int]) -> None:
        """Gère le choix du joueur (X ou O) dans le menu."""
        btn_x, btn_o = self.get_menu_buttons()

        if btn_x.collidepoint(mouse_pos):
            time.sleep(0.2)
            log.info("Sélection du joueur X")
            self.user = tictactoe.game.X
        elif btn_o.collidepoint(mouse_pos):
            time.sleep(0.2)
            log.info("Sélection du joueur O")
            self.user = tictactoe.game.O

    def handle_game_click(self, mouse_pos: tuple[int, int]) -> None:
        """Gère les clics pendant la partie (jeu ou rejouer)."""
        log.info("Gestion d'un clic dans le jeu")

        if tictactoe.game.terminal(self.board):
            log.info("Jeu terminé!")
            btn_replay = self.get_replay_button()
            if btn_replay.collidepoint(mouse_pos):
                time.sleep(0.2)
                self.reset_game()
            return

        player = tictactoe.game.player(self.board)
        if self.user == player:
            log.info("Au tour de l'humain!")
            self.process_player_move(mouse_pos)

    def process_player_move(self, mouse_pos: tuple[int, int]) -> None:
        """Vérifie si le clic correspond à une case valide et applique le coup."""
        if not self.tiles:
            return

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == tictactoe.game.EMPTY and self.tiles[i][
                    j
                ].collidepoint(mouse_pos):
                    self.board = tictactoe.game.result(self.board, (i, j))
                    return

    def update_ai_state(self) -> None:
        """Gère le tour de l'intelligence artificielle."""
        if self.user is None or tictactoe.game.terminal(self.board):
            return

        player = tictactoe.game.player(self.board)
        if self.user != player:
            log.info("Au tour de l'IA!")
            if self.ai_turn:
                time.sleep(0.5)
                move = tictactoe.game.minimax(self.board)
                self.board = tictactoe.game.result(self.board, move)
                self.ai_turn = False
            else:
                self.ai_turn = True

    def reset_game(self) -> None:
        """Réinitialise l'état pour une nouvelle partie."""
        self.user = None
        self.board = tictactoe.game.initial_state()
        self.ai_turn = False

    def draw_screen(self) -> None:
        """Point d'entrée pour dessiner l'écran courant."""
        self.screen.fill(BLACK)
        if self.user is None:
            self.draw_menu()
        else:
            self.draw_game_board()
            self.draw_status_text()
            if tictactoe.game.terminal(self.board):
                self.draw_replay_button()

    def draw_menu(self) -> None:
        """Dessine le menu de sélection de joueur."""
        self.draw_text("Play Tic-Tac-Toe", self.large_font, WHITE, (WIDTH / 2, 50))

        btn_x, btn_o = self.get_menu_buttons()

        pygame.draw.rect(self.screen, WHITE, btn_x)
        self.draw_text("Play as X", self.medium_font, BLACK, btn_x.center)

        pygame.draw.rect(self.screen, WHITE, btn_o)
        self.draw_text("Play as O", self.medium_font, BLACK, btn_o.center)

    def draw_game_board(self) -> None:
        """Dessine la grille de jeu et les coups joués."""
        self.tiles = []
        origin_x = WIDTH / 2 - (1.5 * TILE_SIZE)
        origin_y = HEIGHT / 2 - (1.5 * TILE_SIZE)

        for i in range(3):
            row_rects = []
            for j in range(3):
                rect = pygame.Rect(
                    origin_x + j * TILE_SIZE,
                    origin_y + i * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE,
                )
                pygame.draw.rect(self.screen, WHITE, rect, 3)

                # Dessiner le X ou le O
                if self.board[i][j] != tictactoe.game.EMPTY:
                    self.draw_text(self.board[i][j], self.move_font, WHITE, rect.center)

                row_rects.append(rect)
            self.tiles.append(row_rects)

    def draw_status_text(self) -> None:
        """Affiche le statut de la partie (Tour du joueur, victoire, etc.)."""
        if tictactoe.game.terminal(self.board):
            winner = tictactoe.game.winner(self.board)
            text = f"Game Over: {winner} wins." if winner else "Game Over: Tie."
        else:
            player = tictactoe.game.player(self.board)
            text = (
                f"Play as {self.user}"
                if self.user == player
                else "Computer thinking..."
            )

        self.draw_text(text, self.large_font, WHITE, (WIDTH / 2, 30))

    def draw_replay_button(self) -> None:
        """Affiche le bouton pour relancer une partie."""
        btn = self.get_replay_button()
        pygame.draw.rect(self.screen, WHITE, btn)
        self.draw_text("Play Again", self.medium_font, BLACK, btn.center)

    def draw_text(
        self,
        text: str,
        font: pygame.font.Font,
        color: tuple[int, int, int],
        center: tuple[float, float],
    ) -> None:
        """Utilitaire DRY pour dessiner du texte centré."""
        surface = font.render(text, True, color)  # noqa: FBT003 # Ok de hardcoder un bool ici
        rect = surface.get_rect(center=center)
        self.screen.blit(surface, rect)

    def get_menu_buttons(self) -> tuple[pygame.Rect, pygame.Rect]:
        """Retourne les coordonnées des boutons du menu."""
        btn_x = pygame.Rect((WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
        btn_o = pygame.Rect(5 * (WIDTH / 8), (HEIGHT / 2), WIDTH / 4, 50)
        return btn_x, btn_o

    def get_replay_button(self) -> pygame.Rect:
        """Retourne les coordonnées du bouton de fin de jeu."""
        return pygame.Rect(WIDTH / 3, HEIGHT - 65, WIDTH / 3, 50)


@click.command()
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Increase log level. '-v' will output INFO messages. "
    "More than -vv is useless.",
)
@click.option(
    "-q",
    "--quiet",
    count=True,
    help="Reduce log level. '-q' will suppress WARNING messages. "
    "More than -qq is useless.",
)
@click.option(
    "-l",
    "--log-file",
    help="Reduce log level. '-q' will suppress WARNING messages. "
    "More than -qq is useless.",
)
def main(verbose: int, quiet: int, log_file: str) -> None:
    """Point d'entrée de l'application."""
    verbosity: int = int(logging.INFO / 10) + verbose - quiet

    logging.config.dictConfig(
        logging_configuration(verbosity, Path(log_file) if log_file else None)
    )

    log.debug(verbosity)

    app = TicTacToeApp()
    app.run()
