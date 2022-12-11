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
    else:
        typer.echo("Not implemented yet")


app.command()(main)

if __name__ == "__main__":
    app()