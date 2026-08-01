import sys

def valid_length(word, integer):
    list1 = list(map(word, lambda a : len(a) >= integer))
    return list1

def filterstring(words_list, integer):
    splitted_list = words_list.split(' ')
    new_list = [word for word in splitted_list if valid_length(word, integer)]
    print(splitted_list)

def valid_string(str_1):
    """This function checks if the argument is a valid string"""
    for char in str_1:
        if char.isalpha() == False and char != ' ':
            return False
    return True

def main():
    """This is the main function"""
    try:
        print(filter.__doc__)
        assert len(sys.argv) == 3, "you should enter 2 arguments"
        assert valid_string(sys.argv[1]), "first argument must be a string, with spaces only"
        assert sys.argv[2].isdigit(), "second argument must be an integer"
        filterstring(sys.argv[1], int(sys.argv[2]))
    except AssertionError as error:
        print("Assertion error:", error)

if __name__ == "__main__":
    main()