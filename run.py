from webpage import capture_screenshot
from utils import generate_filename

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
# chrome_options.add_argument("--start-maximized") # Maximize window to ensure entire page is captured
driver = webdriver.Chrome(options=chrome_options)


# URL of the webpage to scrape
url = "https://www.bigsnowamericandream.com/live-stream/"  # Replace this with the URL of the webpage you want to scrape


driver.get(url)
def main(step_time = 900):
    # Run the scraping script every 15 minutes
    log_path = f"./log/{generate_filename()}"
    while True:
        capture_screenshot(driver = driver,
                        url = url, 
                        save_path = log_path)
        time.sleep(step_time)  # 900 seconds = 15 minutes
        


        
if __name__ == "__main__":
    import sys
    step_time = sys.argv[1]
    print(f"Saving screenshots every {step_time} seconds")
    main(step_time)
    
    # test()