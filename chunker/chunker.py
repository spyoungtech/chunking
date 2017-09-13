def split(iterable, sentinel):
    """Works like str.split, but with any arbitrary iterable"""
    x = iter(iterable)
    for item in x:
        chunk = []
        while item != sentinel:
            chunk.append(item)
            item = next(x)
        yield chunk

def chunk(iterable, chunk_size):
    """Yield successive n-sized chunks from l."""
    x = iter(iterable)
    for item in x:
        yield (item, *(next(x) for _ in range(chunk_size - 1)))

