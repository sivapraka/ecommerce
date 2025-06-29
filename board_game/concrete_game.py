from board_game.board_game import BoardGame
from board_game.game_type import GameType


class TicTacToe(BoardGame):
    def game_type(self) -> GameType:
        return GameType.TIC_TAC_TOE

class Chess(BoardGame):
    def game_type(self) -> GameType:
        return GameType.CHESS

class SnakeAndLadder(BoardGame):
    def game_type(self) -> GameType:
        return GameType.SNAKE_LADDER