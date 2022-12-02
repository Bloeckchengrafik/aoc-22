from rich.progress import track
from rich import print
from lib import *


def stage(data: list[str]):
    sum_current = 0
    sum_max = 0

    for line in track(data, description="Calculating"):
        if line == "":
            if sum_current > sum_max:
                sum_max = sum_current
            sum_current = 0

            continue

        sum_current += int(line)

    print(f"{GREEN_OK} Sum: {sum_max}")