import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

BOT_API_KEY = '5885749837:AAFrGe1YRIt7nmCLEvsidGfecoqKfVQS2Pk'

def start(update, context):
    update.message.reply_text('Hello!')

def Alex(update, context):
    # Create the buttons
    button1 = InlineKeyboardButton("Maand 1", callback_data="1")
    button2 = InlineKeyboardButton("Maand 2", callback_data="2")
    button3 = InlineKeyboardButton("Maand 3", callback_data="3")
    button4 = InlineKeyboardButton("Maand 4", callback_data="4")
    button5 = InlineKeyboardButton("Maand 5", callback_data="5")
    button6 = InlineKeyboardButton("Maand 6", callback_data="6")
    button7 = InlineKeyboardButton("Maand 7", callback_data="7")
    button8 = InlineKeyboardButton("Maand 8", callback_data="8")
    button9 = InlineKeyboardButton("Maand 9", callback_data="9")
    button10 = InlineKeyboardButton("Maand 10", callback_data="10")
    button11 = InlineKeyboardButton("Maand 11", callback_data="11")
    button12 = InlineKeyboardButton("Maand 12", callback_data="12")
    button13 = InlineKeyboardButton("Maand 13", callback_data="13")
    button14 = InlineKeyboardButton("Maand 14", callback_data="14")
    button15 = InlineKeyboardButton("Maand 15", callback_data="15")
    button16 = InlineKeyboardButton("Maand 16", callback_data="16")



    # Create a list of the buttons to create the keyboard
    keyboard = [
        [button1, button2, button3],
        [button4, button5, button6],
        [button7, button8, button9],
        [button10, button11, button12],
        [button13, button14, button15],
        [button16]

    ]

    # Create the keyboard markup
    keyboard_markup = InlineKeyboardMarkup(keyboard)

    # Send the message with the keyboard to the user
    context.bot.send_message(chat_id=update.message.chat_id, text="Selecteer een maand:", reply_markup=keyboard_markup)

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
    dp.add_handler(CommandHandler("Alex", Alex))

    # Add callback query handler to handle button clicks
    dp.add_handler(CallbackQueryHandler(button_clicked))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
