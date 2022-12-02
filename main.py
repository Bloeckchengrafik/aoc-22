import os.path

import typer
from dec01.stage1 import stage as dec01_stage1
from dec01.stage2 import stage as dec01_stage2
from dec02.stage1 import stage as dec02_stage1
from dec02.stage2 import stage as dec02_stage2

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
    else:
        typer.echo("Not implemented yet")


app.command()(main)

if __name__ == "__main__":
    app()