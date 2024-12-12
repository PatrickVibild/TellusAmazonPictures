import os
from shutil import copyfile

def organize_images(source_image, total_images, output_dir):
    """
    Create copies of the source image and organize them into a single folder.

    Parameters:
    - source_image: Path to the original image.
    - total_images: Total number of images to create.
    - output_dir: Root directory to store the organized images.
    """
    if not os.path.exists(source_image):
        print(f"Source image '{source_image}' not found!")
        return

    # Create the root output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, total_images + 1):
        # Construct the target file name
        target_filename = f"{i}.ps0.jpg"
        target_path = os.path.join(output_dir, target_filename)

        # Copy the source image to the target path
        copyfile(source_image, target_path)

    print(f"Organized {total_images} images into a single folder in '{output_dir}'")

# Example usage
source_image_path = "Label.jpg"  # Path to the source image
total_images = 1054               # Total number of images to create
output_directory = "/Users/patrickvibild/repo/TellusAmazonPictures/pictures/safety/all_images" # Root directory for output

organize_images(source_image_path, total_images, output_directory)
