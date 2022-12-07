import time

from rich.progress import track
from rich import print

NL = "\n"


class Command:
    def __init__(self, data: list[str]):
        name_and_args = data[0][2:].split(" ")
        self.name = name_and_args[0]
        self.args = name_and_args[1:]
        self.data = data[1:]

    def execute_ls(self, tree):
        tree.recalculate_node()
        time.sleep(0.0001)
        for line in self.data:
            if line.startswith("dir"):
                tree.node_by_path(tree.current_path).add_child(DirNode(line[4:]))
            else:
                filedata = line.split(" ")
                tree.node_by_path(tree.current_path).add_child(FileNode(filedata[1], int(filedata[0])))

    def execute_cd(self, tree):
        change_to = self.args[0]
        if change_to == "..":
            tree.current_path = "/" + "/".join(tree.current_path.split("/")[:-1])
        elif change_to.startswith("/"):
            tree.current_path = change_to
        else:
            tree.current_path += "/" + change_to

        tree.current_path = tree.current_path.replace("//", "/")

        if tree.current_path == "":
            tree.current_path = "/"

        tree.recalculate_node()

    def execute(self, tree):
        if self.name == "ls":
            self.execute_ls(tree)
        elif self.name == "cd":
            self.execute_cd(tree)

    def __str__(self):
        return f"Command {self.name} with args {self.args} and data {self.data}"


class Node:
    def __init__(self, path: str):
        self.path: str = path
        self.children: list[Node] = []
        self.size: int = 0
        self.type = "dir"

    def get_path(self):
        return self.path

    def calculate_size(self):
        if self.type == "file":
            return self.size

        self.size = 0
        for child in self.children:
            self.size += child.calculate_size()
        return self.size

    def str(self, indent: int = 0, nesting: bool = True):
        if self.type == "file":
            return f"{' ' * indent}F {self.path} ({self.calculate_size()})"
        elif nesting:
            return f"{' ' * indent}D {self.path} ({self.calculate_size()}){NL if len(self.children) > 0 else ''}" + "\n" \
                .join([child.str(indent + 2) for child in self.children])
        else:
            return f"{' ' * indent}D {self.path} ({self.calculate_size()})"


class FileNode(Node):
    def __init__(self, path: str, size: int):
        super().__init__(path)
        self.size = size
        self.type = "file"

    def calculate_size(self):
        return self.size


class DirNode(Node):
    def __init__(self, path: str):
        super().__init__(path)

    def calculate_size(self):
        self.size = 0
        for child in self.children:
            self.size += child.calculate_size()
        return self.size

    def add_child(self, child: Node):
        self.children.append(child)


class FileTree:
    def __init__(self):
        self.root: DirNode = DirNode("/")
        self.current_path = ""

    def parse(self, data: list[str]):
        data.append("$")
        # Partition the data into commands. A command starts with a line that
        # starts with a $ and ends before the next command.
        commands: list[Command] = []
        command_data: list[str] = []
        for line in track(data, "Parsing commands  "):
            if line.startswith("$"):
                if len(command_data) > 0:
                    commands.append(Command(command_data))
                    command_data = []
            command_data.append(line)

        # Execute the commands
        for command in track(commands, "Executing commands"):
            command.execute(self)

    def __str__(self):
        return self.root.str()

    def recalculate_node(self):
        # Make sure the current_path is represented in the tree
        current_node = self.root
        for path in self.current_path.split("/")[1:]:
            if path == "":
                continue
            for child in current_node.children:
                if child.get_path() == path:
                    current_node = child
                    break
            else:
                new_node = DirNode(path)
                current_node.add_child(new_node)
                current_node = new_node

    def node_by_path(self, path: str):
        current_node = self.root
        for path in path.split("/")[1:]:
            if path == "":
                continue
            for child in current_node.children:
                if child.get_path() == path:
                    current_node = child
                    break
            else:
                return None
        return current_node

    def traverse(self, node: Node = None):
        if node is None:
            node = self.root
        for child in node.children:
            yield child
            yield from self.traverse(child)


