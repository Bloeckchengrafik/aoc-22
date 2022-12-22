import os.path

import typer
from dec01.stage1 import stage as dec01_stage1
from dec01.stage2 import stage as dec01_stage2
from dec02.stage1 import stage as dec02_stage1
from dec02.stage2 import stage as dec02_stage2
from dec03.stage1 import stage as dec03_stage1
from dec03.stage2 import stage as dec03_stage2
from dec04.stage1 import stage as dec04_stage1
from dec04.stage2 import stage as dec04_stage2
from dec05.stage1 import stage as dec05_stage1
from dec05.stage2 import stage as dec05_stage2
from dec06.stage1 import stage as dec06_stage1
from dec06.stage2 import stage as dec06_stage2
from dec07.stage1 import stage as dec07_stage1
from dec07.stage2 import stage as dec07_stage2
from dec08.stage1 import stage as dec08_stage1
from dec08.stage2 import stage as dec08_stage2
from dec09.stage1 import stage as dec09_stage1
from dec09.stage2 import stage as dec09_stage2
from dec10.stage1 import stage as dec10_stage1
from dec10.stage2 import stage as dec10_stage2
from dec11.stage1 import stage as dec11_stage1
from dec11.stage2 import stage as dec11_stage2
from dec12.stage1 import stage as dec12_stage1
from dec12.stage2 import stage as dec12_stage2
from dec13.stage1 import stage as dec13_stage1
from dec13.stage2 import stage as dec13_stage2
from dec14.stage1 import stage as dec14_stage1
from dec14.stage2 import stage as dec14_stage2
from dec15.stage1 import stage as dec15_stage1
from dec15.stage2 import stage as dec15_stage2
from dec16.stage1 import stage as dec16_stage1
from dec16.stage2 import stage as dec16_stage2
from dec17.stage1 import stage as dec17_stage1
from dec17.stage2 import stage as dec17_stage2
from dec18.stage1 import stage as dec18_stage1
from dec18.stage2 import stage as dec18_stage2
from dec20.stage1 import stage as dec20_stage1
from dec20.stage2 import stage as dec20_stage2
from dec21.stage1 import stage as dec21_stage1
from dec21.stage2 import stage as dec21_stage2
from dec22.stage1 import stage as dec22_stage1
from dec22.stage2 import stage as dec22_stage2

app = typer.Typer()


