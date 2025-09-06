from driver_setup import create_driver
from login import login
from marketplace_scraper import get_listing_urls, scrape_listing
from discord.webhook_setup import send_webhook_message

def main():

    driver = create_driver()
    try:
        login(driver)
        urls = get_listing_urls(driver, max_links=2)

        for url in urls:
            data = scrape_listing(driver, url)
            send_webhook_message(data)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
