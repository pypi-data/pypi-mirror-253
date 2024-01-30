import re
import shutil
from os import path
from pathlib import Path

import typer
from rich import print
from rich.prompt import Prompt
from typing_extensions import Annotated

from xjenza_gen.article import Article, Author
from xjenza_gen.latex import LatexEngine
from xjenza_gen.prompts import prompt_article

app = typer.Typer()

def is_in_project_folder():
    """Check if the current working directory is a Xjenza project folder."""
    return path.exists("./packages/xjenza.sty")

@app.command()
def new(
    name: Annotated[str, typer.Argument(..., help="Name of the project")] = "",
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode"),
):
    print("\n:sparkles: [green]Creating a new Xjenza article... \n")

    if not name:
        name = Prompt.ask("[blue]Project name", default="xjenza_article")
        print()

    regex_name = r"^[a-zA-Z0-9_-]*$"

    if not name.strip() or not re.match(regex_name, name):
        print(
            f"[red]:x: Project name '{name}' is invalid. Please use only alphanumeric characters, dashes and underscores."
        )

        raise typer.Exit(1)

    internal_path = path.dirname(path.realpath(__file__))

    latex = copy_skel(internal_path, name, debug)

    article = prompt_article()

    print("\n:pencil: Data entry complete, generating files...\n")

    latex.build_article(article)

    print(
        f"\n:tada: [green]Done! Feel free to edit the generated files at [cyan]'{path.abspath(name)}'."
    )


@app.command()
def clean():

    if not is_in_project_folder():
        print(
            "[red]Error: 'xjenza.sty' not found in packages folder. Please run this command from the root of a Xjenza Online project."
        )
        raise typer.Exit(1)

    exts_to_remove = ["aux", "log", "out", "toc", "bbl", "blg", "synctex.gz", 'fdb_latexmk', 'fls', 'bcf', 'run.xml', 'synctex(busy)', 'synctex.gz(busy)']

    # remove all files with the above extensions
    for ext in exts_to_remove:
        for file in Path(".").glob(f"*.{ext}"):
            file.unlink()

        for file in Path("./packages").glob(f"*.{ext}"):
            file.unlink()

@app.command()
def build(
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode"),
):

    if not is_in_project_folder():
        print(
            "\n[red]:x: 'xjenza.sty' not found in packages folder. Please run this command from the root of a Xjenza Online project."
        )
        raise typer.Exit(1)


    internal_path = path.dirname(path.realpath(__file__))

    name = path.basename(path.abspath("."))

    latex = LatexEngine(
        path.join(internal_path, "templates"),
        "main.tex",
        "./",
        name + ".tex",
        debug,
    )

    latex.compile()

    print(
        f"\n:tada: [green]Done! Feel free to edit the generated files at [cyan]'{path.abspath(name)}'."
    )


def copy_skel(src: path, dst: path, debug: bool = False):
    """Copy the skeleton project to the specified folder."""
    if path.exists(dst):
        print(f"[red]Folder '{dst}' already exists, exiting...")
        raise typer.Exit(1)

    internal_output_path = path.join(src, "outputs")
    internal_template_folder = path.join(src, "templates")

    if not path.exists(internal_output_path):
        print(
            f"\n[red]Template folder was not bundled with the package! Please reinstall the package."
        )
        raise typer.Exit(1)

    try:
        shutil.copytree(internal_output_path, dst)
    except Exception as e:
        print(f"[red]Error copying output folder: {e}")
        raise typer.Exit(1)

    return LatexEngine(
        internal_template_folder,
        "main.tex",
        path.abspath(dst),
        path.basename(dst) + ".tex",
        debug,
    )

