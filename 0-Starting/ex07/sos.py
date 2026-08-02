import sys

NESTED_MORSE = {
    " " : "/ ",
    "A" : ".- ",
    "B" : "-... ",
    "C" : "-.-. ",
    "D" : "-.. ",
    "E" : ". ",
    "F" : "..-. ",
    "G" : "--. ",
    "H" : ".... ",
    "I" : ".. ",
    "J" : ".--- ",
    "K" : "-.- ",
    "L" : ".-.. ",
    "M" : "-- ",
    "N" : "-. ",
    "O" : "--- ",
    "P" : ".--. ",
    "Q" : "--.- ",
    "R" : ".-. ",
    "S" : "... ",
    "T" : "- ",
    "U" : "..- ",
    "V" : "...- ",
    "W" : ".-- ",
    "X" : "-..- ",
    "Y" : "-.-- ",
    "Z" : "--.. ",
    "0" : "----- ",
    "1" : ".---- ",
    "2" : "..--- ",
    "3" : "...-- ",
    "4" : "....- ",
    "5" : "..... ",
    "6" : "-.... ",
    "7" : "--... ",
    "8" : "---.. ",
    "9" : "----. ",
}

def valid_string(str_1):
    """This function checks if the argument is a valid string"""
    for char in str_1:
        if char.isalnum() == False and char != ' ' or ord(char) > 122:
            return False
    return True

def convert_to_morse(str_1):
    """This function converts a string to morse code"""
    converted_string = ''
    for char in str_1:
        if(char.isalpha()):
            char = char.upper()
        converted_string += NESTED_MORSE[char]
    return converted_string

def main():
    """This is the main function"""
    try:
        assert len(sys.argv) == 2, "you should enter 1 argument"
        assert valid_string(sys.argv[1]), "argument must be a string, with spaces or letters"
        print(convert_to_morse(sys.argv[1]).strip())
    except AssertionError as error:
        print("Assertion error:", error)

if __name__ == "__main__":
    main()