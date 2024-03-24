import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, commandHandler
from config import telegram_bot_token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level = loggin.INFO
)


async def start(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id= update.effective_chat.id, text= "I'm a bot,pleas talk to me!")


if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_bot_token).build()

    start_handler = CommandHandler().('start', start)
    application.add_handler(start_handler)

    application.run_polling()
