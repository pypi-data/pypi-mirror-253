import argparse
import logging
from typing import Sequence, get_args

import yaml

from cardscraper.__version__ import __version__
from cardscraper.config import Config
from cardscraper.generate import (
    StepName,
    generate_anki_package_from_config_meta,
    get_entrypoints_by_step,
    write_package,
)
from cardscraper.template import TEMPLATE


def cli(argv: Sequence[str] | None = None):
    logger = logging.getLogger('cardscraper')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(20)

    parser = argparse.ArgumentParser(
        prog='cardscraper',
        description='A tool for generating Anki packages by webscraping',
    )

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=__version__,
    )

    subparsers = parser.add_subparsers(dest='command')

    gen_parser = subparsers.add_parser(
        'gen',
        help='generate Anki packages',
        description='Generates Anki packages from input files',
    )

    gen_parser.add_argument(
        'file',
        nargs='+',
        metavar='file',
        type=argparse.FileType(),
        help='yaml input file(s)',
    )

    init_parser = subparsers.add_parser(
        'init',
        help='generate skeleton input files',
        description='Generates easily modifiable input file skeletons',
    )

    init_parser.add_argument(
        'file',
        nargs='+',
        metavar='file',
        type=argparse.FileType('w'),
        help='file name(s)',
    )

    subparsers.add_parser(
        'list',
        help='list available functions',
        description='List all available functions for each step',
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return

    match args.command:
        case 'gen':
            for file in args.file:
                config: Config = yaml.load(file, yaml.Loader)
                package, path = generate_anki_package_from_config_meta(config)
                write_package(package, path)
        case 'init':
            for file in args.file:
                file.write(TEMPLATE)
        case 'list':
            for step in get_args(StepName):
                points = get_entrypoints_by_step(step)
                print(f'Available functions for {step}:')
                for point in points:
                    print(f'  - {point.name}')


if __name__ == '__main__':
    cli()
