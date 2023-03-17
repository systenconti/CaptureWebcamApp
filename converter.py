from PIL import Image
 
 
def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    with Image.open(input_image) as img:
        return img.convert(mode="L")