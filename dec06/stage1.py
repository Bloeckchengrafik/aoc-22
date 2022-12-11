from rich.progress import track
from rich import print


def stage(data: list[str]):
    data: str = data[0]
    solution: int = 0

    for i, _ in track(enumerate(data[4:])):
        list_of_fours = data[i-4:i]

        if len(list_of_fours.strip().replace("\n", "")) == 0:
            continue

        # Check if all are different
        if len(set(list_of_fours)) == 4:
            solution = i
            break
    print(f"Packet Marker: {solution}")
