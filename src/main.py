import argparse

from driver_setup import create_driver
from login import login
from marketplace_scraper import get_listing_urls, scrape_listing
from discord.webhook_setup import send_webhook_message

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type = int, help = "Enter how many listings you would like", default = 10)
    parser.add_argument('--headless', type = bool, help = "Enter True or False for headless", default = False)

    args = parser.parse_args()

    limit = args.limit
    headless = args.headless

    driver = create_driver(headless = headless)
    try:
        login(driver)
        urls = get_listing_urls(driver, max_links = limit)

        # scrape information (title, price, location, etc.) from each listing
        # and send it to the Discord webhook
        for url in urls:
            data = scrape_listing(driver, url)
            send_webhook_message(data)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
