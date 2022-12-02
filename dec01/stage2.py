from rich.progress import track
from halo import Halo


def stage(data: list[str]):
    sums_of_calories = []
    current_sum = 0

    for line in track(data, "Calculating Sums"):
        if line == "":
            sums_of_calories.append(current_sum)
            current_sum = 0
            continue

        current_sum += int(line)

    spinner = Halo(text="Sorting...", spinner="dots")
    spinner.start()

    sums_of_calories.sort()
    sums_of_calories.reverse()

    max_three = sums_of_calories[:3]

    spinner.succeed("Done! The three highest sums are: " + str(max_three) + ", with a total of " + str(
        sum(max_three)) + " calories.")
