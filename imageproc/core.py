from PIL import Image

def load_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def resize_image(image, size):
    return image.resize(size)

def rotate_image(image, angle):
    return image.rotate(angle)

def to_grayscale(image):
    return image.convert("L")