def main(day: int, stage: int, file: str = typer.Option(..., "--file", "-f", help="Input file")):
    if not os.path.exists(file):
        typer.echo(typer.style(f"File {file} does not exist", fg=typer.colors.WHITE, bg=typer.colors.RED))
        raise typer.Exit(1)

    with open(file) as f:
        data = f.readlines()

    data = [line.replace("\n", "").replace("\r", "") for line in data]

    if day == 1 and stage == 1:
        typer.echo("Running day 1 stage 1: Calorie Counting (part 1)")
        dec01_stage1(data)
    elif day == 1 and stage == 2:
        typer.echo("Running day 1 stage 2: Calorie Counting (part 2)")
        dec01_stage2(data)
    elif day == 2 and stage == 1:
        typer.echo("Running day 2 stage 1: Rock Paper Scissors (part 1)")
        dec02_stage1(data)
    elif day == 2 and stage == 2:
        typer.echo("Running day 2 stage 2: Rock Paper Scissors (part 2)")
        dec02_stage2(data)
    elif day == 3 and stage == 1:
        typer.echo("Running day 3 stage 1: Rucksack Reorganization (part 1)")
        dec03_stage1(data)
    elif day == 3 and stage == 2:
        typer.echo("Running day 3 stage 2: Rucksack Reorganization (part 2)")
        dec03_stage2(data)
    elif day == 4 and stage == 1:
        typer.echo("Running day 4 stage 1: Camp Cleanup (part 1)")
        dec04_stage1(data)
    elif day == 4 and stage == 2:
        typer.echo("Running day 4 stage 2: Camp Cleanup (part 2)")
        dec04_stage2(data)
    elif day == 5 and stage == 1:
        typer.echo("Running day 5 stage 1: Supply Stacks (part 1)")
        dec05_stage1(data)
    elif day == 5 and stage == 2:
        typer.echo("Running day 5 stage 2: Supply Stacks (part 2)")
        dec05_stage2(data)
    elif day == 6 and stage == 1:
        typer.echo("Running day 6 stage 1: Tuning Trouble (part 1)")
        dec06_stage1(data)
    elif day == 6 and stage == 2:
        typer.echo("Running day 6 stage 2: Tuning Trouble (part 2)")
        dec06_stage2(data)
    elif day == 7 and stage == 1:
        typer.echo("Running day 7 stage 1: No Space left on Device (part 1)")
        dec07_stage1(data)
    elif day == 7 and stage == 2:
        typer.echo("Running day 7 stage 2: No Space left on Device (part 2)")
        dec07_stage2(data)
    elif day == 8 and stage == 1:
        typer.echo("Running day 8 stage 1: Treetop Tree House (part 1)")
        dec08_stage1(data)
    elif day == 8 and stage == 2:
        typer.echo("Running day 8 stage 2: Treetop Tree House (part 2)")
        dec08_stage2(data)
    elif day == 9 and stage == 1:
        typer.echo("Running day 9 stage 1: Rope Bridge (part 1)")
        dec09_stage1(data)
    elif day == 9 and stage == 2:
        typer.echo("Running day 9 stage 2: Rope Bridge (part 2)")
        dec09_stage2(data)
    elif day == 10 and stage == 1:
        typer.echo("Running day 10 stage 1: Cathode-Ray Tube (part 1)")
        dec10_stage1(data)
    elif day == 10 and stage == 2:
        typer.echo("Running day 10 stage 2: Cathode-Ray Tube (part 2)")
        dec10_stage2(data)
    elif day == 11 and stage == 1:
        typer.echo("Running day 11 stage 1: Monkey in the Middle (part 1)")
        dec11_stage1(data)
    elif day == 11 and stage == 2:
        typer.echo("Running day 11 stage 2: Monkey in the Middle (part 2)")
        dec11_stage2(data)
    elif day == 12 and stage == 1:
        typer.echo("Running day 12 stage 1: Hill Climbing Algorithm (part 1)")
        dec12_stage1(data)
    elif day == 12 and stage == 2:
        typer.echo("Running day 12 stage 2: Hill Climbing Algorithm (part 2)")
        dec12_stage2(data)
    elif day == 13 and stage == 1:
        typer.echo("Running day 13 stage 1: Distress Signal (part 1)")
        dec13_stage1(data)
    elif day == 13 and stage == 2:
        typer.echo("Running day 13 stage 2: Distress Signal (part 2)")
        dec13_stage2(data)
    elif day == 14 and stage == 1:
        typer.echo("Running day 14 stage 1: Regolith Reservoir (part 1)")
        dec14_stage1(data)
    elif day == 14 and stage == 2:
        typer.echo("Running day 14 stage 2: Regolith Reservoir (part 2)")
        dec14_stage2(data)
    elif day == 15 and stage == 1:
        typer.echo("Running day 15 stage 1: Beacon Exclusion Zone (part 1)")
        dec15_stage1(data)
    elif day == 15 and stage == 2:
        typer.echo("Running day 15 stage 2: Beacon Exclusion Zone (part 2)")
        dec15_stage2(data)
    elif day == 16 and stage == 1:
        typer.echo("Running day 16 stage 1: Proboscidea Volcanium (part 1)")
        dec16_stage1(data)
    elif day == 16 and stage == 2:
        typer.echo("Running day 16 stage 2: Proboscidea Volcanium (part 2)")
        dec16_stage2(data)
    elif day == 17 and stage == 1:
        typer.echo("Running day 17 stage 1: Pyroclastic Flow (part 1)")
        dec17_stage1(data)
    elif day == 17 and stage == 2:
        typer.echo("Running day 17 stage 2: Pyroclastic Flow (part 2)")
        dec17_stage2(data)
    elif day == 18 and stage == 1:
        typer.echo("Running day 18 stage 1: Boiling Boulders (part 1)")
        dec18_stage1(data)
    elif day == 18 and stage == 2:
        typer.echo("Running day 18 stage 2: Boiling Boulders (part 2)")
        dec18_stage2(data)
    elif day == 20 and stage == 1:
        typer.echo("Running day 20 stage 1: Grove Positioning System (part 1)")
        dec20_stage1(data)
    elif day == 20 and stage == 2:
        typer.echo("Running day 20 stage 2: Grove Positioning System (part 2)")
        dec20_stage2(data)
    elif day == 21 and stage == 1:
        typer.echo("Running day 21 stage 1: Monkey Math (part 1)")
        dec21_stage1(data)
    elif day == 21 and stage == 2:
        typer.echo("Running day 21 stage 2: Monkey Math (part 2)")
        dec21_stage2(data)
    elif day == 22 and stage == 1:
        typer.echo("Running day 22 stage 1: Monkey Map (part 1)")
        dec22_stage1(data)
    elif day == 22 and stage == 2:
        typer.echo("Running day 22 stage 2: Monkey Map (part 2)")
        dec22_stage2(data)
    else:
        typer.echo("Not implemented yet")


app.command()(main)

if __name__ == "__main__":
    app()
