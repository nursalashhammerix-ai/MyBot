import asyncio, os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
URL = os.environ["RENDER_EXTERNAL_URL"]
PORT = int(os.environ.get("PORT", 10000))

async def reply(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await asyncio.sleep(30)
    await update.message.reply_text("Salom! Javob beraman.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN, webhook_url=f"{URL}/{TOKEN}")
