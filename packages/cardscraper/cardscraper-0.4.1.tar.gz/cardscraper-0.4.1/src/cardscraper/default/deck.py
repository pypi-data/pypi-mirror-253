import logging

from genanki import Deck, Note

from cardscraper.config import Config


def get_deck(config: Config, notes: list[Note]) -> Deck:
    deck_config = config['deck']
    id = deck_config['id']
    name = deck_config['name']

    deck = Deck(id, name)
    deck.notes.extend(notes)
    logger = logging.getLogger('cardscraper')
    logger.info('Generated deck!')
    return deck
