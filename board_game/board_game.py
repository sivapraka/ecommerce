from abc import ABC


class BoardGame(ABC):
    def __init__(self, name: str):
        self.name = name

    def get_game_name(self) -> str:
        return self.name

    def play_game(self):
        print(f"Playing {self.name}... Let's go!")


