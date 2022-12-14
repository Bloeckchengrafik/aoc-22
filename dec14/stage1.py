from dec14.CaveScan import CaveScan


def stage(data: list[str]):
    scan = CaveScan(data)

    num = 0

    while True:
        if not scan.step():
            break
        num += 1

    print(f"Number of steps: {num}")
    print(scan)
