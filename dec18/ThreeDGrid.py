class ThreeDGrid:
    def __init__(self):
        self.grid = [[['.' for _ in range(100)] for _ in range(100)] for _ in range(100)]

    def set(self, x, y, z, val):
        self.grid[x][y][z] = val

    def get(self, x, y, z):
        return self.grid[x][y][z]

    def count_open_faces(self, x, y, z, requirement, air='.'):
        count = 0
        if self.grid[x][y][z] == requirement:
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                # Check if the face is outside the grid
                if x + dx < 0 or x + dx >= 100 or y + dy < 0 or y + dy >= 100 or z + dz < 0 or z + dz >= 100:
                    count += 1
                elif self.grid[x + dx][y + dy][z + dz] == air:
                    count += 1

        return count
