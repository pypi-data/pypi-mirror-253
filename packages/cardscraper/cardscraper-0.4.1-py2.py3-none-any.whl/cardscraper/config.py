from typing import TypedDict


class MetaConfig(TypedDict):
    model: str
    scraping: str
    deck: str
    package: str


class DeckConfig(TypedDict):
    id: int
    name: str


class NoteTemplate(TypedDict):
    name: str
    afmt: str
    qfmt: str


class ModelConfig(TypedDict):
    id: int
    name: str
    templates: list[NoteTemplate]
    css: str


class QueryDict(TypedDict):
    name: str
    query: str
    many: bool
    regex: str | None
    children: list['QueryDict']


class ScrapingConfig(TypedDict):
    urls: list[str]
    agent: str | None
    queries: list[QueryDict]


class PackageConfig(TypedDict):
    name: str
    output: str
    media: str | None
    pattern: str


class Config(TypedDict):
    """
    YAML input file example with explanations: ::

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
              # this is a python regex with re.DOTALL enabled i.e. '.' captures '\\n'
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
    """  # noqa: E501

    meta: MetaConfig
    model: ModelConfig
    scraping: ScrapingConfig
    deck: DeckConfig
    package: PackageConfig


def set_config_defaults(config: Config) -> Config:
    """
    Sets default values for a config.

    NOTE: Mutates the config!

    Args:
        config (Config): Config to set the defaults of.

    Returns:
        Config: The same config that was passed in.
    """
    model_config = config['model']
    model_config.setdefault('css', '')

    package_config = config['package']
    package_config.setdefault('output', '.')
    package_config.setdefault('media', None)
    package_config.setdefault('pattern', '**/*.*')

    scraping_config = config['scraping']
    scraping_config.setdefault('agent', None)

    return config
