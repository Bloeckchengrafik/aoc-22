from dec18.ThreeDGrid import ThreeDGrid


def floodfill_3d6(grid: ThreeDGrid, x: int, y: int, z: int, requirement: str, replacement: str):
    if grid.get(x, y, z) == requirement:
        grid.set(x, y, z, replacement)
        for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            # Check if the face is outside the grid
            if x + dx < 0 or x + dx >= 100 or y + dy < 0 or y + dy >= 100 or z + dz < 0 or z + dz >= 100:
                continue
            floodfill_3d6(grid, x + dx, y + dy, z + dz, requirement, replacement)


def floodfill_3d6_no_recurse(grid: ThreeDGrid, x: int, y: int, z: int, requirement: str, replacement: str):
    stack = [(x, y, z)]
    while stack:
        x, y, z = stack.pop()
        if grid.get(x, y, z) == requirement:
            grid.set(x, y, z, replacement)
            for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                # Check if the face is outside the grid
                if x + dx < 0 or x + dx >= 100 or y + dy < 0 or y + dy >= 100 or z + dz < 0 or z + dz >= 100:
                    continue
                stack.append((x + dx, y + dy, z + dz))


def stage(data: list[str]):
    grid = ThreeDGrid()

    for line in data:
        grid.set(*map(int, line.split(',')), '#')

    # Flood fill the grid
    floodfill_3d6_no_recurse(grid, 0, 0, 0, '.', 'O')

    # Count all the open faces
    count = 0
    for x in range(100):
        for y in range(100):
            for z in range(100):
                count += grid.count_open_faces(x, y, z, '#', "O")
    print(count)
