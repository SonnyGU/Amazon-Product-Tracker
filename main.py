import requests
import os
from bs4 import BeautifulSoup

# URL of the Amazon product page
URL = ("https://www.amazon.com/Microsoft-Elite-Controller-Starter-Bundle/dp/B082LNJ927/ref=sr_1_2?content-id=amzn1.sym"
       ".9bbe09a5-e2ce-4594-80e8-ad6153d0ea3e%3Aamzn1.sym.9bbe09a5-e2ce-4594-80e8-ad6153d0ea3e&keywords=xbox"
       "+controller+elite&pd_rd_r=b0f25058-e382-4466-b8e7-91903564459d&pd_rd_w=garNi&pd_rd_wg=dCq0P&pf_rd_p=9bbe09a5"
       "-e2ce-4594-80e8-ad6153d0ea3e&pf_rd_r=8PGKMPS2R441SXQ2CNVJ&qid=1701632641&sr=8-2&ufe=app_do%3Aamzn1.fos"
       ".17d9e15d-4e43-4581-b373-0e5c1a776d5d")

# Environment variables for user agent and accept language headers
USER_AGENT = os.getenv("USER_AGENT")
ACCEPT_LANGUAGE = os.getenv("ACCEPT_LANGUAGE")
bot_token = os.getenv('BOT_TOKEN')  # Token for telegram messaging bot
chat_id = os.getenv('CHAT_ID')  # Token for telegram chat id

# Headers to mimic a real browser request
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

# Send a GET request to Amazon product page
response = requests.get(url=URL, headers=headers)
amazon_data = response.text

# Parse the HTML content of the page
soup = BeautifulSoup(amazon_data, "lxml")

# Find the price element and extract its text
price = soup.find(name="span", class_="a-price-whole")
xbox_price = price.getText().replace(".", '')


# Function to send a message through a Telegram bot
def telegram_bot_sendtext(bot_message):
    # Construct the URL for the Telegram sendMessage API
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    # Send the request to Telegram API and get the response
    bot_response = requests.get(send_text)

    # Return the JSON response
    return bot_response.json()


# Check if the Xbox price is below a certain threshold and send an alert
if int(xbox_price) < 200:
    # Construct the alert message
    message = f"Xbox price Alert\nPrice: ${xbox_price}\nURL: {URL}"
    # Sending the message via Telegram bot
    telegram_bot_sendtext(message)
