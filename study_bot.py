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
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
STAGE_ONE, STAGE_TWO, STAGE_THREE, STAGE_FOUR = range(4)


def groupet(array, num=3):
    return [array[i:i + num] for i in range(0, len(array), num)]



class section: 
    id: int
    name: str
    text: str
    sections: list

    key = 'section_'
    
    def __init__(self, id: int, name: str, text: str=''):
        self.id = id
        self.name = name
        self.text = text

   
    def get_inline_button(self):
        return InlineKeyboardButton(self.name, callback_data=self.key+str(self.id))

class course: 
    id: int
    name: str
    key = 'course_'

def __init__(self, id: int, name: str, sections: list):
    self.id = id
    self.name = name
    self.sections = sections

    def get_inline_button(self):
        return InlineKeyboardButton(self.name, callback_data=self.key+str(self.id))

courses = [
    course(1, "Python", [section(1, 'Урок 1'), section(2, 'Урок 2'), section(3, 'Урок 3')]),
    course(2, "SQL",[section(1, 'Урок 1'), section(2, 'Урок 2'), section(3, 'Урок 3')]),
    course(3, "PHP", [section(1, 'Урок 1'), section(2, 'Урок 2'), section(3, 'Урок 3')]),
    course(4, "Telegram", [section(1, 'Урок 1'), section(2, 'Урок 2'), section(3, 'Урок 3')]),
    course(5, "HTML", [section(1, 'Урок 1'), section(2, 'Урок 2'), section(3, 'Урок 3')]),
]


def get_course_by_course_key(course_key):
    id = int(course_key.replace(course.key, ''))

    for c in courses: 
        if c.id == id:
            return c

    return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""

    courses = groupet([c.get_inline_button() for c in courses], 3)

    keyboard = courses
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите курс", reply_markup=reply_markup)
    return START_ROUTES



async def course_deteil(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show new choice of buttons"""
    query = update.callback_query
    course=get_course_by_course_key(query.data)

    #print(
     #   'course',
     #  course.id,
     # course.name
    #)

    await query.answer()
    keyboard = section_keyboard
    replay_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text= f'курс по: {course_name}', reply_markup=replay_markup)
    return START_ROUTES

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    TOKEN = '6734422120:AAFpCuIJzF1PZrd3xGE-IlEEKtDpkcPGcp0'

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(course_deteil, pattern="^" + courses.key),
                
            ],
            #END_ROUTES: [
                #CallbackQueryHandler(start_over, pattern="^" + str(ONE) + "$"),
                #CallbackQueryHandler(end, pattern="^" + str(TWO) + "$"),
            #],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    

if __name__ == "__main__":
    main()