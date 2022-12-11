from rich import table, print


class Forest:
    def __init__(self, matrix: list[str]):
        """
        Create a forest from a matrix of strings
        :param matrix:
        Format:
        123
        456

        What it means:
        [
            [1, 2, 3],
            [4, 5, 6]
        ]
        """

        # Convert the matrix to a matrix of integers
        self.matrix = [[int(x) for x in row] for row in matrix]

        # Convert the matrix to a matrix of tuples
        # The first value is the value of the tree
        # The second value is a boolean that indicates if the tree is visible from the outside
        self.matrix = [[[x, False] for x in row] for row in self.matrix]

    def get_row(self, row: int):
        return self.matrix[row]

    def get_column(self, column: int):
        return [row[column] for row in self.matrix]

    def set_column(self, column: int, values: list[list[int, bool]]):
        for i, row in enumerate(self.matrix):
            row[column] = values[i]

    def rows(self):
        return len(self.matrix)

    def columns(self):
        return len(self.matrix[0])

    def table(self):
        # Create a table to display the forest
        t = table.Table()
        t.add_column("Row")
        for i in range(len(self.matrix[0])):
            t.add_column(str(i))
        for i, row in enumerate(self.matrix):
            t.add_row(str(i), *[f"{'#' if x[1] else '.' } {x[0]}" for x in row])
        print(t)
