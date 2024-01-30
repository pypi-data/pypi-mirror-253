# my_telebot/bot.py
from telegram.ext import Updater as U, MessageHandler as MH, Filters as F

class MTB:
    def __init__(s, t):
        s.u = U(token=t, use_context=True)
        s.d = s.u.dispatcher
        s.h1 = MH(F.command & F.regex('start'), s.s)
        s.h2 = MH(F.text & ~F.command, s.e)
        s.d.add_handler(s.h1)
        s.d.add_handler(s.h2)

    def s(s, u, c):
        c.bot.send_message(chat_id=u.effective_chat.id, text="Hello! I'm your cool telebot. Send me a message, and I'll echo it back.")

    def e(s, u, c):
        c.bot.send_message(chat_id=u.effective_chat.id, text=u.message.text)

    def p(s):
        s.u.start_polling()

    def i(s):
        s.u.idle()
