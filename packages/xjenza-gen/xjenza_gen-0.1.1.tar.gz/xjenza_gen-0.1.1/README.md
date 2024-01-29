# xjenza-gen

This tool is a Python-based utility designed to automate the process of creating
and compiling LaTeX documents.

## Prerequisites

To run this tool successfully, you will need:

- Python 3.6 or later (I'll assume you have this already)
- LaTeX distribution installed (e.g., TeX Live, MiKTeX)
- [`biber`](https://en.wikipedia.org/wiki/Biber_(LaTeX)) bibliography tool

### macOS

If you don't have a package manager installed, I recommend installing
[Homebrew](https://brew.sh/).

```bash
brew install biber texlive
```

### Ubuntu

```bash
sudo apt-get install biber texlive-full
```

## Usage

To get started, install `xjenza-gen` using `pip` or [`pipx`](https://github.com/pypa/pipx) (recommended):

> [!NOTE]
> macOS users that want to give `pipx` a try should install it using `brew install pipx`.
> Ubuntu users can install it using `pip install --user pipx`.

```bash
pip install xjenza-gen
```

## Quick Start

It's very easy to get started with `xjenza-gen`. Simply run the following
command:

```bash
xjenza-gen new [article-name]
```

You will be prompted to enter the title, author, and some other basic information about
your article.

`xjenza-gen` will then create new directory called `article-name` under your
current directory with the following structure:

```text
article-name/
├── packages/
│   ├── logo.pdf
│   ├── xjenza-preamble.tex
│   └── xjenza.sty
├── figs/
├── bibliography.bib
├── article-name.tex
```

and populate `article-name.tex` with the information you provided. This file is the main LaTeX file you will be working with, following the template found [here](https://www.overleaf.com/latex/templates/xjenza-article/ktbfsjgqqcpw).

## Acknowledgements

- William Hicklin for the [xjenza LaTeX template](https://www.overleaf.com/latex/templates/xjenza-article/ktbfsjgqqcpw)
- [Malta Chamber of Scientists](https://www.mcs.org.mt/)