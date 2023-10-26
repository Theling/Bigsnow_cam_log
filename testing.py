
def main_crop():
    
    from webpage import crop
    crop("/Users/zhiyuanyao/Projects/Bigsnow_cam_log/log/screenshot_2023-10-26_14-23-36.png")


def main():
    from webpage import capture_screenshot
    from utils import generate_filename
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    # Set up Chrome WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    # chrome_options.add_argument("--start-maximized") # Maximize window to ensure entire page is captured
    driver = webdriver.Chrome(options=chrome_options)


    # URL of the webpage to scrape
    url = "https://www.bigsnowamericandream.com/live-stream/"  # Replace this with the URL of the webpage you want to scrape


    driver.get(url)
    def test():
        log_path = f"./log/{generate_filename()}"
        capture_screenshot(driver = driver,
                            url = url, 
                            save_path = log_path,
                            verbose=True)
        
    test()
        
        

if __name__=="__main__":
    main()