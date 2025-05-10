from imageproc import (
    load_image, save_image, resize_image, rotate_image,
    to_grayscale, apply_blur, apply_sharpen, show_image
)

img = load_image("example.jpg")
img = resize_image(img, (300, 300))
img = rotate_image(img, 45)
img = to_grayscale(img)
img = apply_sharpen(img)

show_image(img)
save_image(img, "processed_example.jpg")
