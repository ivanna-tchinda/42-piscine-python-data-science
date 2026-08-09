import cv2
from rotate import ft_rotate
import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> list:

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Only JPG and JPEG formats are supported")

    im = cv2.imread(path)
    if im is None:
        raise ValueError("Cannot load image")

    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    return im

def main():

    try:
        image = ft_load("animal.jpeg")
        print("The shape of the image is ", image.shape)
        print(image)

        new_image = np.array(ft_rotate(image))
        print("New shape after transpose:", new_image.shape)
        print(new_image)

        fig, ax = plt.subplots()
        ax.imshow(new_image, cmap="gray")
        plt.show()
    except (ValueError, TypeError) as e:
        print("Error:", e)


if __name__== "__main__":
    main()