#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import os
import random

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def get_files(folder):
    files = []
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            files.append(file)
    
    return files


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    folder = ''

    if query.data == '1':
        folder = 'images\cats'
    elif query.data == '2':
        folder = 'images\dogs'
    else:
        folder = 'images\cats'

    c = []

    files = get_files(folder)

    random_file = random.choice(files)
    print('Random file:', random_file)

    image_path = f'/{folder}/{random_file}'

    await query.message.reply_photo(
     photo=open(image_path, 'rb'),
    )

    # print(update.callback_query.message.chat.id)

    # await query.edit_message_text(
    #     text=f"Selected option: {query.data}",
    #     reply_markup=InlineKeyboardMarkup(
    #         [
    #             [
    #                 InlineKeyboardButton(
    #                     text="Back",
    #                     callback_data="back",
    #                 )
    #             ]
    #         ]
    #     )
    # )
    #
    # await update.get_bot().send_photo(
    #     chat_id=update.callback_query.message.chat.id,
    #     photo=open(image_path, 'rb'),
    # )

    # await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")

   

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    TOKEN = '6734422120:AAFpCuIJzF1PZrd3xGE-IlEEKtDpkcPGcp0'
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()