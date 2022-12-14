from dec14.CaveScan import CaveScan


def stage(data: list[str]):
    scan = CaveScan(data)

    scan.add_floor()

    num = 0

    while True:
        try:
            num += 1
            scan.step()
        except RuntimeError:
            break

    print(f"Number of steps: {num}")
    print(scan)
