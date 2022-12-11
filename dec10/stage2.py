from rich.progress import track

from dec10.vm import VirtualMachine


def stage(data: list[str]):
    vm = VirtualMachine(data)
    data = vm.to_value_list()

    image = " "

    for i, value in enumerate(track(data)):
        i += 1

        sprite = [value, value + 1, value + 2]

        crt_draws = i % 40

        if crt_draws == 0:
            image += "\n"

        if crt_draws in sprite:
            image += "█"
        else:
            image += " "

    print(image)
