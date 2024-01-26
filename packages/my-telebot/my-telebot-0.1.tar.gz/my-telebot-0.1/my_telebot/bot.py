# my_telebot/bot.py
from telegram.ext import Updater, MessageHandler, Filters

class MyTeleBot:
    def __init__(self, token):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Define handlers
        start_handler = MessageHandler(Filters.command & Filters.regex('start'), self.start)
        echo_handler = MessageHandler(Filters.text & ~Filters.command, self.echo)

        # Add handlers to the dispatcher
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(echo_handler)

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your cool telebot. Send me a message, and I'll echo it back.")

    def echo(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def start_polling(self):
        self.updater.start_polling()

    def idle(self):
        self.updater.idle()
