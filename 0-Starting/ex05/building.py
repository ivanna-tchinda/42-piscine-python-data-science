import sys

def count_char_types(arg):
  """This function counts the number of each type of character"""
  lower_case_count = 0
  upper_case_count = 0
  punctuation_count = 0
  digit_count = 0
  spaces_count = 0

  for char in arg:
    if char.islower():
      lower_case_count += 1
    elif char.isupper():
      upper_case_count += 1
    elif char.isdigit():
      digit_count += 1
    elif char.isspace():
      spaces_count += 1
    else:
      punctuation_count += 1

  total_chacacters = upper_case_count + lower_case_count + punctuation_count + spaces_count + digit_count
  
  print(total_chacacters, "characters")
  print(upper_case_count, "upper letters")
  print(lower_case_count,"lower letters")
  print(punctuation_count, "punctuation marks")
  print(spaces_count, "spaces")
  print(digit_count, "digits")

def ask_prompt():
  """This function is triggered when there is one argument missing in the stdin"""
  print("What is the text to count?")
  prompt = ""
  try:
    for line in sys.stdin:
      prompt += line
  except KeyboardInterrupt:
    exit(0)
  count_char_types(prompt)
      
def main():
  """This is the main function"""
  try:
    assert len(sys.argv) <= 2, "you must provide exactly one string argument"
    if(len(sys.argv) == 1):
      return ask_prompt()
    arg = sys.argv[1]
    count_char_types(arg)
    print(main.__doc__)
    

  except AssertionError as error:
    print("AssertionError:", error)

if __name__ == "__main__":
    main()