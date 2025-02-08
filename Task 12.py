def apply_grayscale_filter(image):
    for row in range(len(image)):
        for col in range(len(image[0])):
            r, g, b = image[row][col]
            gray = int((r + g + b) / 3)
            image[row][col] = [gray, gray, gray]
    return image


image = [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 0]]]
grayscale_image = apply_grayscale_filter(image)
print("Grayscale Image:", grayscale_image)