import time

from rich import table, print
from rich.progress import track

from dec09.MotionList import MotionList, move_tail_with_rules
from lib import GREEN_OK


def stage(data: list[str]):
    motions = MotionList(data)
    visited = set()

    head = [0, 0]
    tail = [0, 0]

    # Execute the motions on the head
    for motion in track(motions, description="Moving head"):
        head[0] += motion[0]
        head[1] += motion[1]

        tail = move_tail_with_rules(head, tail)
        visited.add((*tail,))
        # Wait for 0.0001 seconds to make the progress bar more visible
        time.sleep(0.0001)

    print(f"{GREEN_OK} Visited {len(visited)} locations")
