import cv2
from zoom import ft_zoom
import matplotlib.pyplot as plt



def ft_load(path: str) -> list:

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Only JPG and JPEG formats are supported")

    im = cv2.imread(path)
    if im is None:
        raise ValueError("Cannot load image")

    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    
    return im

def main():

    try:
        image = ft_load("animal.jpeg")
        print("The shape of the image is ", image.shape)
        print(image)

        new_image = ft_zoom(image)
        print("New shape after slicing:", new_image.shape)
        print(new_image)

        fig, ax = plt.subplots()
        ax.imshow(new_image)
        plt.show()
    except (ValueError, TypeError) as e:
        print("Error:", e)


if __name__== "__main__":
    main()