from concurrent.futures import ThreadPoolExecutor

from re import findall


class HCaveScan:
    """
    This is a horizontal cave scan on one y-line
    That line is 20000000 long
    """
    OFFSET = 10000000

    def __init__(self, parsed: list[tuple[int, int, int, int]], at):
        self.parsed = parsed
        self.at = at
        self.scanline = [0] * 20000000

        scanline_beacons = []
        for _, _, x, y in self.parsed:
            if y == at:
                scanline_beacons.append(x)

        open_cues = 0

        def parse_line(line):
            nonlocal open_cues

            scanner = (line[0], line[1])
            beacon = (line[2], line[3])

            open_cues += 1
            distance = abs(scanner[0] - beacon[0]) + abs(scanner[1] - beacon[1])

            # walk left
            current = scanner[0]
            while True:
                if current not in scanline_beacons:
                    self.scanline[current + self.OFFSET] = 1
                current -= 1
                if abs(current - scanner[0]) + abs(at - scanner[1]) > distance:
                    break

            # walk right
            current = scanner[0]
            while True:
                if current not in scanline_beacons:
                    self.scanline[current + self.OFFSET] = 1
                current += 1
                if abs(current - scanner[0]) + abs(at - scanner[1]) > distance:
                    break

        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(parse_line, self.parsed)

    def count(self):
        final_count = self.scanline.count(1)
        return final_count

    @staticmethod
    def parse_raw(raw: list[str]) -> list[tuple[int, int, int, int]]:
        """
        Parse the raw data into a list of tuples
        Each tuple is a pair of coordinates

        This is done by finding all 4 numbers in the input with regex
        """
        return [tuple(map(int, findall(r'\d+', line))) for line in raw]
