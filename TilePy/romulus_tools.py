def remove_newlines(x):
    """

    :param x: list
    """
    for y in x:
        if y == "\n":
            x.remove(x[x.index(y)])
    return x
