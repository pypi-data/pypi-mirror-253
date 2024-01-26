import typer

app = typer.Typer()



@app.command()
def main(name:str):
    print((f"Hello {name}"))



@app.command()
def goodbye(name:str):
    print(f"good bye {name}")