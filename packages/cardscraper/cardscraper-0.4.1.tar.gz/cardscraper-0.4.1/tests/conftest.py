import shutil
from pathlib import Path

import pytest
from cardscraper import Config
from genanki.model import yaml

path = Path('tests/files/').absolute()


@pytest.fixture(scope='session')
def config() -> Config:
    with (path / 'config.yaml').open() as f:
        config: Config = yaml.load(f, yaml.Loader)
    return config


@pytest.fixture(scope='session')
def test_dir(tmp_path_factory: pytest.TempPathFactory):
    tmp_path = tmp_path_factory.mktemp('files')
    files_dir = shutil.copytree(path, (tmp_path), dirs_exist_ok=True)

    return files_dir
