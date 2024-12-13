import os

def rename_images():
    # Get a list of all files in the current directory
    files = os.listdir('.')

    # Iterate through the files
    for file_name in files:
        # Check if the file name matches the pattern
        if file_name.endswith('.ps0.jpg'):
            # Create the new file name
            new_file_name = file_name.replace('.ps0.jpg', '.ps01.jpg')

            # Rename the file
            os.rename(file_name, new_file_name)
            print(f'Renamed: {file_name} -> {new_file_name}')

if __name__ == "__main__":
    rename_images()
