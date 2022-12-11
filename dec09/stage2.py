import os
import time

from rich import table, print
from rich.progress import track

from dec09.MotionList import MotionList, move_tail_with_rules
from lib import GREEN_OK


def stage(data: list[str]):
    motions = MotionList(data)
    visited = set()

    n = int(os.environ.get("N", 9))

    head = [0, 0]
    tails = [[0, 0] for _ in range(n)]

    # Execute the motions on the head
    global_track = track(range(len(motions) * (n + 1)), description="Moving").__iter__()
    for motion in motions:
        head[0] += motion[0]
        head[1] += motion[1]
        next(global_track)

        for i in range(n):
            next(global_track)

            prev_tail = head
            if i > 0:
                prev_tail = tails[i - 1]

            tails[i] = move_tail_with_rules(prev_tail, tails[i])

        # Only count the last tail
        visited.add((*tails[-1],))
        time.sleep(0.0001)

    try:
        next(global_track)
    except StopIteration:
        pass

    print(f"{GREEN_OK} Visited {len(visited)} locations")
