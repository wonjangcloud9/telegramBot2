from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

token = '1944485735:AAEDWxnqpVQmjeJza2RM_43V5rRBfBWNQGI'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="자, 게임을 시작하지.")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def end(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="자, 게임을 종료하지.")


end_handler = CommandHandler('end', end)
dispatcher.add_handler(end_handler)


def echo(update, context):
    text = "너 지금 \'"+update.message.text+"\'이라 했니?"
    context.bot.send_message(chat_id=update.effective_chat.id, text= text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
