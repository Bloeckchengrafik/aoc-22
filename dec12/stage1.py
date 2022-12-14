from dec12.heightmap import HeightMap
from rich import print


def stage(data: list[str]):
    """
    The first stage is to find the shortest path between the start and end
    nodes. The path must be a sequence of nodes that are at the same height
    or lower than the previous node. The path must also be a sequence of
    nodes that are adjacent to each other.
    """
    heightmap = HeightMap(data)
    print(len(heightmap.calculate_path())-1)
