from abc import abstractmethod

from pylatexenc.latexencode import unicode_to_latex


class Insertable:
    @abstractmethod
    def to_latex(self) -> str:
        pass


class Command(Insertable):
    command: str
    options: list[str]
    arguments: list[str]

    def __init__(self, command: str, arguments: list[str] = [], *options: str):
        self.command = command
        self.options = options
        self.arguments = arguments

    def to_latex(self) -> str:
        command = f"\\{self.command}"

        if self.options:
            command += f"[{','.join(self.options)}]"
        if self.arguments:
            command += f"{{{','.join(self.arguments)}}}"

        return command


class Subsection(Command):
    def __init__(self, title: str):
        super().__init__("subsection", [title])


class Section(Command):
    def __init__(self, title: str):
        super().__init__("section", [title])


class Text(Insertable):
    text: str

    def __init__(self, text: str):
        self.text = unicode_to_latex(text)

    def to_latex(self) -> str:
        return self.text


class Environment(Insertable):
    name: str
    content: list[Insertable]

    def __init__(self, name: str, content: list[Insertable]):
        self.name = name
        self.content = content

    def to_latex(self) -> str:
        return (
            f"\\begin{{{self.name}}}\n"
            + "\n".join([c.to_latex() for c in self.content])
            + f"\n\\end{{{self.name}}}"
        )
