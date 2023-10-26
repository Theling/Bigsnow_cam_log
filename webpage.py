import time
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

from image import ImageProc


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

    # if verbose: print(video_element)
    # Scroll to the video element
    driver.execute_script("arguments[0].scrollIntoView(true);", video_element)

    # Capture screenshot
    screenshot_path = save_path 
    driver.save_screenshot(screenshot_path)
    if verbose: print(f"Log created: {save_path}")
    
    ImageProc(screenshot_path).crop().add_timestamp().save()



