import sys

def words_with_letter_a(word):
    if "a" in word:
        return True
    return False

def words_with_6_lettes(word):
    if len(word) >= 6:
        return True
    return False

def ft_filter(list_1, func):
    newlist = [w for w in list_1 if func(w)]
    return newlist


def main():
    list_1 = ["apple", "banana", "eee", "cucumber", "cashew"]
    func_1 = words_with_letter_a
    func_2 = words_with_6_lettes

    print("first list: ", list_1)

    newlist = ft_filter(list_1, func_1)
    print("filtered by letter a:", newlist)

    newlist = ft_filter(list_1, func_2)
    print("filtered by length:", newlist)

if __name__ == "__main__":
    main()