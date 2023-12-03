# "Amazon Price Tracker with Telegram Alerts"
<br />
</br>

## Overview

This Python application monitors the price of a specific item on Amazon (in this case, an Xbox controller) and sends an alert via Telegram if the price falls below a predefined threshold.
It uses BeautifulSoup for web scraping and the Telegram Bot API for sending notifications.
<br />


## Features

1. Tracks the price of an Xbox controller on Amazon using a Python Webscraper.
2. Sends a Telegram message if the price drops below $200.
3. Customizable for different products and price thresholds.




## Prerequisites 
To run this project, you will need:

+ **Python:** The application is written in Python(3.6 and above), a recent version of [Python](https://www.python.org/downloads/).
+ **Pip:** Python's package installer, pip, should be installed for managing Python packages. It usually comes with Python installation.
+ **Libraries:** requests and beautifulsoup4.
+ **APIs:** A Telegram bot and corresponding API token.
+ **URL:** Amazon product URL.

## Installation

- **Clone the Repository:** git clone https://github.com/SonnyGU/Amazon-Product-Tracker.git
- **Install the Requests library using pip:** pip install requests beautifulsoup4 
- **Run the Application:** python main.py

## Setup

1. Create a Telegram bot using BotFather and get the API token.
2. Set up environment variables for the Telegram bot token, chat ID, Amazon product URL, User-Agent, and Accept-Language. You can use a .env file or your system's environment variable settings.
   


## Program walk-through:

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/dHm4kV2.png" height="60%" width="60%" alt="Amazon Tracker Steps"/>
<br />
<br />
Once the application runs, you'll receive a message through Telegram:  <br/>
<img src="https://i.imgur.com/CPSl3aG.png" height="70%" width="70%" alt="Amazon Tracker Steps"/>



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
