
import os
from PIL import Image

def resize_images_in_directory(input_dir, output_dir, size):
    """
    Resize all images in the input directory and save them to the output directory.

    Parameters:
    - input_dir : Path to the directory containing input images.
    - output_dir : Path to the directory where resized images will be saved.
    - size (tuple): Desired size of the output images in the format (width, height).
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over files in input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            input_image_path = os.path.join(input_dir, filename)
            output_image_path = os.path.join(output_dir, filename)
            resize_image(input_image_path, output_image_path, size)

def resize_image(input_image_path, output_image_path, size):
    """
    Resize the input image and save it to the output path.

    Parameters:
    - input_image_path (str): Path to the input image file.
    - output_image_path (str): Path to save the resized image.
    - size (tuple): Desired size of the output image in the format (width, height).
    """
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size)
    resized_image.save(output_image_path)

# Example usage:
input_dir = "input path of directory" # input path to directory
output_dir = "resized_images" # name of output directory
desired_size = (300, 200)  # Specify desired width and height

resize_images_in_directory(input_dir, output_dir, desired_size)
