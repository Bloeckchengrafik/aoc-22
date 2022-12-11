from rich.progress import track

from dec11.monke import Monke


def stage(data: list[str]):
    # Split the data by empty lines
    data = "\n".join(data).split("\n\n")
    # Split the data by newlines
    data = [i.splitlines() for i in data]
    # Create a list of Monke objects
    monkeys = [Monke(i) for i in data]

    master_divisor = 1

    for monke in monkeys:
        master_divisor *= monke.test

    print(f"Master divider: {master_divisor}")

    for _ in track(range(1000), description="Running monkeys"):
        for monke in monkeys:
            while monke.starting_items:
                throw, item = monke.inspect_item(stress=True, divider=master_divisor)
                monkeys[throw].add_item(item)

    for monke in monkeys:
        print(f"Monke {monke.num} has {len(monke.starting_items)} items: {monke.starting_items} "
              f"with monke buisness {monke.num_items_inspected}")

    # Multiply the two maximal num_items_inspected values
    data = [monke.num_items_inspected for monke in monkeys]
    data.sort()
    print(f"Monke buisness: {data[-1] * data[-2]}")
