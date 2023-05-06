def main(list1, n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1.reverse()
    return list1[::n]


v = main(['a', 1, 'b', 2, 'c', 3, 'd', 4], 2)
print(v)
