from rich.progress import track
from rich.console import Console

from dec03 import get_priority
from lib import GREEN_OK

console = Console()


def stage(data: list[str]):
    new_data = []

    for line in track(data, "Splitting  "):
        # Split the line into two halves, split at the center
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]
        new_data.append([left, right])

    score = 0

    for line in track(new_data, "Calculating"):
        # Find the elements that are present in both lists
        # and add them to a new list
        new_list = []
        for element in line[0]:
            if element in line[1]:
                if element in new_list:
                    continue

                new_list.append(element)

        # If the new list is empty, skip to the next line
        if not new_list:
            continue

        for item in new_list:
            score += get_priority(item)

    console.log(f"{GREEN_OK} Score: {score}")
