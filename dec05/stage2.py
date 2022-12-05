from rich.progress import track
from rich.console import Console

from dec05 import CargoCrane

console = Console()


def stage(data: list[str]):
    crane = CargoCrane(data)
    for move in track(crane.moves, description="Crane moves   "):
        crane.move_all(move)

    console.print(crane.get_top_of_all())
