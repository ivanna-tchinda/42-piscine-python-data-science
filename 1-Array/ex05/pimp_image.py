import matplotlib.pyplot as plt
import numpy as np

def ft_invert(array: list) -> list:
    """This function inverts the colors of an image"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            for k in range(3):
                array[i][j][k] = 255 - array[i][j][k]

    new_image = np.array(array)

    print("The shape of the image is ", new_image.shape)
    fig, ax = plt.subplots()
    ax.imshow(new_image, cmap="gray")
    plt.show()
    return new_image

#your code here
def ft_red(array: list) -> list:
    """This function display the image in red"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j][1] = 0
            array[i][j][2] = 0

    new_image = np.array(array)

    print("The shape of the image is ", new_image.shape)
    fig, ax = plt.subplots()
    ax.imshow(new_image)
    plt.show()
    return new_image


def ft_green(array: list) -> list:
    """This function display the image in green"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j][0] = 0
            array[i][j][2] = 0

    new_image = np.array(array)

    print("The shape of the image is ", new_image.shape)
    fig, ax = plt.subplots()
    ax.imshow(new_image)
    plt.show()
    return new_image
    

def ft_blue(array: list) -> list:
    """This function display the image in blue"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j][0] = 0
            array[i][j][1] = 0

    new_image = np.array(array)

    print("The shape of the image is ", new_image.shape)
    fig, ax = plt.subplots()
    ax.imshow(new_image)
    plt.show()
    return new_image


def ft_grey(array: list) -> list:
    """This function display the image in grey"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            grey = (array[i][j][0] / 3 + array[i][j][1] / 3 + array[i][j][2] / 3 )
            array[i][j][0] = grey
            array[i][j][1] = grey
            array[i][j][2] = grey

    new_image = np.array(array)

    print("The shape of the image is ", new_image.shape)
    fig, ax = plt.subplots()
    ax.imshow(new_image)
    plt.show()
    return new_image