import re


def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()


def search(docs, sample):
    if sample == '':
        return [doc['id'] for doc in docs]

    token = clean_text(sample)
    cleaned_docs = map(
        lambda doc: {**doc, 'text': clean_text(doc['text'])}, docs
    )

    result = (
        (doc['id'], doc['text'].split(' ').count(token)) for doc in cleaned_docs
    )
    sorted_result = sorted(result, key=lambda el: el[1], reverse=True)

    return [el for el, count in sorted_result if count != 0]
