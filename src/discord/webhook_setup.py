import requests
from config import DISCORD_WEBHOOK_URL

def send_webhook_message(data: dict):
    content = (
    f"Title: {data.get('title', 'Unknown Title')}\n"
    f"Price: {data.get('price', 'N/A')}\n"
    f"Mileage: {data.get('mileage', 'N/A')}\n"
    f"Transmission: {data.get('transmission', 'N/A')}"
)
    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json={"content": content}
    )

