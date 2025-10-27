import os
import random
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define your prediction categories
def generate_prediction():
    over_under = random.choice([
        "Over 0.5", "Over 1.5", "Over 2.5", "Under 2.5", "Under 3.5"
    ])
    double_chance = random.choice([
        "1X (Home or Draw)", "2X (Away or Draw)", "12 (Home or Away)"
    ])
    btts = random.choice([
        "GG (Both Teams to Score)", "NG (No Goal)"
    ])
    result = random.choice([
        "Home Win (1)", "Away Win (2)", "Draw (X)"
    ])
    
    return f"""
⚽ *Football Analyzer Bot Prediction*

📊 Over/Under: {over_under}
🎯 Double Chance: {double_chance}
🔥 Both Teams to Score: {btts}
🏁 Match Result: {result}
"""

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        odds = random.randint(10, 15)
        msg = f"🌅 *Morning Odds:* {odds}\n"
    else:
        odds = random.randint(100, 200)
        msg = f"🌆 *Evening Odds:* {odds}\n"

    prediction = generate_prediction()
    await update.message.reply_text(msg + prediction, parse_mode="Markdown")

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
