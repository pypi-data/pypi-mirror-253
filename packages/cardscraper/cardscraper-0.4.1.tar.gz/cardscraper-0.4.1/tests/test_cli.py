import os

from cardscraper.__main__ import cli


def test_dry_run(test_dir):
    os.chdir(test_dir)
    cli(['gen', 'config.yaml'])
