from dec13 import parse_input, compare
from rich import print


def stage(data: list[str]):
    data = parse_input(data)

    indices = []

    for i, [left, right] in enumerate(data):
        valid_order = compare(left, right)
        if valid_order:
            indices.append(i + 1)

    print(sum(indices))
