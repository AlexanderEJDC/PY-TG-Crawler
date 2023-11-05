import logging
import asyncio
import telegram
from telegram import Update, File, Document, Message
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder, ContextTypes 

#Configure Logging module - use level=logging.DEBUG for more verbose info.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

#async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    await context.bot.send_message(
#        chat_id=update.effective_chat.id, 
#        text="The Bot Is Starting")

    
async def main():
    bot = telegram.Bot('6460026166:AAFf7Wv93Cpa9YUFtsZ0E-AJfmFgKGDx_1s')
    async with bot:
        print((await bot.send_message(text="This sends a file", chat_id=6343314843)))
        await bot.send_document(chat_id=6343314843, document='ECA.jpg')

        receivedFile = await message.effective_attachment.get_file()
        await new_file.download_to_drive('TGFile') 

if __name__ == '__main__':
    asyncio.run(main())
