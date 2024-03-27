# scraper.py (for scraping followers)
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

    # Get all followers
    followers = driver.find_elements(By.XPATH, "//div[@class='avatar']//span[@class='username']")
    follower_list = [follower.text for follower in followers]

    driver.quit()
    return follower_list












