import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """This function prints the shape of a list and returns the new version considering a start and an end variable"""


    if not isinstance(family, list):
        raise ValueError("You should enter a list")
    
    if(len(family) == 0):
        raise ValueError("Array should not be empty")

    if not all(isinstance(tab, list) for tab in family):
        raise ValueError("Array should be 2D")

    len_tab = len(family[0])
    for tab in family:
        if(len(tab) != len_tab):
            raise ValueError("lenghts of arrays are not equal")

    family = np.array(family)
    print("My shape is", family.shape)

    new_version = family[start:end]

    print("My new shape is", new_version.shape)

    return new_version.tolist()