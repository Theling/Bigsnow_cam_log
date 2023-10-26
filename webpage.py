import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By


X1, Y1, X2, Y2 = 80, 0, 1520, 820

def crop(filename):
    # Crop the image
    img = Image.open(filename)
    cropped_img = img.crop((X1, Y1, X2, Y2))  # Set the coordinates (x1, y1, x2, y2) for cropping
    cropped_img.save(filename+'.crop.png')
    img.close()

# Function to capture and crop screenshot
def capture_screenshot(*, 
                       driver, 
                       url: str, 
                       save_path: str,
                       verbose = False) -> None:
    # Open the webpage
    driver.get(url)
    time.sleep(5)  # Wait for the page to load (you might need to adjust this)

    video_element = driver.find_element(By.ID, "webcam_holder")  # Replace with the actual class name of the <video> element

    # Scroll to the bottom of the page to load all content
    driver.execute_script("arguments[0].scrollIntoView(true);", video_element)

    # Capture screenshot
    screenshot_path = save_path 
    driver.save_screenshot(screenshot_path)
    if verbose: print(f"Log created: {save_path}")
    
    crop(screenshot_path)
    



