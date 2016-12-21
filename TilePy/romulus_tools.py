def remove_newlines(x):
    """
    .. py:function:: remove_newlines(x)
    Extract newlines from a list.
    :param x: list of characters
    :rtype: list of characters
    """
    for y in x:
        if y == "\n":
            x.remove(x[x.index(y)])
    return x
