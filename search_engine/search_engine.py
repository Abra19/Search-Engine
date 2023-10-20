def search(docs, sample):
  if sample == '':
    return [doc['id'] for doc in docs]
  return [doc['id'] for doc in docs if sample in doc['text'].split(' ')]