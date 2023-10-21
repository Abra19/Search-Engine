import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text)

def search(docs, sample):
    if sample == '':
        return [doc['id'] for doc in docs]
    token = clean_text(sample)
    cleaned_docs = map(lambda doc: {**doc, 'text': clean_text(doc['text'])}, docs)
    return [doc['id'] for doc in cleaned_docs if token in doc['text'].split(' ')]
