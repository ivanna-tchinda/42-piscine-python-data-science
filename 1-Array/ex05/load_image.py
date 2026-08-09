import cv2
from pimp_image import ft_invert



def ft_load(path: str) -> list:

    if not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("Only JPG and JPEG formats are supported")

    im = cv2.imread(path)
    if im is None:
        raise ValueError("Cannot load image")

    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        
    
    return im
