import numpy as np

def ft_rotate(image: list) -> list:

    middle_row_image = len(image) // 2
    middle_column_image = len(image[0]) // 2
    new_image = image[middle_row_image - 200:middle_row_image + 200, middle_column_image - 200:middle_column_image +200]
    
    transposed_array = []
    for j in range(len(new_image[0])):
        row = []
        for i in range(len(new_image)):
            row.append(new_image[i][j])
        transposed_array.append(row)

    return transposed_array