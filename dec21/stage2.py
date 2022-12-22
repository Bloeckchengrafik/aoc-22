from dec21.MonkeyDependencyGraph import MDGraph
import sympy


def stage(data: list[str]):
    graph = MDGraph(data)

    graph.get_node("root").operator = '='
    humn = graph.get_node("humn")
    humn.value = "x"

    equation = graph.to_equation()[1:-1].split("=")
    x = sympy.symbols("x")
    eq = sympy.Eq(eval(equation[0], {"x": x}), eval(equation[1], {"x": x}))
    print(round(sympy.solve(eq)[0]))
