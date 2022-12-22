from dec21.MonkeyDependencyGraph import MDGraph


def stage(data: list[str]):
    graph = MDGraph(data)
    print(int(graph.get_node("root").collapse(graph)))
