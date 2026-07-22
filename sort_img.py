import os # Lets us work with files and folders
import shutil # Lets us move files

folder = "Images" # The folder containing the image files

files = os.listdir(folder) # Get a list of all files in the folder

for file in files: # Loops through each file
    if file.startswith("person"): # Check if the filename starts with "person", same for other images
        destination = os.path.join(folder, "Person") # Destination folder for "Person", same for the other images

    elif file.startswith("animal"):
        destination = os.path.join(folder, "Animal")

    elif file.startswith("fruit"):
        destination = os.path.join(folder, "Fruit")

    else:
        continue # Skips the files that don't fit into any category

    os.makedirs(destination, exist_ok=True) # Creates the folder(s) if it doesn't already exist

    source = os.path.join(folder, file) # Path to current file

    shutil.move(source, destination) # Moves the file into the appropriate folder(s)
