import abc
import random


class Player(abc.ABC):

    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):

    def __init__(self):
        super().__init__()
        # 1 unit up, down, left, right
        self.moves = [
            (0, 1),   # Up
            (0, -1),  # Down
            (-1, 0),  # Left
            (1, 0),   # Right
        ]

    def level_up(self):
        # Adds the 4 diagonal movements
        diagonal_moves = [
            (1, 1),    # Up-Right
            (-1, 1),   # Up-Left
            (1, -1),   # Down-Right
            (-1, -1),  # Down-Left
        ]
        self.moves.extend(diagonal_moves)