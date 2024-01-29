import logging
import os
from pathlib import Path

from genanki import Deck, Package

from cardscraper.config import Config


def get_package(config: Config, deck: Deck) -> tuple[Package, Path]:
    package_config = config['package']
    name = package_config['name'].removesuffix('.apkg')
    output_path = package_config['output']
    media_path = package_config['media']
    pattern = package_config['pattern']

    if media_path:
        media = [str(path) for path in Path(media_path).rglob(pattern)]
    else:
        media = []
    package = Package(deck, media)
    path = Path(os.path.join(output_path, name + '.apkg'))
    logger = logging.getLogger('cardscraper')
    logger.info('Generated package!')
    return package, path
