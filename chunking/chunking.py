def _iter(iterable, sep):
    x = iter(iterable)
    for item in x:
        yield item
    yield sep


def split(iterable, sep):
    """
    Split any arbitrary iterable into list items separated by a sep value.
    :param iterable: any iterable
    :param sep: value to split on
    :returns: a list of chunks
    >>> a_list = ["foo", 'bar', 'SEP', 'bacon', 'eggs']
    >>> split(a_list, 'SEP')
    [['foo', 'bar'], ['bacon', 'eggs']]
    """
    return list(iter_split(iterable, sep))

def iter_split(iterable, sep):
    """
    Split any arbitrary iterable into list items separated by a sep value. Generator used by split
    :param iterable: any iterable
    :param sep: value to split on
    :yields: chunks
    >>> from chunking import iter_split
    >>> a_list = ["foo", 'bar', 'SEP', 'bacon', 'eggs']
    >>> for c in iter_split(a_list, 'SEP'):
    ...     print(c)
    ...
    ['foo', 'bar']
    ['bacon', 'eggs']
    """
    x = _iter(iterable, sep)
    for item in x:
        chunk = []
        while item != sep:
            chunk.append(item)
            item = next(x)
        yield chunk


def chunk(iterable, chunk_size):
    """
    Yield successive n-sized chunks from an iterable.
    If the iterable does not fit evenly into chunk_size, the last chunk will be smaller than chunk_size.
    :param iterable: any iterable
    :param chunk_size: size of chunks
    >>> r = range(5)
    >>> for c in chunk(r, 2):
    ...     print(c)
    (0, 1)
    (2, 3)
    (4,)
    """
    x = iter(iterable)
    for item in x:
        yield (item, *(next(x) for _ in range(chunk_size - 1)))
