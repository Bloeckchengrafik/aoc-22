from dec15.HCaveScan import HCaveScan
from rich import print


def stage(data: list[str]):
    scan_raw = HCaveScan.parse_raw(data)
    for i in range(0, 20):
        scan = HCaveScan(scan_raw, i)
        if scan.count() >= 20:
            continue

        print(i)
        break

