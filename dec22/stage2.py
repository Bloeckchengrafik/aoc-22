from dec22.AMazingMaze import AMazingMaze, DIRECTIONS


def walk(maze: AMazingMaze, times: int):
    for _ in range(times):
        maze.move_forward_cube()


def stage(data: list[str]):
    maze = AMazingMaze(data)
    current_num = 0
    for instruction in maze.instructions:
        if instruction in ["R", "L"]:
            walk(maze, current_num)
            maze.turn(instruction)
            current_num = 0
        else:
            current_num *= 10
            current_num += int(instruction)

    if current_num != 0:
        walk(maze, current_num)

    print(maze.x+1, maze.y+1, DIRECTIONS.index(maze.direction))
    y = ((maze.y + 1) * 1000)
    x = ((maze.x + 1) * 4)
    direction = DIRECTIONS.index(maze.direction)

    print(x + y + direction)
