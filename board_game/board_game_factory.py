from board_game.concrete_game import BoardGame
from .game_type import GameType


class BoardGameFactory:
    @staticmethod
    def create_game(game_type: GameType) -> BoardGame:
        return BoardGame(game_type.name)

