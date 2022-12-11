import os
import telegram
import random
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Bot API key
API_KEY = '5885749837:AAFrGe1YRIt7nmCLEvsidGfecoqKfVQS2Pk'

# Create the Updater and pass it the bot's API key
updater = Updater(API_KEY)

# Define a function to handle the /pics command
def pics_command(update, context):
    # Get the bot instance
    bot = context.bot

    # Define a callback function to handle the button clicks
    def button_clicked(update, context):
        # Get the data from the callback query
        query = update.callback_query
        data = query.data

        # Check which button was clicked
        if data == "button1":
            # Open a random picture from the "pictures" folder
            # Get a list of all files in the "pictures" folder
            files = os.listdir("pictures")

            # Get a random file from the list of files
            file = random.choice(files)

            # Open the picture file and send it to the chat
            with open("pictures/" + file, "rb") as f:
                bot.send_photo(chat_id=query.message.chat_id, photo=f)
        elif data == "button2":
            # Open a random picture from the "pictures" folder
            # Get a list of all files in the "pictures" folder
            files = os.listdir("pictures")

            # Get a random file from the list of files
            file = random.choice(files)

            # Open the picture file and send it to the chat
            with open("pictures/" + file, "rb") as f:
                bot.send_photo(chat_id=query.message.chat_id, photo=f)
        elif data == "button3":
            # Create the buttons using the inline keyboard
            keyboard = [
                [
                    telegram.InlineKeyboardButton("Button 4", callback_data="button4"),
                    telegram.InlineKeyboardButton("Button 5", callback_data="button5"),
                ]
            ]

            # Create the inline keyboard markup
            reply_markup = telegram.InlineKeyboardMarkup(keyboard)

            # Send the message with the buttons to the chat
            bot.send_message(
                chat_id=query.message.chat_id,
                text="Click on one of the buttons below to go to Google!",
                reply_markup=reply_markup,

            )


    # Create the buttons using the inline keyboard
    keyboard = [
        [
            telegram.InlineKeyboardButton("Button 1", callback_data="button1"),
            telegram.InlineKeyboardButton("Button 2", callback_data="button2"),
            telegram.InlineKeyboardButton("Button 3", callback_data="button3"),
        ]
    ]

    # Create the inline keyboard markup
    reply_markup = telegram.InlineKeyboardMarkup(keyboard)

    # Send the message with the buttons to the chat
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Click on one of the buttons below to go to Google!",
        reply_markup=reply_markup,

    )

    # Create a callback query handler for the buttons
    button_clicked_handler = CallbackQueryHandler(button_clicked)

    # Add the callback query handler to the updater
    updater.dispatcher.add_handler(button_clicked_handler)


# Create a CommandHandler for the /pics command
pics_handler = CommandHandler('pics', pics_command)

# Add the command handler to the updater
updater.dispatcher.add_handler(pics_handler)

# Start the bot
updater.start_polling()