from rich.progress import track
from rich.console import Console
from dec04 import Pair

console = Console()


def stage(data: list[str]) -> list[str]:
    pairs = []

    for line in track(data, description="Building Pairs    "):
        pairs.append([Pair(x) for x in line.split(",")])

    overlaps = []

    for x, y in track(pairs, description="Checking Contained"):
        if x in y or y in x:
            overlaps.append(x)

    console.log(f"Number of Containments: {len(overlaps)}")