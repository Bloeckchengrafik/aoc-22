from rich.progress import track
from rich import print

from dec07.FileTree import FileTree

all_nodes_sum: int = 0


def stage(data: list[str]):
    tree = FileTree()
    tree.parse(data)

    # Finding all directories with a size < 100000 and add the size of all files in them

    def work_on_node(current_node):
        global all_nodes_sum
        if current_node.type == "dir":
            current_node.calculate_size()
            if current_node.size < 100000:
                all_nodes_sum += current_node.size

    for node in tree.traverse():
        work_on_node(node)

    print(f"Total size of all files in directories with size < 100000: {all_nodes_sum}")
