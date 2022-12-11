class Instruction:
    def __init__(self, opcode, arg):
        self.opcode = opcode
        self.arg = arg

    def __repr__(self):
        return f"{self.opcode} {self.arg}"

    def mutate_vm(self, vm):
        if self.opcode == "addx":
            vm.x += int(self.arg)

    def get_length(self):
        if self.opcode == "addx":
            return 2
        return 1


class VirtualMachine:
    def __init__(self, source: list[str]):
        self.program: list[Instruction] = []

        for line in source:
            data = line.split(" ")
            if len(data) == 1:
                data.append("")
            self.program.append(Instruction(*data))

        self.cycle = 0
        self.current_instruction_nr = 0
        # This VM has one register, called "x"
        self.x = 1

    def to_value_list(self):
        data = []
        for instruction in self.program:
            for _ in range(instruction.get_length() - 1):
                data.append(self.x)

            data.append(self.x)
            instruction.mutate_vm(self)

        return data

    def __repr__(self):
        return f"VirtualMachine(x={self.x}, pc={self.cycle})"
