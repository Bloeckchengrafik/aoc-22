from rich import print


class Tetris:
    PIECES = [
        [
            [1, 1, 1, 1],
        ],
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
        ],
        [
            [1],
            [1],
            [1],
            [1],
        ],
        [
            [1, 1],
            [1, 1],
        ],
    ]

    def __init__(self, jet_pattern: list[str]):
        self.board = [[0] * 7 for _ in range(20000)]
        self.current_piece = 0
        self.jet_pattern = jet_pattern
        self.current_jet_position = 0
        self.pat_idx = 0

    def get_height(self) -> int:
        n = 0
        for i, row in enumerate(self.board):
            if any(row):
                n = i + 1
        return n

    def check_movement_allowed(self, piece: list[list[int]], x: int, y: int) -> bool:
        # Check wall collisions
        if x < 0 or x + len(piece[0]) > len(self.board[0]):
            return False

        # Check floor collisions
        if y < 0 or y + len(piece) > len(self.board):
            return False

        # Check block collisions
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell and self.board[y + i][x + j]:
                    return False
        return True

    def step(self):
        # Create a new piece
        piece = self.PIECES[self.current_piece]
        self.current_piece = (self.current_piece + 1) % len(self.PIECES)
        bottom_left = [self.get_height() + 3, 2]

        while True:
            should_stop = False

            if self.jet_pattern[self.current_jet_position] == ">":
                if self.check_movement_allowed(piece, bottom_left[1] + 1, bottom_left[0]):
                    bottom_left[1] += 1
            elif self.jet_pattern[self.current_jet_position] == "<":
                if self.check_movement_allowed(piece, bottom_left[1] - 1, bottom_left[0]):
                    bottom_left[1] -= 1
            self.pat_idx += 1

            self.current_jet_position = (self.current_jet_position + 1) % len(self.jet_pattern)

            if self.check_movement_allowed(piece, bottom_left[1], bottom_left[0] - 1):
                bottom_left[0] -= 1
            else:
                should_stop = True

            if should_stop:
                break

        # Persist the piece
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell:
                    self.board[bottom_left[0] + i][bottom_left[1] + j] = cell

    def visualize(self, piece, bottom_left):
        boardcopy = [row.copy() for row in self.board]
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                boardcopy[bottom_left[0] + i][bottom_left[1] + j] = cell
        print(self.__repr__(boardcopy))

    def __repr__(self, board: list[list[int]] = None) -> str:
        if board is None:
            board = self.board

        final = f"({2000 - self.get_height() - 10} more)\n"
        for i, row in enumerate(reversed(board[:self.get_height() + 10])):
            final += f"{(self.get_height() + 9)-i:3} " + " ".join("#" if cell else "·" for cell in row) + "\n"

        return final
