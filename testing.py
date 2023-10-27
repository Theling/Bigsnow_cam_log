
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
    driver.set_window_size(800, 600)

    # URL of the webpage to scrape
    url = "https://www.bigsnowamericandream.com/live-stream/"  # Replace this with the URL of the webpage you want to scrape


    driver.get(url)
    def test():
        log_path = f"./test/{generate_filename()}"
        capture_screenshot(driver = driver,
                            url = url, 
                            save_path = log_path,
                            verbose=True)
        
    test()
    
def main_remove():
    from utils import remove_old_files
    
    remove_old_files("./log", 1800)
    
    
def main_git():
    from git import git_operations
    
    git_operations('./log')
    
def main_window_size():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
    # chrome_options.add_argument("--start-maximized") # Maximize window to ensure entire page is captured
    driver = webdriver.Chrome(options=chrome_options)
    

    # Open a webpage (optional)
    url = "https://www.bigsnowamericandream.com/live-stream/"   # Replace with the URL of the webpage you want to open (optional)
    driver.get(url)

    # Get the WebDriver window's resolution
    window_rect = driver.get_window_rect()
    window_width = window_rect['width']
    window_height = window_rect['height']

    # Print the resolution
    print("Window Width:", window_width, "pixels")
    print("Window Height:", window_height, "pixels")

    # Close the WebDriver
    driver.quit()
        
        
def main_report():
    from utils import report
    
    report('./test')
        

if __name__=="__main__":
    # main_remove()
    # main_git()
    # main_window_size()
    # main()
    main_report()