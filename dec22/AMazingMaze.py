def str_rep_of_num(num: int) -> str:
    if num == 0:
        return ' '
    elif num == 1:
        return '.'
    elif num == 2:
        return '#'


def direction_to_str(direction: int) -> str:
    if direction == (0, 1):
        return '^'
    elif direction == (0, -1):
        return 'v'
    elif direction == (1, 0):
        return '>'
    elif direction == (-1, 0):
        return '<'


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


class AMazingMaze:
    def __init__(self, data):
        self.instructions = data[-1]
        self.data = data[:-1]
        self.grid = [[0 for _ in range(max([len(x) for x in data]))] for _ in range(len(data))]
        self.parse()
        self.x = self.grid[0].index(1)
        self.y = 0
        self.direction = (1, 0)

    def parse(self):
        for y, row in enumerate(self.data):
            for x, char in enumerate(row):
                if char == '.':
                    self.grid[y][x] = 1
                elif char == '#':
                    self.grid[y][x] = 2

    def __repr__(self):
        out = ""
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if x == self.x and y == self.y:
                    out += direction_to_str(self.direction)
                else:
                    out += str_rep_of_num(char)
                out += ' '
            out += "\n"
        return out

    def move_forward(self):
        tx = self.x + self.direction[0]
        ty = self.y + self.direction[1]

        if self.grid[ty][tx] == 0:
            # Wrap around to the other side of the maze
            if self.direction == DIRECTIONS[0]:
                tx = 0
            elif self.direction == DIRECTIONS[1]:
                ty = 0
            elif self.direction == DIRECTIONS[2]:
                tx = len(self.grid[0]) - 1
            elif self.direction == DIRECTIONS[3]:
                ty = len(self.grid) - 1

            while self.grid[ty][tx] == 0:
                tx += self.direction[0]
                ty += self.direction[1]

            if self.grid[ty][tx] == 2:
                return False

        if self.grid[ty][tx] == 2:
            return False

        self.x = tx
        self.y = ty

    def move_forward_cube(self):
        tx = self.x + self.direction[0]
        ty = self.y + self.direction[1]

        if self.grid[ty][tx] == 0:
            if tx == 49 and ty < 50:
                tx = 0
                ty = 50 - ty
                ty += 100
            elif ty == -1 and 50 <= tx < 100:
                tmp = tx - 50
                tx = 0
                ty = 150 + tmp
            elif ty == -1 and 100 <= tx < 150:
                tx = tx - 100
                ty = 199
            elif ty < 50 and tx == 150:
                ty = 50 - ty
                ty += 100
                tx -= 51
            elif ty == 50 and tx > 100:
                ty = 50 + (tx - 100)
                tx = 99
            elif tx == 100 and 50 <= ty < 100:
                tx = 100 + (ty - 50)
                ty = 49
            elif tx == 100 and 100 <= ty < 150:
                ty -= 100
                ty = 50 - ty
                tx = 149
            elif ty == 150 and tx >= 50:
                tmp = tx - 50
                tx = 49
                ty = 150 + tmp
            elif tx == 50 and ty >= 150:
                ty -= 200
                tx = ty + 50
                ty = 149
            elif ty == 200:
                ty = 0
                tx += 100
            elif tx == -1 and ty >= 150:
                ty -= 150
                tx = ty + 50
                ty = 0
            elif tx == -1 and ty < 150:
                ty -= 100
                ty = 50 - ty
                tx = 50
            elif ty == 99:
                ty = tx + 50
                tx = 50
            elif tx == 49:
                tx = ty - 50
                ty = 100
            else:
                raise ValueError()

            if self.grid[ty][tx] == 2:
                return False

        if self.grid[ty][tx] == 2:
            return False

        self.x = tx
        self.y = ty

    def turn(self, direction):
        if direction == 'L':
            self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) - 1) % len(DIRECTIONS)]
        elif direction == 'R':
            self.direction = DIRECTIONS[(DIRECTIONS.index(self.direction) + 1) % len(DIRECTIONS)]
