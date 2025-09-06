import time
from selenium.webdriver.common.by import By
from config import FB_EMAIL, FB_PASSWORD, LOGIN_URL

def login(driver):
    driver.get(LOGIN_URL)
    driver.refresh()
    time.sleep(2)

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")

    email_input.send_keys(FB_EMAIL)
    time.sleep(4)
    password_input.send_keys(FB_PASSWORD)
    time.sleep(4)

    login_button = driver.find_element(By.ID, "loginbutton")
    login_button.click()
    time.sleep(3)