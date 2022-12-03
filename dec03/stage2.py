from rich.progress import track
from rich.console import Console

from dec03 import get_priority
from lib import GREEN_OK

console = Console()


def stage(data: list[str]):
    # Split the data into triples
    triples = []
    current = []
    num = 0
    for line in track(data, "Splitting  "):
        current.append(line)
        num += 1
        if num == 3:
            triples.append(current)
            current = []
            num = 0

    console.log(f"{GREEN_OK} Split into {len(triples)} triples")

    commons = []

    for lists in track(triples, "Calculating"):
        # Find the elements that are present in all three lists
        # and add them to a new list
        new_list = []
        for element in lists[0]:
            if element in lists[1] and element in lists[2]:
                if element in new_list:
                    continue

                new_list.append(element)

        commons.append(new_list)

    console.log(f"{GREEN_OK} Found {len(commons)} common elements")

    score = 0

    for common in track(commons, "Scoring    "):
        for item in common:
            score += get_priority(item)

    console.log(f"{GREEN_OK} Score: {score}")