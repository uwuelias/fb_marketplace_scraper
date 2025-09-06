import requests
from config import DISCORD_WEBHOOK_URL

def send_webhook_message(data: dict):
    content = (
        f"Title: {data['title']}\n"
        f"Price: {data['price']}\n"
        f"Mileage: {data['mileage']}\n"
        f"Transmission: {data['transmission']}"
    )
    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json={"content": content}
    )

