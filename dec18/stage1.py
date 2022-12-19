from dec18.ThreeDGrid import ThreeDGrid


def stage(data: list[str]):
    grid = ThreeDGrid()

    for line in data:
        grid.set(*map(int, line.split(',')), '#')

    # Count all the open faces
    count = 0
    for x in range(100):
        for y in range(100):
            for z in range(100):
                count += grid.count_open_faces(x, y, z, '#')
    print(count)
