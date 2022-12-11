from rich.progress import track

from dec11.monke import Monke


def stage(data: list[str]):
    # Split the data by empty lines
    data = "\n".join(data).split("\n\n")
    # Split the data by newlines
    data = [i.splitlines() for i in data]
    # Create a list of Monke objects
    monkeys = [Monke(i) for i in data]

    for _ in track(range(20), description="Running monkeys"):
        for monke in monkeys:
            while monke.starting_items:
                throw, item = monke.inspect_item()
                monkeys[throw].add_item(item)

    # Multiply the two maximal num_items_inspected values
    data = [monke.num_items_inspected for monke in monkeys]
    data.sort()
    print(f"Monke buisness: {data[-1] * data[-2]}")
