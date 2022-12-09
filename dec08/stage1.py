from dec08.forest import Forest
from rich import table, print


def stage(data: list[str]):
    forest = Forest(data)

    # Go through the forest and find all trees that are visible from the outside
    # by checking all rows and columns for trees that are not blocked by other trees

    def recalculate_row(current_row: list[list[int, bool]]) -> list[list[int, bool]]:
        # All trees are visible from the outside
        current_row[0][1] = True
        current_row[-1][1] = True

        # Recalculate the row or column to mark all trees that are not visible from the outside

        current_max = -1
        for element in current_row:
            if element[0] > current_max:
                element[1] = True
                current_max = element[0]

        return current_row

    for row in range(forest.rows()):
        forest.matrix[row] = recalculate_row(forest.get_row(row))
        # Recalculate in reverse order to check all visibilities on the right side
        forest.matrix[row] = recalculate_row(forest.get_row(row)[::-1])[::-1]

    for col in range(forest.columns()):
        forest.set_column(col, recalculate_row(forest.get_column(col)))
        # Recalculate in reverse order to check all visibilities on the bottom side
        forest.set_column(col, recalculate_row(forest.get_column(col)[::-1])[::-1])


    # Count the number of trees that are visible from the outside
    visible = 0
    for row in range(forest.rows()):
        for column in range(forest.columns()):
            if forest.get_row(row)[column][1]:
                visible += 1
    print(f"Number of trees visible from the outside: {visible}")
