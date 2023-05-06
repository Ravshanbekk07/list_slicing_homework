def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    list1.reverse()
    return  list1[:n]

v = main(['a', 'b', 'c', 'd', 'e', 'f'],3)
print(v)