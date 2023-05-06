def main(list1):
    """
    A list of several elements is given. Reverse this list.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    list1.reverse()
    return list1

v = main([1, 2, 3, 4, 5])
print(v)