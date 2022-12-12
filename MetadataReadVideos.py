import glob
import os
from pymediainfo import MediaInfo

#todo do the same for all other file formats, .mp4 etc

# Get a list of all .mov files in the directory
mov_files = glob.glob("pic4/*.jpg")

# Loop through the list of files
for file in mov_files:
    # Open the file
    media_info = MediaInfo.parse(file)

    # Print all metadata
    for track in media_info.tracks:
        if track.track_type == "Video":
            print("Video:")
            for key, value in track.to_data().items():
                if key == "encoded_date":
                    value = value.replace("UTC", "")
                    value = value[:11]
                    print(value)

                    # Rename the file
                    current_file_path = file
                    new_file_name = f"{value}.jpg"
                    new_file_path = os.path.join("video", new_file_name)

                    # Add a counter to the file name to make it unique
                    counter = 1
                    while os.path.exists(new_file_path):
                        new_file_name = f"{value}_{counter}.jpg"
                        new_file_path = os.path.join("video", new_file_name)
                        counter += 1

                    # Rename the file
                    os.rename(current_file_path, new_file_path)


