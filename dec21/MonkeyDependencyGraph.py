from functools import reduce


def mul(iterable):
    return reduce(lambda x, y: x * y, iterable)


def div(iterable):
    return reduce(lambda x, y: x / y, iterable)


def sub(iterable):
    return reduce(lambda x, y: x - y, iterable)


def match(it):
    if it[0] == it[1]:
        return 1
    else:
        return 0


class Node:
    def __init__(self, name, value=None, operator=None, dependencies=None):
        self.name = name
        self.dependencies = dependencies
        if dependencies is None:
            self.dependencies = []

        self.value = value
        self.operator = operator

    def operate(self, values):
        if self.operator == '+':
            return sum(values)
        elif self.operator == '*':
            return mul(values)
        elif self.operator == '/':
            return div(values)
        elif self.operator == '-':
            return sub(values)
        elif self.operator == '=':
            return match(values)

    def collapse(self, graph):
        if self.operator is None:
            return self.value
        else:
            return self.operate([graph.get_node(dep).collapse(graph) for dep in self.dependencies])

    def to_equation(self, graph):
        if self.operator is None:
            return str(self.value)
        else:
            return f"({self.operator.join([graph.get_node(dep).to_equation(graph) for dep in self.dependencies])})"


class MDGraph:
    def __init__(self, data: list[str]):
        self.data = data
        self.nodes = set()
        self.parse()

    def parse(self):
        for line in self.data:
            name, payload = line.split(": ")
            if len(payload.split(" ")) == 1:
                self.nodes.add(Node(name, value=int(payload)))
            else:
                dep1, operator, dep2 = payload.split(" ")
                self.nodes.add(Node(name, operator=operator, dependencies=[dep1, dep2]))

    def get_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def to_equation(self):
        return self.get_node("root").to_equation(self)
