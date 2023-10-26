from webpage import capture_screenshot
from utils import generate_filename, remove_old_files, create_directory

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from pathlib import Path

from git import git_operations


# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
# chrome_options.add_argument("--start-maximized") # Maximize window to ensure entire page is captured
driver = webdriver.Chrome(options=chrome_options)


# URL of the webpage to scrape
url = "https://www.bigsnowamericandream.com/live-stream/"  # Replace this with the URL of the webpage you want to scrape


def clean_push(log_path, keep_time):    
    try:
        remove_old_files(log_path, keep_time)
        git_operations(log_path, prod=args.prod)
        
    except Exception as info:
        current_time = datetime.datetime.now()
        # Format and print the current timestamp
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"<clean_push> Exceptions ({formatted_time}) -- ", info)

    

def main(args):
    step_time = int(args.step_time)
    log_path = args.log_path
    create_directory(log_path)
    while True:
        filename = str(Path(log_path)/generate_filename())
        try:
            capture_screenshot(driver = driver,
                            url = url, 
                            save_path = filename,
                            verbose=True)
            
            # time.sleep(5)
            clean_push(log_path, step_time*5)
        except Exception as info:
            current_time = datetime.datetime.now()
            # Format and print the current timestamp
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"<main> Exceptions ({formatted_time}) -- ", info)
            

        time.sleep(step_time)  # 900 seconds = 15 minutes
        



        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Capture frames from a video element and save them as images.")
    parser.add_argument("--step_time", default=900, type = int, help="Length of time interval between two screenshots in seconds, default 900.")
    parser.add_argument("--keep_num_screenshots", default=5, type = int, help="The number of screenshots kept in the directory, default 5.")
    parser.add_argument("--prod", default=True, type=bool, help="Product mode, whether to push screenshots to prod branch, default True")
    
    parser.add_argument("--log_path", default='./log', help="Directory to save screenshots, default ./log")
    args = parser.parse_args()
    print(f"Saving screenshots every {args.step_time} seconds")
    
    
    main(args)
    
    # test()