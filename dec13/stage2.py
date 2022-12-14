from dec13 import compare, parse_input


def stage(data: list[str]):
    data = parse_input(data)
    flat_inputs = []
    flat_inputs.extend([[[2]], [[6]]])

    for i, [left, right] in enumerate(data):
        flat_inputs.append(left)
        flat_inputs.append(right)

    idx_1 = sum([1 for e in flat_inputs if compare(e, [[2]])]) + 1
    idx_2 = sum([1 for e in flat_inputs if compare(e, [[6]])]) + 1

    print(idx_1 * idx_2)
