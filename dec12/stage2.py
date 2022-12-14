from rich import print

from dec12.heightmap import HeightMap


def stage(data: list[str]):
    heightmap = HeightMap(data)

    a_s = heightmap.find(0)
    a_s.append(heightmap.find_start())

    values = []

    for a in a_s:
        hmd = heightmap.calculate_path(a)
        if hmd is not None:
            values.append(len(hmd) - 1)

    print(min(values))

