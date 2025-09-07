# Facebook Marketplace Scraper

This project automates tracking vehicle listings on Facebook Marketplace by using Selenium to log in and parse listing details such as title, price, location, and link. The collected information is then sent in real time to a Discord server via a webhook, enabling instant notifications of new listings. This automation streamlines the process of monitoring Marketplace, saving time and ensuring users never miss relevant vehicle postings.

## Features

- Log in to Facebook using credentials from '.env' file
- Access Facebook Marketplace
- Avoid CAPTCHA (I think it works)
- Parse listing info (i.e. title, price, transmission type, mileage)
- Sends the listing info to a discord webhook

## Built With

Python 3.13.7
Selenium
Discord Webhooks
dotenv

## Prerequisites

- Python 3.10+
- Google Chrome or Mozilla Firefox installed

## Getting Started

```bash
# Clone repo
git clone https://github.com/uwuelias/fb_marketplace_scraper.git
cd fb_marketplace_scraper

# Create Virtual Environment
python -m venv venv
source venv/bin/activate # Linux/Mac
# or
venv\Scripts\activate # Windows

# Install dependencies
pip install -r requirements.txt

# Create a .env file based on the example provided
touch .env # Remember to put in your facebook credentials and discord webhook url

# Go into the source directory
cd src

# Run the scraper
python main.py
```

## Limitations

- CAPTCHA may still appear; the scraper may not bypass all challenges
- Scraping Facebook may violate their Terms of Service – use responsibly
- Facebook Marketplace layout changes can break the scraper
- Only supports vehicles at the moment

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgement

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Discord Webhooks Documentation](https://discord.com/developers/docs/resources/webhook)
- Inspiration from similar Facebook Marketplace automation projects
