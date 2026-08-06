import numpy

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    height_pow = [x**2 for x in height]
    bmi = []
    for h in range(len(height)):
        bmi.append(weight[h]/height_pow[h])
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = [True if x > limit else False for x in bmi]
    return res



#checker les exceptions

def main():
  """This is the main function"""
  try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
  except AssertionError as error:
    print("AssertionError:", error)

if __name__ == "__main__":
    main()