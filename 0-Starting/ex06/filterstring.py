import sys
from ft_filter import ft_filter

def filterstring(words_list, integer):
    """This function filter the string provided by the lenght of the words specified by the integer"""
    splitted_list = words_list.split(' ')
    new_list = [word for word in ft_filter(lambda a : len(a)>= integer, splitted_list)]
    print(new_list)

def valid_string(str_1):
    """This function checks if the argument is a valid string"""
    for char in str_1:
        if char.isalpha() == False and char != ' ':
            return False
    return True

def isint(strint):
    """This function checks if the int provided is valid"""
    sign = False
    for char in strint:
        if char == '-' and sign == False:
            sign = True
            continue
        if char.isdigit():
            continue
        else:
            return False
    return True

def main():
    """This is the main function"""
    try:
        assert len(sys.argv) == 3, "you should enter 2 arguments"
        assert valid_string(sys.argv[1]), "first argument must be a string, with spaces only"
        assert isint(sys.argv[2]), "second argument must be an integer"
        filterstring(sys.argv[1], int(sys.argv[2]))
    except AssertionError as error:
        print("Assertion error:", error)

if __name__ == "__main__":
    main()