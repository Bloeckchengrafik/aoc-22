from rich.progress import track

from dec08.forest import Forest


def stage(data: list[str]):
    forest = Forest(data)

    def get_scenic_score(x, y) -> int:
        """
        To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you
        reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a
        tree is right on the edge, at least one of its viewing distances will be zero.)
        This will be done for the tree at position (x, y)

        Finally, all the viewing distances are multiplied together to get the scenic score for the tree at position (x, y).
        """

        current_height = forest.get_row(y)[x][0]

        def lateral_score(vector):
            """
            Calculate the scenic score in one direction
            :param vector: The direction to calculate the score in
            :return: The scenic score in the given direction
            """
            current_position = (x, y)

            # Traverse the forest in the given direction until we reach the edge or a tree that is the same height
            # or taller than the tree under consideration
            score = 0
            while True:
                current_position = (current_position[0] + vector[0], current_position[1] + vector[1])

                # Check if we are out of bounds
                if current_position[0] < 0 or current_position[0] >= forest.columns() or current_position[1] < 0 or \
                        current_position[1] >= forest.rows():
                    break

                # Check if we found a tree that is the same height or taller than the tree under consideration
                if forest.get_row(current_position[1])[current_position[0]][0] >= current_height:
                    score += 1
                    break

                score += 1

            return score

        # Get the score for all 4 directions
        score = 1
        score *= lateral_score([1, 0])
        score *= lateral_score([-1, 0])
        score *= lateral_score([0, 1])
        score *= lateral_score([0, -1])

        return score

    # Calculate the scenic score for all trees and get the maximum
    max_score = 0
    for y in track(range(forest.rows()), "Calculating scenic scores"):
        for x in range(forest.columns()):
            score = get_scenic_score(x, y)
            if score > max_score:
                max_score = score

    print(f"Max score: {max_score}")
