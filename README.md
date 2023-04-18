# URL-to-PDF-Telegram-Bot

This Telegram bot allows users to convert a web page to a PDF file by providing the URL of the page. Users can interact with the bot using simple commands, and the bot responds with the converted PDF file. The bot is built using the Python Telegram Bot library and the PDFShift API for converting web pages to PDF.

Features
Convert a web page to PDF by providing the URL
Rename the PDF file with the domain name of the given URL
Display a simple progress bar while the bot is processing the URL
Commands
/start: Starts the bot and sends a welcome message
/pdf <url>: Converts the provided URL to a PDF file
Setup
Clone this repository:

bash
Copy code
git clone https://github.com/your-github-username/url-to-pdf-telegram-bot.git
Install the required dependencies:

Copy code
pip install python-telegram-bot requests
Replace 'YOUR_API_TOKEN' with your Telegram bot API token in the bot = telebot.TeleBot('YOUR_API_TOKEN') line.

Replace  your PDFShift API key in the auth=('api', 'PDFShift_API_KEY') line.

Run the bot:

css
Copy code
python main.py
License
This project is licensed under the MIT License.
