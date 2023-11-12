import logging
import asyncio
import telegram
from telegram import Update
from telegram.ext import MessageHandler, filters, ApplicationBuilder, ContextTypes

#Configure Logging module - use level=logging.DEBUG for more verbose info.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="I have recieved your response")
    
async def file_download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    incom_file = await update.message.effective_attachment.get_file()
    await incom_file.download_to_drive('recieved_file')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="File recieved!")

#Actual "Main" - runs handlers & bot!
if __name__ == '__main__':
    #Application builder. On its own, doesn't do anything.
    application = ApplicationBuilder().token(
        '6460026166:AAFf7Wv93Cpa9YUFtsZ0E-AJfmFgKGDx_1s').build()
    
    file_handler = MessageHandler(filters.ATTACHMENT & (~filters.COMMAND), file_download)
    echo_handler = MessageHandler(filters.ALL & (~filters.COMMAND), echo)

    application.add_handler(file_handler)
    application.add_handler(echo_handler)

    application.run_polling()  #Run until Cntrl-C! 