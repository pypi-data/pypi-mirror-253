"""
A tool for generating Anki packages by webscraping.

Takes in YAML input files and returns an Anki package based
on its instructions/contents.
This is primarily a CLI tool, but *can* be used inside code.
For the explanation of the YAML input files please read `cardscraper.Config`
docstring.

Typical usage example: ::

    $ cardscraper init hello.yaml
    $ nvim hello.yaml
    ...
    $ cardscraper gen hello.yaml
"""
from cardscraper.config import Config
from cardscraper.generate import (
    generate_anki_package,
    generate_anki_package_from_config_meta,
    get_entrypoints_by_step,
    select_function_by_step_and_name,
    write_package,
)

__all__ = [
    'Config',
    'get_entrypoints_by_step',
    'generate_anki_package_from_config_meta',
    'generate_anki_package',
    'select_function_by_step_and_name',
    'write_package',
]
