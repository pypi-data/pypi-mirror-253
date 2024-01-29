import logging
import re

import requests
from bs4 import BeautifulSoup, Tag
from genanki import Model, Note

from cardscraper.config import Config, QueryDict


class Query:
    def __init__(
        self,
        name: str,
        query: str,
        many: bool = False,
        regex: str | None = None,
        children: list[QueryDict] | None = None,
    ) -> None:
        if children is None:
            children = []
        self.name = name
        self.query = query
        self.many = many
        self.regex = regex
        self.children = [Query(**child) for child in children]


def generate_notes_for_quote(
    tag: Tag,
    query: Query,
    model: Model,
    notes: list[Note] | None = None,
    info: dict | None = None,
) -> list[Note]:
    """
    Generates notes from a query tree.

    Args:
        tag (Tag): BeautifulSoup tag object to query in.
        query (Query): Query tree starting node.
        model (Model): Anki Model for the notes.
        notes (list[Note] | None): List of notes to return.
        info (dict | None): Dictionary of collected results.

    Returns:
        list[Note]: Generated notes.
    """
    if notes is None:
        notes = []
    if info is None:
        info = {}

    # this is a simplified way of how this function works
    # info = {}
    # for a in range(10):
    #     info['a'] = a
    #     for b in range(10):
    #         info['b'] = b
    #         for c in range(10):
    #             info['c'] = c
    #             make_note_from_info(info, ...)

    # info is a dictionary of query names to their values that will be used
    # to construct the field list for genanki.Note(...) in make_note_from_info.
    # it is a mutable shared state that is passed in further on each recursive
    # call where we store all evaluated query results.

    # there are two types of queries: 'many' and non 'many' queries
    # the difference is we have to loop over the 'many' queries
    selected_tags = tag.select(query.query)
    # non 'many' queries only get the first selected tag
    if not query.many and selected_tags:
        selected_tags = selected_tags[:1]

    for selected_tag in selected_tags:
        # here we regex the result if we need to
        if query.regex is not None:
            text = re.search(query.regex, selected_tag.text, re.DOTALL)
            if text is None:
                text = ''
            else:
                text = text.group(1)
            info[query.name] = text
        else:
            info[query.name] = selected_tag.text

        # we separate the two types of queries to ensure that 'many' ones are
        # processed last.
        # we need to do that because we need to have all the information
        # that will not be changed before we 'go down a level' and start
        # evaluating the results there.
        normal_queries = [q for q in query.children if not q.many]
        many_queries = [q for q in query.children if q.many]

        # this ensures that 'many' query will be processed last
        for child in normal_queries + many_queries:
            generate_notes_for_quote(selected_tag, child, model, notes, info)

        # if we are the last 'many' query that means we are at the end of the
        # loop and we need to make the note.
        if not many_queries and query.many:
            notes.append(make_note_from_info(info, model))

    return notes


def make_note_from_info(info: dict, model: Model) -> Note:
    """
    Creates a Note from the collected info.

    Args:
        info (dict): Collected info from queries.
        model (Model): Anki Model for the notes.

    Returns:
        Note: Constructed note.
    """
    model_field_names = [
        field_name for fd in model.fields for _, field_name in fd.items()
    ]
    fields_for_note = [info[field_name] for field_name in model_field_names]
    return Note(model, fields_for_note)


def validate_query_tree(query: Query) -> bool:
    """
    Validates that the query tree is correct.

    If there are multiple queries that we should loop over and they are not
    under each other (i.e. each 'many' query is not the sole 'many' child of a
    parent 'many' query) we have no idea how to loop over them.

    Args:
        query (Query): Query tree starting node.

    Returns:
        bool: Whether query tree is correct or not.
    """
    queries_with_many_under = [
        validate_query_tree(child) for child in query.children
    ].count(True)
    if queries_with_many_under > 1:
        raise ValueError(
            "Having two or more 'many' queries not "
            'under each other is undefined behavior.'
        )
    return query.many | bool(queries_with_many_under)


def get_notes(config: Config, model: Model) -> list[Note]:
    scraping_config = config['scraping']
    urls = scraping_config['urls']
    agent = scraping_config['agent']
    if agent is None:
        headers = {}
    else:
        headers = {'User-Agent': agent}

    queries = [Query(**child) for child in scraping_config['queries']]
    for query in queries:
        validate_query_tree(query)
    notes = []
    for url in urls:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        for query in queries:
            notes.extend(generate_notes_for_quote(soup, query, model))
    logger = logging.getLogger('cardscraper')
    logger.info('Generated notes!')
    return notes
