from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "6429731092:AAHbdUp9BlQnQ5B0AmWrbUFrSEtBM2N-mvY"

RANDOM_IMAGE = "Random image"
GET_MP3 = "Get mp3"
RANDOM_IMG_URL = "https://picsum.photos/1200"

global IMAGE_COUNTER
IMAGE_COUNTER = 0

print("Running up the bot...")

def start(update, context):
    _send_local_file(update, context)

def _send_local_file(update, context):
    with open("me.jpg", "rb") as f:
        update.message.reply_photo(f, caption="Hello world! This is me!")

def _send_mp3(update: Update, context: CallbackContext):
    with open("music.mp3", "rb") as f:
        update.message.reply_audio(f, caption="This is mp3")

def get_buttons(update: Update, context: CallbackContext):
    buttons = [
        [KeyboardButton(RANDOM_IMAGE)],
        [KeyboardButton(GET_MP3)]
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Choose option:",
        reply_markup=ReplyKeyboardMarkup(buttons)
    )

def message_handler(update: Update, context: CallbackContext):
    global IMAGE_COUNTER
    IMAGE_COUNTER += 1
    if update.message.text == RANDOM_IMAGE:
        image = get(RANDOM_IMG_URL).content
        context.bot.sendMediaGroup(
            chat_id=update.effective_chat.id,
            media=[InputMediaPhoto(image, caption=f"Random {IMAGE_COUNTER}")]
        )
    elif update.message.text == GET_MP3:
        _send_mp3(update, context)

def help(update, context):
    update.message.reply_text("""
/start   - Start the bot
/help    - Help
/buttons - Get Optional buttons
"""
                              )

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler('buttons', get_buttons))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

updater.start_polling()
updater.idle()
