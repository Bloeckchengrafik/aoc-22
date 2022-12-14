class CaveScan:
    """
    This is a cave scan. It is represenented by a two-dimensional array of characters.
    The array has the dimensions of 1000 x 512.
    The array is filled with the following characters:
    - ' ' (space) - empty space
    - '#' - wall
    - '+' - sand
    - 'o' - sand that is at rest
    """

    def __init__(self, data: list[str]):
        self.scan = [['.' for _ in range(1000)] for _ in range(512)]

        self.lowest_y = 0

        # The data is formatted as follows:
        # x1,y1 -> x2,y2 -> x3,y3 -> ... -> xn,yn
        # where x1,y1 is the starting point, and x2,y2 is the ending point.
        # The scan is filled with walls between the starting and ending points.
        for line in data:
            linedata = line.split(' -> ')
            start = linedata[0].split(',')
            end_num = 1
            while end_num < len(linedata):
                end = linedata[end_num].split(',')
                self.fill_wall(start, end)
                start = end
                if int(end[1]) > self.lowest_y:
                    self.lowest_y = int(end[1])
                end_num += 1

        # Sand starts dropping from point 500,0
        self.scan[0][500] = '+'

    def __repr__(self):
        return '\n'.join(' '.join(row[450:520]) for row in self.scan[:50])

    def fill_wall(self, start: list[int], end: list[int]):
        """
        Fills the scan with walls between the starting and ending points.
        """
        start_x = int(start[0])
        start_y = int(start[1])
        end_x = int(end[0])
        end_y = int(end[1])
        if start_x == end_x:
            if start_y < end_y:
                for y in range(start_y, end_y + 1):
                    self.scan[y][start_x] = '#'
            else:
                for y in range(end_y, start_y + 1):
                    self.scan[y][start_x] = '#'
        elif start_y == end_y:
            if start_x > end_x:
                start_x, end_x = end_x, start_x
            for x in range(start_x, end_x + 1):
                self.scan[start_y][x] = '#'

    def step(self):
        """
        Drops one unit of sand
        """

        sand_position = [500, 0]

        did_move = True
        while did_move:
            # Check if below is out of bounds
            if sand_position[1] + 1 >= len(self.scan):
                return False
            # Check if sand can move down
            # Mark the position to be checked as the current position in the scan as a "*"
            if self.scan[sand_position[1] + 1][sand_position[0]] == '.':
                sand_position[1] += 1
                continue

            # Check if sand can move left diagonally
            if self.scan[sand_position[1] + 1][sand_position[0] - 1] == '.':
                sand_position[0] -= 1
                sand_position[1] += 1
                continue

            # Check if sand can move right diagonally
            if self.scan[sand_position[1] + 1][sand_position[0] + 1] == '.':
                sand_position[0] += 1
                sand_position[1] += 1
                continue

            did_move = False

        self.scan[sand_position[1]][sand_position[0]] = 'o'

        # If the sand is at the spawn point, throw an exception
        if sand_position[0] == 500 and sand_position[1] == 0:
            raise RuntimeError("Sand is at spawn point")

        return True

    def add_floor(self):
        """
        Adds a floor two blocks below the lowest wall.
        """
        for x in range(1000):
            self.scan[self.lowest_y + 2][x] = '#'
