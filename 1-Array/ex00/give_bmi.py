import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """This function returns the bmi according to the weight and height given"""

    if(len(height) != len(weight)):
        ValueError("Lenghts of height and weight should be equal")
    try:
        height_pow = np.array(height)
        height_pow = np.power(height_pow, 2)
        bmi = np.array(len(height))
        bmi = np.divide(weight, height_pow)
    except Exception as e:
        print(f"Error : {e}")
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function tells wether or not a bmi is above a limit or not"""
    return (np.array(bmi) > limit).tolist()