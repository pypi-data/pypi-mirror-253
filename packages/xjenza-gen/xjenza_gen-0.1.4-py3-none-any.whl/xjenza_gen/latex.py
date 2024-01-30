import subprocess
from os import path

from latexbuild import render_latex_template
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn

from .article import Article


class LatexEngine:
    """This class is responsible for building the final PDF document from the given Article object."""

    template_folder: str
    template_file: str
    output_folder: str
    output_file: str
    debug: bool

    def __init__(
        self,
        template_folder: str,
        template_file: str,
        output_folder: str,
        output_file: str,
        debug: bool = False,
    ):
        assert path.exists(template_folder), "Path to Jinja2 template does not exist"
        assert path.isfile(
            path.join(template_folder, template_file)
        ), "Path to template file does not exist"

        self.template_folder = template_folder
        self.template_file = template_file
        self.output_folder = output_folder
        self.output_file = output_file
        self.debug = debug

    def write_tex(self, article: Article):
        """This method writes the content of the Article object to a .tex file, using the Jinja2 template engine."""
        template_dictionary = article.dict()
        template_dictionary.update({"name": self.output_file})
        content = render_latex_template(
            self.template_folder, self.template_file, template_dictionary
        )

        with open(path.join(self.output_folder, self.output_file), "w") as f:
            f.write(content)
            f.close()

    def compile_pdf(self):
        with Progress(
            SpinnerColumn(finished_text=":heavy_check_mark:"),
            TextColumn("[bold blue]{task.description} [cyan]{task.fields[file_name]}"),
        ) as progress:
            task = progress.add_task(
                "Compiling...", total=None, file_name=self.output_file
            )

            subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-output-directory",
                    self.output_folder,
                    self.output_file,
                ],
                stdout=subprocess.DEVNULL if not self.debug else None,
                stderr=subprocess.STDOUT if not self.debug else None,
            )

            progress.update(task, total=1, advance=1, completed=1)

    def run_biber(self):
        with Progress(
            SpinnerColumn(finished_text=":heavy_check_mark:"),
            TextColumn(
                "[bold blue]{task.description} on [cyan]{task.fields[file_name]}"
            ),
        ) as progress:
            task = progress.add_task(
                "Running biber", total=None, file_name=self.output_file
            )

            print(path.join(self.output_folder, self.output_file.removesuffix(".tex")))

            subprocess.run(
                [
                    "biber",
                    path.join(
                        self.output_folder, self.output_file.removesuffix(".tex")
                    ),
                ],
                stdout=subprocess.DEVNULL if not self.debug else None,
                stderr=subprocess.STDOUT if not self.debug else None,
            )

            progress.update(task, total=1, advance=1, completed=1)

    def build_article(self, article: Article) -> str:
        """
        This method is responsible for building the final PDF document from the given Article object.

        It performs the following steps:
        1. Writes the content of the Article object to a .tex file.
        2. Compiles the .tex file into a .pdf file.
        3. Runs the biber command to process the bibliography in the .tex file.
        4. Compiles the .tex file into a .pdf file two more times. This is necessary as LaTeX sometimes requires multiple passes to resolve all references correctly.

        Args:
            article (Article): The Article object containing the content to be written to the .tex file.

        Returns:
            path of the generated PDF file
        """
        self.write_tex(article)
        self.compile_pdf()
        self.run_biber()
        self.compile_pdf()
        self.compile_pdf()

        return path.join(self.output_folder, self.output_file.strip(".tex") + ".pdf")

    def compile(self):
        with Progress(
            SpinnerColumn(finished_text=":heavy_check_mark:"),
            TextColumn("[bold blue]{task.description} [cyan]{task.fields[file_name]}"),
        ) as progress:
            task = progress.add_task(
                "Compiling...", total=None, file_name=self.output_file
            )
            subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-output-directory",
                    self.output_folder,
                    self.output_file,
                ],
                stdout=subprocess.DEVNULL if not self.debug else None,
                stderr=subprocess.STDOUT if not self.debug else None,
            )

            progress.update(task, total=1, advance=1, completed=1)

