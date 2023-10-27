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
        
     

def report(filepath):
    images_directory = filepath
    # Get a list of all .png files in the directory
    image_files = [file for file in os.listdir(images_directory) if file.lower().endswith(".png")]

    # Sort the image files in reverse order
    image_files.sort(reverse=True)

    # Output Markdown file path
    markdown_output_path = "history.md"

    # Create a Markdown file with image links in reverse order
    with open(markdown_output_path, "w") as markdown_file:
        markdown_file.write("# Big Snow Cam Log\n\n")
        
        for image_file in image_files:
            image_path = os.path.join(images_directory, image_file)
            markdown_file.write(f"![{image_file}]({image_path})\n\n")

    print(f"Markdown file with images created: {markdown_output_path}")

# def report(filepath):
#     images_directory = filepath
#     # Get a list of all .png files in the directory
#     image_files = [file for file in os.listdir(images_directory) if file.lower().endswith(".png")]

#     # Sort the image files in reverse order
#     image_files.sort(reverse=True)

#     # Output PDF file path
#     pdf_output_path = "history.pdf"

#     # Create a PDF with images in reverse order
#     c = canvas.Canvas(pdf_output_path, pagesize=letter)
#     pdf_width, pdf_height = letter

#     # Function to add an image to the PDF
#     def add_image_to_pdf(image_path, x, y, width, height):
#         img = Image.open(image_path)
#         img_width, img_height = img.size
#         aspect_ratio = img_width / img_height
        
#         # Scale the image to fit within the specified width and height
#         if img_width > width:
#             img_width = width
#             img_height = int(img_width / aspect_ratio)
#         if img_height > height:
#             img_height = height
#             img_width = int(img_height * aspect_ratio)
        
#         c.drawImage(image_path, x, y, width=img_width, height=img_height)

#     # Add images to the PDF
#     x_position = 20
#     y_position = pdf_height - 50
#     for image_file in image_files:
#         image_path = os.path.join(images_directory, image_file)
#         add_image_to_pdf(image_path, x_position, y_position, width=400, height=300)
#         y_position -= 320  # Adjust the vertical position for the next image

#     # Save the PDF file
#     c.save()

#     print(f"PDF with images created: {pdf_output_path}")
        
