import os
import cv2
import numpy as np
import random


def add_noise(image):
    """Add subtle Gaussian noise to an image (unnoticeable to humans)."""
    row, col, ch = image.shape
    mean = 0
    sigma = random.uniform(2, 5)  # Subtle noise level (small sigma)
    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype(np.float32)
    noisy = np.clip(image + gauss, 0, 255).astype(np.uint8)  # Ensure pixel values are valid
    return noisy


def rotate_image(image):
    """Rotate the image by a random angle and add a white background."""
    angle = random.uniform(-180, 180)  # Random rotation between -30 and 30 degrees
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Calculate the rotation matrix and expanded bounds
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    abs_cos = abs(matrix[0, 0])
    abs_sin = abs(matrix[0, 1])

    new_w = int(h * abs_sin + w * abs_cos)
    new_h = int(h * abs_cos + w * abs_sin)

    # Adjust rotation matrix to account for translation
    matrix[0, 2] += (new_w / 2) - center[0]
    matrix[1, 2] += (new_h / 2) - center[1]

    # Rotate and add a white background
    rotated = cv2.warpAffine(image, matrix, (new_w, new_h), borderValue=(255, 255, 255))
    return rotated


def scale_image(image):
    """Scale the resolution of the image by a random factor."""
    scale_factor = random.uniform(0.7, 1.3)  # Random scaling between 0.8x and 1.2x
    height, width = image.shape[:2]
    new_dim = (int(width * scale_factor), int(height * scale_factor))
    scaled = cv2.resize(image, new_dim, interpolation=cv2.INTER_LINEAR)
    return scaled


def augment_images(input_folder, output_folder):
    """Perform random noise, rotation, and scaling augmentation on all images."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files matching the pattern *.ps0*.jpg
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") and "ps0" in filename:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Read the image
            image = cv2.imread(input_path)
            if image is None:
                print(f"Failed to load {filename}")
                continue

            # Apply augmentations
            noisy_image = add_noise(image)
            rotated_image = rotate_image(noisy_image)
            scaled_image = scale_image(rotated_image)

            # Save the augmented image
            cv2.imwrite(output_path, scaled_image)
            print(f"Saved augmented image: {output_path}")


# Example usage
input_folder = "/Users/patrickvibild/repo/TellusAmazonPictures/pictures/safety/all_images"  # Folder containing original images
output_folder = os.path.join(input_folder, "augment")  # Subfolder for augmented images

augment_images(input_folder, output_folder)
