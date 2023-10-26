from PIL import Image, ImageDraw, ImageFont
import datetime

class ImageProc:
    X1, Y1, X2, Y2 = 80/1600, 0/1200, 1520/1600, 820/1200
    
    def __init__(self, filename) -> None:
        self.f = filename
        self.img = Image.open(self.f)

    def crop(self):
        # Crop the image
        img = self.img
        image_width, image_height = img.size
        # print(image_width, image_height)
        cropped_img = img.crop((self.X1*image_width, 
                                self.Y1*image_height, 
                                self.X2*image_width, 
                                self.Y2*image_height))  # Set the coordinates (x1, y1, x2, y2) for cropping
        self.img = cropped_img
        return self
        
        
    def add_timestamp(self):
        image = self.img
        # Get the current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Use the default font with a specified size (change 36 to your desired font size)
        font_size = 36
        font = ImageFont.load_default()  # Default font
        font = font.font_variant(size=font_size)  # Modify the font size

        # Set the position for the timestamp (top-left corner)
        position = (10, 10)

        # Set the text color
        text_color = (255, 255, 255)  # White color

        # Add the timestamp to the image
        draw.text(position, current_time, fill=text_color, font = font)
        return self


    def save(self, filename = None):
        if filename is None: filename == self.f
        self.img.save(self.f)
        
    def __del__(self):
        self.img.close()
