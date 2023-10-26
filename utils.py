import datetime
import os

def generate_filename():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    return filename

# Function to remove old files from a directory
def remove_old_files(directory_path, threshold_seconds):
    current_time = datetime.datetime.now()

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # Get the modification time of the file
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            # Calculate the age of the file in seconds
            file_age_seconds = (current_time - modification_time).total_seconds()
            # If the file is older than the threshold, remove it
            if file_age_seconds > threshold_seconds:
                os.remove(file_path)
                print(f"Removed old file: {filename}")
                
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created successfully.")
    else:
        print(f"Directory '{directory_path}' already exists.")