def ft_zoom(image: list) -> list:
    middle_row_image = len(image) // 2
    middle_column_image = len(image[0]) // 2
    new_image = image[middle_row_image - 200:middle_row_image + 200, middle_column_image - 200:middle_column_image +200]
    print("New image",new_image)
    return new_image