import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import MARKETPLACE_URL

def get_listing_urls(driver, max_links=10):
    driver.get(MARKETPLACE_URL)
    listings = WebDriverWait(driver, 15).until( # how selenium will recognize listings 
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, '/marketplace/item/')]"))
    )
    urls = list(set(link.get_attribute("href") for link in listings)) # grab the url of each listing and store them into an array
    return urls[:max_links]

def scrape_listing(driver, url):
    driver.get(url)
    data = {"url": url}

    # scraping info from a listing
    try:
        data["title"] = driver.find_element(By.TAG_NAME, "h1").text
        data["price"] = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'$')]"))
        ).text
        data["transmission"] = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'transmission')]"))
        ).text
        data["mileage"] = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Driven')]"))
        ).text
    except:
        pass
    
    return data
