from rich.progress import track
from rich.console import Console
from dec04 import Pair

console = Console()


def stage(data: list[str]) -> list[str]:
    pairs = []

    for line in track(data, description="Building Pairs   "):
        pairs.append([Pair(x) for x in line.split(",")])

    overlaps = []

    for x, y in track(pairs, description="Checking Overlaps"):
        if x.overlaps(y) or y.overlaps(x):
            overlaps.append(x)

    console.log(f"Number of Overlaps: {len(overlaps)}")
