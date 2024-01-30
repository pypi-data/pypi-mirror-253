from datetime import datetime

from rich import print
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table
from typer import clear

from .article import Article, Author


def prompt_title() -> str:
    """Prompt the user for the title of the article."""
    return Prompt.ask(
        "[blue]Title of the article", default="A very interesting article"
    )


def prompt_short_title(title: str) -> str:
    """Prompt the user for the short title of the article."""
    return Prompt.ask(
        "[blue]Short title of the article?",
        default=title if len(title) < 150 else "",
    )


def prompt_year_of_publication() -> int:
    """Prompt the user for the year of publication of the article."""
    return IntPrompt.ask("[blue]Year of publication", default=datetime.now().year)


def prompt_authors() -> list[Author]:
    """Prompt the user for the authors of the article."""
    authors = []
    while True:
        clear()

        table = Table(title="Authors")
        table.add_column("Name")
        table.add_column("Surname")
        table.add_column("Email")
        table.add_column("Affiliation")
        table.add_column("Corresponding")

        for author in authors:
            table.add_row(
                author.name,
                author.surname,
                author.email,
                author.affiliation,
                "Yes" if author.is_corresponding else "No",
            )

        print(table)

        full_name: str = Prompt.ask(
            "[blue]Author's full name (leave blank to cancel)",
            default="",
            show_default=False,
        )

        # If the user left the field blank, stop asking for authors
        if not full_name:
            break

        # Split the full name into possible first, middle and last names
        name_words = full_name.strip().split(" ")

        # If the user only entered one word, try again
        if len(name_words) < 2:
            print("ERROR: Please enter the author's full name")
            continue
        else:  # We have at least two words and the surname is the last one
            surname = name_words[-1]
            name = " ".join(name_words[:-1])

        email = Prompt.ask("[blue]Author's email")
        affiliation = Prompt.ask("[blue]Author's affiliation")

        is_corresponding = Confirm.ask(
            f"[blue]Is {full_name} the corresponding author?",
            default=(
                True
                if len(authors) == 0
                and not any([author.is_corresponding for author in authors])
                else False
            ),
        )

        author = Author(name, surname, email, affiliation, is_corresponding)

        authors.append(author)

        if not Confirm.ask("[blue]Add another author?", default=True):
            break

    return authors


def prompt_abstract() -> str:
    """Prompt the user for the abstract of the article."""
    abstract = Prompt.ask("[blue]Abstract of the article?", default="")
    word_count = len(abstract.split(" "))
    if word_count >= 250:
        print(
            f"WARNING: Abstract is too long ({word_count} words), it should be less than 250 words"
        )

    return ". ".join([sentence.strip() for sentence in abstract.split(".")])


def prompt_keywords() -> list[str]:
    """Prompt the user for the keywords of the article."""
    keywords = Prompt.ask("[blue]Enter a comma-separated list of keywords", default="")
    return [keyword.strip() for keyword in keywords.split(",")]


def prompt_article() -> Article:
    """Prompt the user for the article."""
    title = prompt_title()
    short_title = prompt_short_title(title)
    year = prompt_year_of_publication()
    authors = prompt_authors()
    abstract = prompt_abstract()
    keywords = prompt_keywords()
    return Article(
        title=title,
        short_title=short_title,
        year=year,
        authors=authors,
        abstract=abstract,
    ).add_keywords(*keywords)
