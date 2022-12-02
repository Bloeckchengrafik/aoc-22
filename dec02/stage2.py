from rich.progress import track
from rich import print

from lib import GREEN_OK
from dec02.stage1 import stage as stage1

ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

SHOULD_LOSE = "X"
SHOULD_DRAW = "Y"
SHOULD_WIN = "Z"

LOSE_WIN_MATRIX = {
    SHOULD_LOSE: {
        OPPONENT_ROCK: SCISSORS,
        OPPONENT_PAPER: ROCK,
        OPPONENT_SCISSORS: PAPER,
    },
    SHOULD_DRAW: {
        OPPONENT_ROCK: ROCK,
        OPPONENT_PAPER: PAPER,
        OPPONENT_SCISSORS: SCISSORS,
    },
    SHOULD_WIN: {
        OPPONENT_ROCK: PAPER,
        OPPONENT_PAPER: SCISSORS,
        OPPONENT_SCISSORS: ROCK,
    },
}


def stage(data: list[str]) -> None:
    data_for_stage1 = []

    for line in track(data, "Transforming as Input for Stage 1"):
        rock_paper_scissors_round = line.split(" ")
        rock_paper_scissors_round[1] = LOSE_WIN_MATRIX[rock_paper_scissors_round[1]][rock_paper_scissors_round[0]]
        data_for_stage1.append(" ".join(rock_paper_scissors_round))

    print(f"{GREEN_OK} Transformed data for Stage 1, now running Stage 1")
    stage1(data_for_stage1)
