def diff(first=[], second=[], preserve_order=True):
    """Compute the difference between two lists.

    Args:
       first (list):  The name to use.
       second (list):  The name to use.
       preserve_order (bool): 

    Returns:
       list.  List of elements present only in the first list.
    """
    if not preserve_order:
        first = set(first)
        second = set(second)
    return [item for item in first if item not in second]
