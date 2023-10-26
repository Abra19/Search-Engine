import math
import re


def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()


def make_index(text, index):
    cleaned_texts = clean_text(text).split(' ')
    length = len(cleaned_texts)
    result = {}
    for el in cleaned_texts:
        tf = cleaned_texts.count(el) / length
        result[el] = [(index, tf)]
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

    length = len(docs)
    token_params = []
    for token in tokens:
        token_index = index.get(token, [])
        docs_count = len(token_index)
        idf = math.log2(1 + (length - docs_count + 1) / (docs_count + 0.5))
        token_params.extend([(id, tf * idf) for (id, tf) in token_index])

    result = {}
    for (id, params) in token_params:
        result[id] = result.get(id, 0) + params

    sorted_result = sorted(
        result.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return [key for (key, _) in sorted_result]
