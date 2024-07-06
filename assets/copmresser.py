from PIL import Image
import os

def resize_image(image_path, output_path, size, quality):
    # Open an image file
    with Image.open(image_path) as image:
        # Save as JPEG
        new_image = image.resize((size, size))
        new_image.save(output_path, 'JPEG', optomize=True, quality=quality)
def compress_image(image_path, output_path, quality):
    # Open an image file
    with Image.open(image_path) as image:
        # Save as JPEG
        image.save(output_path, 'JPEG', optomize=True, quality=quality)

for file in os.listdir('full'):
    image_path = f'backup/{file}'
    output_path = f'100/{file}'
    compress_image(image_path, output_path, quality=95)
    #resize_image(image_path, output_path, size=250, quality=95)
