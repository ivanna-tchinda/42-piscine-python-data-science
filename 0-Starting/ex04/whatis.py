import sys

def whatis():
  try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    arg = sys.argv[1]
    assert arg.isdigit(), "argument is not an integer"
    if arg % 2 == 0:
      print("I'm Even.")
    else:
      print("I'm Odd.")
  except AssertionError as error:
    print("AssertionError:", error)
  return 0

whatis()