import re
from functools import reduce


def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()


def make_index(text, index):
    cleaned_texts = clean_text(text).split(' ')
    result = {}
    for el in cleaned_texts:
        result[el] = result.get(el, []) + [index]
    return result


def search(docs, sample):
    if sample == '':
        return [doc['id'] for doc in docs]

    tokens = clean_text(sample).split(' ')

    index = {}
    for doc in docs:
        current = make_index(doc['text'], doc['id'])
        index = {
            key: index.get(key, []) + current.get(key, [])
            for key in set(index.keys()).union(current.keys())
        }

    meets = reduce(lambda acc, token: [*acc, *index.get(token, [])], tokens, [])
    frequencies = [(meet, meets.count(meet)) for meet in set(meets)]
    return [
        el[0]
        for el in sorted(frequencies, key=lambda el: el[1], reverse=True)
    ]
