import re
from collections import defaultdict


def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()


def make_dict(text):
    cleaned_texts = clean_text(text).split(' ')
    word_count = defaultdict(int)
    for word in cleaned_texts:
        word_count[word] += 1
    return word_count


def count_words_in_text(text, words):
    dictionary = {word: text['text'][word] for word in words}
    values = dictionary.values()
    return (min(values), sum(values))


def search(docs, sample):
    if sample == '':
        return [doc['id'] for doc in docs]

    token_dict = make_dict(sample)
    docs_dict = map(
        lambda doc: {**doc, 'text': make_dict(doc['text'])}, docs
    )

    doc_infos = map(
        lambda el: (el['id'], *count_words_in_text(el, token_dict)),
        docs_dict
    )
    filtered = filter(lambda el: el[2] != 0, list(doc_infos))
    sorted_all = sorted(list(filtered), key=lambda el: el[2], reverse=True)
    return [el[0] for el in sorted_all]
