# cardscraper

Webscraping tool for generating Anki packages.

## Installation

From [PyPI](https://pypi.org/project/cardscraper/):

```sh
pip install cardscraper
```

From git:

```sh
pip install git+https://github.com/sakhezech/cardscraper
```

## Usage

`cardscraper ...` or `python -m cardscraper ...`

Generate a skeleton input file:

```sh
cardscraper init filename.yaml
```

Edit it with your favorite text editor:

```sh
nvim filename.yaml
```

Generate the package:

```sh
cardscraper gen filename.yaml
```

For more info use `cardscraper -h`.

## Input files

You can generate a skeleton input file by using `cardscraper init filename.yaml`.

Here is a big self-explaining input file example:

```yaml
# here you can specify which function to use for each step
# (every one defaults to 'default')
meta:
  # controls package details and package dumping
  package: default
  # controls deck creation
  deck: default
  # controls model creation
  model: default
  # controls scraping and note creation
  scraping: default

# anki package info
package:
  # package name
  name: package_name
  # output folder (defaults to '.')
  output: ./out/
  # media folder (defaults to null)
  # the directory will be walked recursively
  # every pattern matched file will be added to the package as media
  media: ./media/
  # pattern to match files against for media (defaults to **/*.*)
  pattern: "**/*.png"

# anki deck info
deck:
  # deck name
  name: Deck
  # deck id
  # don't forget to make this value unique
  id: 987

# anki model info
model:
  # model name
  name: Model
  # model id
  # don't forget to make this value unique
  id: 321
  # card styling (defaults to '')
  css: |
    .question, .answer {
        text-align: center;
    }
    .question {
        font-size: 5rem;
        font-weight: 700;
    }
    .answer {
        font-size: 3rem;
    }
  # list of cards
  templates:
    # card name
    - name: Front
      # front side
      qfmt: |
        <div class='question'>
        {{Question}}
        </div>
      # back side
      afmt: |
        {{FrontSide}}
        <hr id='answer'>
        <div class='answer'>
        {{Answer}}
        </div>
    # same here
    - name: Back
      qfmt: |
        <div class='question'>
        {{Answer}}
        </div>
      afmt: |
        {{FrontSide}}
        <hr id='answer'>
        <div class='answer'>
        {{Question}}
        </div>

# scraping info
scraping:
  # list of urls to scrape
  urls:
    - https://www.scrapethissite.com/pages/simple/
  # you can set your own custom user agent (defaults to null)
  agent: Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0
  # list of queries
  # each query selects an html element and lets you use its text in the templates
  # each child query runs inside the parent one
  queries:
    # query name which you can use in the templates like {{Country}}
    - name: Country
      # css selector
      query: .country
      # you can select something specific from the query by providing a regex
      # this is a python regex with re.DOTALL enabled i.e. '.' captures '\n'
      # uses the first captured group
      # (defaults to null)
      regex: null
      # if true: we select every instance and iterate over them
      # if false: we only select the first one
      # basically it's querySelector() vs querySelectorAll()
      # (defaults to false)
      many: true
      children:
        - name: Question
          query: .country-info
          many: false
          regex: (Area .*)$
          children: null
        - name: Answer
          query: .country-name
          many: false
          regex: null
          children: null
```

## Usage in code

It is possible to use cardscraper as a library, but it is created to be used as a CLI application.

```py
import yaml
from cardscraper import (
    Config,
    generate_anki_package,
    select_function_by_step_and_name,
    write_package,
)
from genanki import Model, Note

if __name__ == '__main__':
    with open('/path/to/config.yaml', 'r') as f:
        config: Config = yaml.load(f, yaml.Loader)
    # or you can make a config manually

    get_model = select_function_by_step_and_name('model', 'default')
    get_deck = select_function_by_step_and_name('deck', 'default')
    get_package = select_function_by_step_and_name('package', 'default')

    def get_notes(config: Config, model: Model) -> list[Note]:
        notes = []
        ...
        return notes

    package, path = generate_anki_package(
        config, get_model, get_notes, get_deck, get_package
    )
    write_package(package, path)
```

## Plugin system

A plugin system is present in cardscraper. To expose your functions to cardscraper expose them in an entry point named `cardscraper.STEPNAME`.

This is how the default functions are exposed:

```toml
[project.entry-points.'cardscraper.model']
default = 'cardscraper.default:get_model'
[project.entry-points.'cardscraper.scraping']
default = 'cardscraper.default:get_notes'
[project.entry-points.'cardscraper.deck']
default = 'cardscraper.default:get_deck'
[project.entry-points.'cardscraper.package']
default = 'cardscraper.default:get_package'
```
