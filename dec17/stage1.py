from rich import print
from rich.progress import track

from dec17.Tetris import Tetris


def stage(data: list[str]):
    tetris = Tetris(list(data[0]))
    for _ in track(range(2022)):
        tetris.step()
    print(tetris.get_height())
