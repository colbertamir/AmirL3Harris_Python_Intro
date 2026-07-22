# Amir Colbert L3Harris Python Intro

## Hello!

This a python project intended to display my basic professional coding abilities. 
This project contains a program that organizes image data by filename.
I will break down the program step by step.

### Step 1: Create a folder or locate the folder that contains the images

Images/

- example1.jpg
- example2.jpg
- example3.jpg

### Step 2: Import your libraries

```python
import os
import shutil
```

#### os: Works with folders

- List directories/folders: `os.listdir()`
- Creates a directory/folder: `os.mkdir()`
- Creates a valid file path, connects things: `os.path.join`

#### shutil: Copies and moves things (shutil = shuttle, which also moves things.. get it?)

`shutil.move()`

### Step 3: Locate the images

`folder = "Images"`

### Step 4: Read every file

`files = os.listdir(folder)`

### Step 5: Loop through every file

`for file in files:`

### Step 6: Check what each filename starts with

```python
if file.startswith("person"):
        destination = os.path.join(folder, "Person")

    elif file.startswith("animal"):
        destination = os.path.join(folder, "Animal")

    elif file.startswith("fruit"):
        destination = os.path.join(folder, "Fruit")

    else:
        continue
```

Essentially this block of code above is taking the image file that starts with the string "person" for example, and joining the file path from the original folder to a new folder named "Person' as specified in `(folder, Person)` . In this block the process is repeated with `elif` to find the specific images and sort them accordingly. If it cannot find the information specified the program continues, leaving whatever random image data in the original folder.

### Step 7: Create folders

`os.makedirs(destination, exist_ok=True)`

This function only creates the appropriate folders when needed.

### Step 8: Move images

```python
source = os.path.join(folder, file)

shutil.move(source, destination)
```

This block of code completes the program taking the images from the source or original folder and placing it in a new destination.

Thank you for your consideration!

![Company Logo](Images/logo.jpg)
