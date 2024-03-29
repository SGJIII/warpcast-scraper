# scraper.py (for scraping followers)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_followers(username):
    # Initialize WebDriver with Chrome options
    driver = webdriver.Chrome()

    # Load the page
    url = f'https://warpcast.com/{username}/following'
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)  # Wait for up to 10 seconds for elements to become available

    # Scroll down to load all followers
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(2)  # Adjust sleep time as needed

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get all followers
    followers = driver.find_elements(By.XPATH, "//div[@class='text-muted text-base' and starts-with(text(), '@')]")
    follower_list = [follower.text[1:] for follower in followers]  # Remove the "@" symbol

    driver.quit()
    return follower_list















