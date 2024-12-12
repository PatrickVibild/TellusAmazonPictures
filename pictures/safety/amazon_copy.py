import os
from shutil import copyfile

def organize_images(source_image, total_images, output_dir):
    """
    Create copies of the source image and organize them into folders.

    Parameters:
    - source_image: Path to the original image.
    - total_images: Total number of images to create.
    - output_dir: Root directory to store the organized folders.
    """
    if not os.path.exists(source_image):
        print(f"Source image '{source_image}' not found!")
        return

    # Create the root output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, total_images + 1):
        # Determine folder number (1-based index)
        folder_number = (i - 1) // 100 + 1
        folder_path = os.path.join(output_dir, str(folder_number))

        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Construct the target file name
        target_filename = f"{i}.ps0.jpg"
        target_path = os.path.join(folder_path, target_filename)

        # Copy the source image to the target path
        copyfile(source_image, target_path)

    print(f"Organized {total_images} images into folders in '{output_dir}'")

# Example usage
source_image_path = "Label.jpg"  # Path to the source image
total_images = 1054               # Total number of images to create
output_directory = "/Users/patrickvibild/repo/TellusAmazonPictures/pictures/safety/images" # Root directory for output

organize_images(source_image_path, total_images, output_directory)
