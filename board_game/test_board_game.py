import inspect
from unittest import TestCase

from board_game.board_game import BoardGame
from board_game.board_game_factory import BoardGameFactory
from board_game.game_type import GameType


class TestBoardGameFactory(TestCase):

    def test_board_game(self):

        subclasses = BoardGame.__subclasses__()
        self.assertTrue(len(subclasses) == 3)

        attrs = dir(BoardGame)

        self.assertIn("get_game_name", attrs, "BoardGame much have method get_game_name")
        self.assertIn("play_game", attrs, "BoardGame much have method play_game")

    def test_board_game_factory(self):
        attrs = dir(BoardGameFactory)
        self.assertIn("create_game", attrs, "BoardGame much have method create_game")

        create_game = BoardGameFactory.create_game

        param_list = list(inspect.signature(create_game).parameters.keys())
        self.assertIn("game_type", param_list, "create_game must have a game_type parameter")

        game = BoardGameFactory.create_game(
            game_type=GameType.CHESS
        )

        self.assertIsInstance(game, BoardGame)

