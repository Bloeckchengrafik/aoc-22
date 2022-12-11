from gmpy2 import mpz


class Monke:
    def __init__(self, data: list[str]):
        self.num = int(data[0].split()[1][:-1])
        self.starting_items = [int(x.replace(",", "")) for x in data[1].split()[2:]]
        self.operation = " ".join(data[2].split()[1:])
        self.test = int(data[3].split()[3])
        self.if_true = int(data[4].split()[-1])
        self.if_false = int(data[5].split()[-1])
        self.num_items_inspected = 0

    def __repr__(self):
        return f"Monke(\n\tid={self.num}, \n\tstarting_items={self.starting_items}, \n\toperation={self.operation}, \n\ttest={self.test}, \n\tif_true={self.if_true}, \n\tif_false={self.if_false}\n)"

    def __str__(self):
        return self.__repr__()

    def inspect_item(self, stress: bool = False, divider: int = -1):
        self.num_items_inspected += 1
        item = self.starting_items.pop(0)
        item = eval(self.operation.replace("new = ", ""), {"old": item})
        if not stress:
            item = item // 3

        if item % self.test == 0:
            return self.if_true, item

        return self.if_false, item

    def add_item(self, item: int):
        self.starting_items.append(item)
