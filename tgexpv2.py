import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

#Configure Logging module - use level=logging.DEBUG for more verbose info.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#This is what the application builder actually uses. 
#Defines a function that processes a specific form of update. 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Setting out a basic platform.")

if __name__ == '__main__':
    #Application builder. On its own, doesn't do anything.
    application = ApplicationBuilder().token(
        '6460026166:AAFf7Wv93Cpa9YUFtsZ0E-AJfmFgKGDx_1s').build()
    
    #The command handler. This will listen for the "\start"
    #commands.
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    #This runs the bot until it recieves Cntrl-C from Terminal!
    application.run_polling() 