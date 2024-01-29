import bs4
import pytest
from cardscraper.default.scraping import (
    Query,
    generate_notes_for_quote,
    validate_query_tree,
)
from genanki import Model, Note


def test_validate():
    root_query = Query('root', '.test', many=True)
    a_query = Query('childa', '.test', many=True)
    b_query = Query('childb', '.test', many=False)
    b1_query = Query('childbb', '.test', many=False)

    root_query.children = [a_query, b_query]
    b_query.children = [b1_query]

    assert validate_query_tree(root_query)

    b1_query.many = True
    with pytest.raises(ValueError):
        validate_query_tree(root_query)


PAGE = """
<table>
    <tbody>
        <tr>
            <td class='question'>Q1</td>
            <td class='answer'>A1</td>
        </tr>
        <tr>
            <td class='question'>Q2</td>
            <td class='answer'>A2</td>
        </tr>
    </tbody>
</table>
<table>
    <tbody>
        <tr>
            <td class='question'>Q3</td>
            <td class='answer'>A3</td>
        </tr>
        <tr>
            <td class='question'>Q4</td>
            <td class='answer'>A4</td>
        </tr>
    </tbody>
</table>
"""


def test_generating():
    model = Model(
        model_id=3211,
        name='Model Name',
        templates=[{'name': 'Hi', 'afmt': 'Hello', 'qfmt': 'Hiii'}],
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
    )
    soup = bs4.BeautifulSoup(PAGE, 'html.parser')
    table_query = Query('Table', 'table', True)
    row_query = Query('Row', 'tr', True)
    question_query = Query('Question', '.question', False)
    answer_query = Query('Answer', '.answer', False)

    table_query.children = [row_query]
    row_query.children = [question_query, answer_query]

    notes = generate_notes_for_quote(soup, table_query, model)
    expected = [
        Note(model, ['Q1', 'A1']),
        Note(model, ['Q2', 'A2']),
        Note(model, ['Q3', 'A3']),
        Note(model, ['Q4', 'A4']),
    ]
    assert [note.guid for note in notes] == [note.guid for note in expected]
