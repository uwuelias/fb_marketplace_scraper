import os
from dotenv import load_dotenv

load_dotenv()

# FB credentials
FB_EMAIL = os.getenv("EMAIL")
FB_PASSWORD = os.getenv("PASSWORD")

# discord bot credentials
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# urls
LOGIN_URL = "https://www.facebook.com/login"
MARKETPLACE_URL = "https://www.facebook.com/marketplace/category/vehicles/"

