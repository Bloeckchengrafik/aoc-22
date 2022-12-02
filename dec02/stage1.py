from rich.progress import track
from rich import print
from lib import *

ROCK = 1
PAPER = 2
SCISSORS = 3

ALIASES_ROCK = ["A", "X"]
ALIASES_PAPER = ["B", "Y"]
ALIASES_SCISSORS = ["C", "Z"]

ALIASES_DICT = {
    ROCK: ALIASES_ROCK,
    PAPER: ALIASES_PAPER,
    SCISSORS: ALIASES_SCISSORS,
}

WIN_MAP = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}


def stage(data: list[str]) -> None:
    input_data = []

    for line in track(data, "Transforming"):
        rock_paper_scissors_round = line.split(" ")

        for guess_type, aliases in ALIASES_DICT.items():
            for alias in aliases:
                if alias == rock_paper_scissors_round[0]:
                    rock_paper_scissors_round[0] = guess_type

                if alias == rock_paper_scissors_round[1]:
                    rock_paper_scissors_round[1] = guess_type

        input_data.append(rock_paper_scissors_round)

    scores = []

    for input_round in track(input_data, "Calculating "):
        """
         The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for 
         Scissors) plus the score for the outcome of the round 
         (0 if you lost, 3 if the round was a draw, and 6 if you won).
        """

        current_score = input_round[1] # The score for the shape you selected

        if input_round[0] == input_round[1]:
            current_score += 3
        elif WIN_MAP[input_round[0]] == input_round[1]:
            current_score += 6

        scores.append(current_score)

    print(f"{GREEN_OK} Player 2's score is {sum(scores)}")