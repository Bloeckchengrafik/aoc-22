from dec15.HCaveScan import HCaveScan
from rich import print


def stage(data: list[str]):
    at = int(input('At what y value do you want to see the scan? '))
    scan_raw = HCaveScan.parse_raw(data)
    scan = HCaveScan(scan_raw, at)
    print(scan.count())
