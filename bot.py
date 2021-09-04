import telebot
from telebot.types import *
import os  # To get the environment variable
from dict import *
from replit import keep_alive.keep_alive # This is for replit to keep the bot running

# Imports

bot = telebot.TeleBot(os.environ.get("DICT_BOT_API_KEY"))  # This is the bot object


@bot.message_handler(
    content_types=[
        None,
        "audio",
        "document",
        "photo",
        "sticker",
        "video",
        "video_note",
        "voice",
        "location",
        "contact",
        "new_chat_members",
        "left_chat_member",
        "new_chat_title",
        "new_chat_photo",
        "delete_chat_photo",
        "group_chat_created",
        "supergroup_chat_created",
        "channel_chat_created",
        "migrate_to_chat_id",
        "migrate_from_chat_id",
        "pinned_message",
    ]
)  # Reacts to those content types
def dont_know_message(message):
    bot.reply_to(message, "Sorry, But I dont know what to do with it")


@bot.message_handler(commands=["start"])  # Reacts to the command start
def start_command(message):
    bot.reply_to(
        message,
        f"""Hello {message.chat.first_name} I am Dictionary Bot :) You can send me any English word and I will send you its meaning. Thanks For Using :)""",
    )


@bot.message_handler(commands=["about"])  # Reacts to the command about
def about_command(message):
    bot.reply_to(
        message,
        """For now I can only give you the meanings of words but I am being constantly updated by @Zoldyck_kil :)""",
    )


@bot.message_handler(
    content_types=["text"], func=lambda msg: len(msg.text.split(" ")) >= 2
)
# Reacts if the length of the word is more than 1
def invalid_message(message):
    bot.reply_to(message, "Please send me ONLY ONE valid english word at a time")


@bot.message_handler(
    content_types=["text"], func=lambda msg: len(msg.text.split(" ")) == 1
)
# Reacts to a single word, to give its meaning
def get_meaning_of_word(message):
    meaning = get_meaning(message.text)  # meaning of the word
    if meaning:  # If meaning is not false. It is false if no meaning is found
        bot.reply_to(message, meaning)  # Replies with the meaning
    else:
        bot.reply_to(
            message,
            "Sorry but I could not find its meaning. Maybe you have a spelling mistake, please recheck",
        )


def main():
    keep_alive()  # This is to keep the flask server running which will run the bot 24/7
    # Remove the top line if not running on replit
    telebot.apihelper.RETRY_ON_ERROR = True
    bot.infinity_polling()


main()
