from rich.progress import track

from dec10.vm import VirtualMachine


def stage(data: list[str]):
    vm = VirtualMachine(data)
    data = vm.to_value_list()

    signal_strength = 0
    # Update the signal strength during the 20th cycle and every 40 cycles after that
    for i, value in enumerate(track(data)):
        i += 1
        if i == 20 or (i > 20 and (i-20) % 40 == 0):
            current = value * i
            print(f"Cycle {i}: {current} (x={value})")
            signal_strength += current

    print(f"Signal strength: {signal_strength}")
