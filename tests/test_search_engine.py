import pytest
from search_engine.search_engine import search


@pytest.fixture
def docs():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."
    return [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]


def test_search_positive(docs):
    expected = ['doc2', 'doc1']
    assert search(docs, 'shoot') == expected


def test_search_empty(docs):
    expected = ['doc1', 'doc2', 'doc3']
    assert search(docs, '') == expected


def test_search_in_empty(docs):
    expected = []
    assert search([], 'text') == expected


def test_search_negative(docs):
    expected = []
    assert search(docs, 'mum') == expected


def test_search_with_punctuation(docs):
    expected1 = ['doc1']
    expected2 = ['doc2']
    assert search(docs, 'pint!') == expected1
    assert search(docs, 'pint') == expected1
    assert search(docs, 'me.') == expected2
    assert search(docs, 'me') == expected2


def test_search_sentence(docs):
    expected = ['doc2', 'doc1']
    assert search(docs, 'shoot at me') == expected
