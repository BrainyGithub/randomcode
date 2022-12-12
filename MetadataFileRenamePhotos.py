import os
import re

# Set the directory containing the files to be renamed
directory = "pic3"

# Get a list of all files in the directory
files = os.listdir(directory)

# Compile a regular expression pattern to match dd-mm-yyyy date strings
date_pattern = re.compile(r"\d{2}-\d{2}-\d{4}")

# Iterate over the files in the directory
for file in files:
    # Get the file name and extension
    name, ext = os.path.splitext(file)

    # Use the regular expression to find the dd-mm-yyyy date string in the file name
    match = date_pattern.search(name)

    # If a match is found, use the matched string as the new file name
    if match:
        new_name = match.group() + ext

        # Check if the new file name already exists in the directory
        if os.path.exists(os.path.join(directory, new_name)):
            # If it does exist, append a number to the end of the file name
            # to make it unique
            i = 1
            while True:
                new_name = match.group() + "_" + str(i) + ext
                if not os.path.exists(os.path.join(directory, new_name)):
                    break
                i += 1

        # Rename the file
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
