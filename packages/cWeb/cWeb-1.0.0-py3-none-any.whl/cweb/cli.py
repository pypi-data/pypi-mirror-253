from typing_extensions import Annotated

from cweb import __version__, fetch, generate_pdf

__author__ = "sanchezcarlosjr"
__copyright__ = "sanchezcarlosjr"
__license__ = "MIT"

from cweb import setup_logging, _logger

# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.

import typer
from typing import Optional

app = typer.Typer(help="The client for web renders web pages and transforms them into whatever format you need.")


@app.command()
def version():
    print(f"cWeb {__version__}")


@app.command()
def html(url: Annotated[str, typer.Argument()]):
    print(fetch(url))


@app.command()
def pdf(url: Annotated[str, typer.Argument()], path: Annotated[str, typer.Argument()]):
    generate_pdf(url, path)


@app.command()
def webapp(share=False):
    _logger.info("Starting webapp..")
    from cweb.webapp import webapp
    webapp.launch(share)


def run():
    app()
