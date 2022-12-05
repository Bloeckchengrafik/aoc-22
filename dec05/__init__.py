from rich.progress import track
from rich.console import Console
from rich import print

THINGS_OF_INTEREST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

console = Console()


class Stack:
    head = None

    def push(self, value):
        self.head = (value, self.head)

    def pop(self):
        value, self.head = self.head
        return value

    def multi_pop(self, n):
        # pop n items off the stack
        data = []
        for _ in range(n):
            data.append(self.pop())

        return data

    def multi_push(self, data):
        # push a list of data onto the stack
        for value in data:
            self.push(value)

    def data(self):
        # return a list of the data in the stack
        data = []
        old_head = self.head

        while self.head:
            value, self.head = self.head
            data.append(value)

        self.head = old_head

        return data


class CargoCrane:
    def __init__(self, data: list[str]):
        """
        :param data: something in the following format:
            [D]
        [N] [C]
        [Z] [M] [P]
         1   2   3

        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2

        This data should be parsed into the following:

        self.crates = [
            ["Z", "N"],
            ["M", "C", "D"],
            ["P"]
        ]

        and a list of moves:
        self.moves = [
            (1, 2, 1),
            (3, 1, 3),
            (2, 2, 1),
            (1, 1, 2)
        ]
        """
        self.crates = []
        self.moves = []

        # Parse the data into self.crates
        header_end = data.index("")

        # Get the max number of crates
        max_crates = len(data[header_end - 1].replace(" ", ""))

        for i in range(max_crates):
            self.crates.append(Stack())

        for line in track(list(reversed(data[:header_end - 1])), description="Parsing crates"):
            for j in range(max_crates):
                try:
                    char = line[1 + 4 * j]
                    if char in THINGS_OF_INTEREST:
                        self.crates[j].push(char)
                except IndexError:
                    pass

        # Parse the data into self.moves
        for line in track(data[header_end + 1:], description="Parsing moves "):
            # Data is present in format:
            # move 1 from 2 to 1
            # Relevant data is: 1, 2, 1
            data = line.split(" ")
            data.remove("move")
            data.remove("from")
            data.remove("to")
            self.moves.append(tuple(map(int, data)))

    def move_one_at_a_time(self, move: tuple[int, int, int]):
        mv_amt, mv_from, mv_to = move
        mv_from -= 1
        mv_to -= 1

        data_to_move = self.crates[mv_from].multi_pop(mv_amt)
        self.crates[mv_to].multi_push(data_to_move)

    def move_all(self, move: tuple[int, int, int]):
        mv_amt, mv_from, mv_to = move
        mv_from -= 1
        mv_to -= 1

        data_to_move = self.crates[mv_from].multi_pop(mv_amt)
        data_to_move.reverse()
        self.crates[mv_to].multi_push(data_to_move)

    def get_top_of_all(self) -> str:
        data = []
        for stack in self.crates:
            if stack.head:
                data.append(stack.pop())

        return "".join(data)
