from rich import print
from rich.progress import track

from dec17.Tetris import Tetris


def stage(data: list[str]):
    tetris = Tetris(list(data[0]))

    # Find the first one trillionth iteration
    for i in track(range(1, 1000000000)):
        tetris.step()

    print(tetris.get_height())
    