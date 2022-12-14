def parse_input(data: list[str]):
    final = []
    current_pair = []

    for line in data:
        if line == "":
            final.append(current_pair)
            current_pair = []
        else:
            line_as_data = eval(line)
            current_pair.append(line_as_data)

    if current_pair:
        final.append(current_pair)

    return final


def flatten(list_data):
    if not list_data:
        return list_data
    if isinstance(list_data[0], list):
        return flatten(list_data[0]) + flatten(list_data[1:])
    return list_data[:1] + flatten(list_data[1:])


def compare(left, right):
    if type(left) is int and type(right) is int:
        if left == right:
            return None
        return left <= right

    if type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            l = left[i]
            r = right[i]

            is_right_order = compare(l, r)

            if is_right_order is not None:
                return is_right_order

        if len(left) != len(right):
            return len(left) < len(right)

        return None

    if type(left) is list:
        return compare(left, [right])

    return compare([left], right)
