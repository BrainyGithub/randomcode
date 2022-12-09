import os

# the folder to read files from
folder = 'photos'

# get the list of files in the folder
files = os.listdir(folder)

# iterate over the list of files
for f in files:
    # get the full path of the file
    file_path = os.path.join(folder, f)

    # extract the date from the file name
    date = f.split('@')[1].split('2021')[0].split('2022')[0]

    # add "2022" or "2021" to the file name if it was found in the original name
    if '2022' in f:
        date += '2022'
    elif '2021' in f:
        date += '2021'

    # keep the ".jpg" extension of the file
    if date.endswith('.jpg'):
        new_path = os.path.join(folder, date)
    else:
        new_path = os.path.join(folder, date + '.jpg')

    # add a number to the file name if it already exists
    if os.path.exists(new_path):
        # initialize the numbering system
        i = 1

        # keep incrementing the number until you find a file name that does not exist
        while os.path.exists(new_path):
            new_path = os.path.join(folder, f"{date} ({i}).jpg")
            i += 1

    # rename the file
    os.rename(file_path, new_path)

    # print the old and new names of the file
    print(f'Renamed "{file_path}" to "{new_path}"')
