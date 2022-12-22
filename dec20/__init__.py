from rich.progress import track


def mix(unchanged_file: list[tuple[int, int]], to_mix: list[tuple[int, int]]):
    output = to_mix.copy()

    for num in track(unchanged_file, description="Mixing"):
        out_index = output.index(num)
        output.remove(num)
        new_index = (out_index + num[1]) % len(output)
        if new_index < 0:
            new_index += len(output)
        output.insert(new_index, num)

    return output


def find_solution(data: list[tuple[int, int]]):
    zero_index = -1
    for i, num in enumerate(data):
        if num[1] == 0:
            zero_index = i
            break

    if zero_index == -1:
        raise ValueError("No zero index found.")
    data = [data[(zero_index + x) % len(data)][1] for x in [1000, 2000, 3000]]
    return sum(data)
