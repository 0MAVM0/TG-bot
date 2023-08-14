from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "6429731092:AAHbdUp9BlQnQ5B0AmWrbUFrSEtBM2N-mvY"

print("Running up the bot...")

def start(update, context):
    _send_local_file(update, context)
    help(update, context)


def _send_local_file(update, context):
    with open("me.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Hello! This is me!")

def get_order_food_message(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton("Best burger of the week")],
        [KeyboardButton("Cheese burger")],
        [KeyboardButton("Hamburger")]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Order food:",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

def callback_query_handler_for_attached_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == "1":
        query.edit_message_text(text="You pressed button 1")
    elif query.data == "2":
        query.edit_message_text(text="You pressed button 2")

def message_handler_for_below_buttons(update: Update, context: CallbackContext):
    if update.message.text == "Best burger of the week":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="It costs 99,9$\nYou should pay by electronic card\nCard of 🍔King is: 8801 3062 3759 9944",
        )
    elif update.message.text == "Cheese burger":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="It costs 49,9$\nYou should pay by electronic card\nCard of 🍔King is: 8801 3062 3759 9944",
        )
    elif update.message.text == "Hamburger":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="It costs 14,9$\nYou should pay by electronic card\nCard of 🍔King is: 8801 3062 3759 9944",
        )
    elif update.message.text == "Burger":
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="It costs 9,9$\nYou should pay by electronic card\nCard of 🍔King is: 8801 3062 3759 9944",
        )

def help(update, context):
    update.message.reply_text("""
/start      - Start the bot
/help       - Help
/order_food - Order food
"""
                              )

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler('order_food', get_order_food_message))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler_for_below_buttons))
dispatcher.add_handler(CallbackQueryHandler(callback_query_handler_for_attached_buttons))

updater.start_polling()
updater.idle()
