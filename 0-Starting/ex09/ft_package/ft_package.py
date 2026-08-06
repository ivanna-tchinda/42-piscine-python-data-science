def count_in_list(lst, item):
    """Count the number of occurrences of an item in a list"""
    count = 0

    for element in lst:
        if element == item:
            count += 1

    return count