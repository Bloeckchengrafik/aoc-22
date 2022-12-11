from rich.progress import track
from rich import print

from dec07.FileTree import FileTree
from lib import *

TOTAL_DISK_SPACE = 70000000


def stage(data: list[str]):
    tree = FileTree()
    tree.parse(data)

    tree.root.calculate_size()

    available_space = TOTAL_DISK_SPACE - tree.root.size
    required_space = 30000000

    delta = required_space - available_space

    # Find all directories that, if deleted, would free enough space to fit the required space
    directories = []
    for node in tree.traverse():
        if node.type == "dir":
            node.calculate_size()
            if node.size > delta:
                directories.append(node)

    # Sort the directories by size
    directories.sort(key=lambda x: x.size)

    # What is the smallest directory that we can delete?
    smallest_directory = directories[0]

    print(f"Smallest directory that can be deleted: {smallest_directory.str(nesting=False)}")
