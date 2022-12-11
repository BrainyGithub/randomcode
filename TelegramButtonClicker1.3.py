import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

BOT_API_KEY = '5885749837:AAFrGe1YRIt7nmCLEvsidGfecoqKfVQS2Pk'

def start(update, context):
    update.message.reply_text('Hello!')

def pics(update, context):
    # Create the buttons
    button1 = InlineKeyboardButton("Button 1", callback_data="1")
    button2 = InlineKeyboardButton("Button 2", callback_data="2")
    button3 = InlineKeyboardButton("Button 3", callback_data="3")
    button4 = InlineKeyboardButton("Button 4", callback_data="4")
    button5 = InlineKeyboardButton("Button 5", callback_data="5")
    button6 = InlineKeyboardButton("Button 6", callback_data="6")

    # Create a list of the buttons to create the keyboard
    keyboard = [
        [button1, button2, button3],
        [button4, button5, button6]
    ]

    # Create the keyboard markup
    keyboard_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the keyboard to the user
    context.bot.send_message(chat_id=update.message.chat_id, text="Select a button:", reply_markup=keyboard_markup)

def button_clicked(update, context):
    query = update.callback_query

    # Check which button was clicked
    if query.data == "1":
        # Get a random picture from the "pic1" folder
        files = os.listdir("pic1")
        picture = random.choice(files)

        # Send the picture to the user
        context.bot.send_photo(chat_id=query.message.chat_id, photo=open("pic1/" + picture, "rb"))
    elif query.data == "2":
        # Get a random picture from the "pic2" folder
        files = os.listdir("pic2")
        picture = random.choice(files)

        # Send the picture to the user
        context.bot.send_photo(chat_id=query.message.chat_id, photo=open("pic2/" + picture, "rb"))

def main():
    # Create the Updater and pass it the bot's API key
    updater = Updater(BOT_API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler to start the bot and the command to display the keyboard
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("pics", pics))

    # Add callback query handler to handle button clicks
    dp.add_handler(CallbackQueryHandler(button_clicked))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
