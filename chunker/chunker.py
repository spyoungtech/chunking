def _iter(iterable, sentinel):
    x = iter(iterable)
    for item in x:
        yield item
    yield sentinel


def split(iterable, sentinel):
    """
    Split any arbitrary iterable into list items separated by a sentinel value.
    :param iterable: any iterable
    :param sentinel: value to split on
    :returns: a list of chunks
    >>> a_list = ["foo", 'bar', 'SENTINEL', 'bacon', 'eggs']
    >>> split(a_list, 'SENTINEL')
    [['foo', 'bar'], ['bacon', 'eggs']]
    """
    return list(iter_split(iterable, sentinel))

def iter_split(iterable, sentinel):
    """
    Split any arbitrary iterable into list items separated by a sentinel value.

    :param iterable: any iterable
    :param sentinel: value to split on
    :yields: chunks
    """
    x = _iter(iterable, sentinel)
    for item in x:
        chunk = []
        while item != sentinel:
            chunk.append(item)
            item = next(x)
        yield chunk

def chunk(iterable, chunk_size):
    """
    Yield successive n-sized chunks from an iterable.
    If the iterable does not fit evenly into chunk_size, the last chunk will be smaller than chunk_size.
    >>> r = range(5)
    >>> for c in chunk(r, 2):
    ...     print(a, b)
    (0, 1)
    (2, 3)
    (4,)
    """
    x = iter(iterable)
    for item in x:
        yield (item, *(next(x) for _ in range(chunk_size - 1)))
