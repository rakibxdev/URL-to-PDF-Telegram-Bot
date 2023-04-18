import os
import requests
import telebot
from urllib.parse import urlparse

# Replace YOUR_API_TOKEN with your bot's API token
bot = telebot.TeleBot('YOUR_API_TOKEN')

def convert_to_pdf(url):
    response = requests.post(
        'https://api.pdfshift.io/v3/convert/pdf',
        auth=('api', ' PDFShift_API_KEY'),
        json={
            "source": url,
            "landscape": False,
            "use_print": False
        }
    )

    response.raise_for_status()
    return response.content

def get_domain_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

def update_progress_bar(chat_id, message_id, progress):
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Converting URL to PDF: {progress}%")

# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, welcome to Webpage to Pdf bot! Use /pdf  for convert")

# Define the handler for the /pdf command
@bot.message_handler(commands=['pdf'])
def pdf_conversion(message):
    url = message.text[4:].strip()
    if not url:
        bot.reply_to(message, "Please provide a URL after /pdf")
        return

    try:
        # Send initial progress message
        progress_message = bot.send_message(message.chat.id, "Converting URL to PDF: 0%")

        # Update progress message
        update_progress_bar(message.chat.id, progress_message.message_id, 50)

        # Convert URL to PDF
        pdf_data = convert_to_pdf(url)

        # Update progress message
        update_progress_bar(message.chat.id, progress_message.message_id, 100)

        domain_name = get_domain_name(url)
        pdf_filename = f"{domain_name}.pdf"

        with open(pdf_filename, 'wb') as f:
            f.write(pdf_data)

        with open(pdf_filename, 'rb') as f:
            bot.send_document(message.chat.id, f, caption='Converted PDF')

        # Delete the progress message
        bot.delete_message(message.chat.id, progress_message.message_id)

    except Exception as e:
        bot.reply_to(message, f"Error while converting the URL to PDF: Please Try Again")

# Define the handler for text messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Hi " + message.from_user.first_name + '  use /pdf Webpage link please')

# Start the bot and listen for incoming messages
bot.polling()
