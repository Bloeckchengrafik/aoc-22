import math
from rich import print

from dec12.astar import Graph

LEVELS = "abcdefghijklmnopqrstuvwxyz"


class HeightMap:
    class HNode:
        def __init__(self, height: int, start=False, end=False):
            self.height = height
            self.start = start
            self.end = end

        def __repr__(self):
            return self.height.__repr__().rjust(2)

    def __init__(self, raw: list[str]):
        """
        The raw map is a grid of characters, each representing a height.
        """
        self.raw = raw
        self.heights = [
            [self.parse_node(c) for c in line]
            for line in raw
        ]

    def parse_node(self, char: str) -> HNode:
        if char == "S":
            return self.HNode(0, start=True)

        if char == "E":
            return self.HNode(LEVELS.index('z'), end=True)

        return self.HNode(LEVELS.index(char))

    def find_start(self):
        for y, line in enumerate(self.heights):
            for x, node in enumerate(line):
                if node.start:
                    return y, x, node

    def find_end(self):
        for y, line in enumerate(self.heights):
            for x, node in enumerate(line):
                if node.end:
                    return y, x, node

    def transform_to_graph(self):
        """
        Transform the heightmap into a graph.
        """
        # Transform the heightmap into a list of adjacent nodes.
        # The nodes are the same as the heightmap, but the edges are the
        # adjacent nodes.

        nodes = {}
        for y, line in enumerate(self.heights):
            for x, node in enumerate(line):
                # Find the adjacent nodes.
                adjacent = []
                # Left
                if x > 0:
                    delta = self.heights[y][x - 1].height - node.height
                    # The adjacent node must be at the same height or one above. It can be as many below as it wants.
                    if delta <= 1:
                        adjacent.append(((y, x - 1, self.heights[y][x - 1]), 1))
                # Right
                if x < len(line) - 1:
                    delta = self.heights[y][x + 1].height - node.height
                    if delta <= 1:
                        adjacent.append(((y, x + 1, self.heights[y][x + 1]), 1))
                # Up
                if y > 0:
                    delta = self.heights[y - 1][x].height - node.height
                    if delta <= 1:
                        adjacent.append(((y - 1, x, self.heights[y - 1][x]), 1))
                # Down
                if y < len(self.heights) - 1:
                    delta = self.heights[y + 1][x].height - node.height
                    if delta <= 1:
                        adjacent.append(((y + 1, x, self.heights[y + 1][x]), 1))
                nodes[y, x, node] = adjacent

        return nodes

    def calculate_path(self, start=None):
        """
        Calculate the possible paths between the start and end nodes.
        The user can only move to a node that is at the same height or one above or below.
        The user has to choose the path that is the shortest.
        The path must be a sequence of nodes that are adjacent to each other.
        """
        if start is None:
            start = self.find_start()
        end = self.find_end()
        graph = Graph(self.transform_to_graph())

        return graph.a_star_algorithm(start, end)

    def __repr__(self):
        grid = "\n".join(
            " ".join(str(h) for h in line)
            for line in self.heights
        )
        return grid

    def find(self, height) -> list[tuple[int, int, int]]:
        """
        Find all nodes at the given height.
        """
        nodes = []
        for y, line in enumerate(self.heights):
            for x, node in enumerate(line):
                if node.height == height:
                    nodes.append((y, x, node))

        return nodes
