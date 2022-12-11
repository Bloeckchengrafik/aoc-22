MOTION_VECTORS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}


class MotionList(list):
    def __init__(self, data: list[str]):
        super().__init__()

        for line in data:
            direction = line[0]
            distance = int(line[1:])

            for _ in range(distance):
                self.append(MOTION_VECTORS[direction])


def move_tail_with_rules(head: list[int], tail: list[int]) -> list[int]:
    """
    in fact, the head and tail must always be touching (diagonally adjacent and even overlapping both count as touching)

    If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step
    in that direction, so it remains close enough.

    Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one
    step diagonally to keep up
    """

    # If both are touching, do nothing
    # This is also the case if they are overlapping or diagonally adjacent
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    # Is the head in the same row or column as the tail?
    if head[0] == tail[0] or head[1] == tail[1]:
        if head[0] == tail[0] + 2:
            tail[0] += 1
        elif head[0] == tail[0] - 2:
            tail[0] -= 1
        elif head[1] == tail[1] + 2:
            tail[1] += 1
        elif head[1] == tail[1] - 2:
            tail[1] -= 1
    else:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1

    return tail
