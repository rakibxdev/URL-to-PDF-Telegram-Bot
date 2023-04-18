# URL-to-PDF-Telegram-Bot

This Telegram bot allows users to convert a web page to a PDF file by providing the URL of the page. Users can interact with the bot using simple commands, and the bot responds with the converted PDF file. The bot is built using the Python Telegram Bot library and the PDFShift API for converting web pages to PDF.

Features
Convert a web page to PDF by providing the URL
Rename the PDF file with the domain name of the given URL
Display a simple progress bar while the bot is processing the URL
Commands
/start: Starts the bot and sends a welcome message
/pdf <url>: Converts the provided URL to a PDF file


This Telegram bot allows users to convert a web page to a PDF file by providing the URL of the page. Users can interact with the bot using simple commands, and the bot responds with the converted PDF file. The bot is built using the [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) library and the [PDFShift](https://pdfshift.io) API for converting web pages to PDF.

## Features

- Convert a web page to PDF by providing the URL
- Rename the PDF file with the domain name of the given URL
- Display a simple progress bar while the bot is processing the URL

## Commands

- `/start`: Starts the bot and sends a welcome message
- `/pdf <url>`: Converts the provided URL to a PDF file

## Setup

1.pip install python-telegram-bot
  
2.pip instal requests
  
3.Replace 'YOUR_API_TOKEN' with your Telegram bot API token in the bot = telebot.TeleBot('YOUR_API_TOKEN') line.
  

4.Replace  your PDFShift API key in the auth=('api', 'PDFShift_API_KEY') line.

  

  
python main.py
