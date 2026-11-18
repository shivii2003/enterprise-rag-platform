def retrieve(query, docs):
    terms=set(query.lower().split())
    return sorted(docs,key=lambda d:len(terms & set(d['text'].lower().split())),reverse=True)
