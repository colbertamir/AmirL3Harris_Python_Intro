import os
import shutil

folder = "Images"

files = os.listdir(folder)

for file in files:
    if file.startswith("person"):
        destination = os.path.join(folder, "Person")

    elif file.startswith("animal"):
        destination = os.path.join(folder, "Animal")

    elif file.startswith("fruit"):
        destination = os.path.join(folder, "Fruit")

    else:
        continue

    os.makedirs(destination, exist_ok=True)

    source = os.path.join(folder, file)

    shutil.move(source, destination)

