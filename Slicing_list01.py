def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    
    return numbers[0::2]
v = main([0, 1, 2, 3, 4, 5])
print(v)