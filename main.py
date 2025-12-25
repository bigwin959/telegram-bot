import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

# --- BOT SETTINGS ---

EVENT_LINK = "https://channel0.bigwin959.com/register.html"
BOT_HANDLE = "@bigwin959official_bot"

# --- START MESSAGE ---
WELCOME_MSG = (
    "🎆 <b>Welcome to BIGWIN959 | Sports & Slots!</b>\n\n"
    "Celebrate the <b>New Year 2026</b> with our special event 🎉\n"
    "💰 <b>150% Slot Deposit Bonus</b> awaits you!\n\n"
    "📅 Event Duration: <b>Dec 25 – Jan 8</b>\n"
    "🏏 Play cricket slots, enjoy sports fun & big rewards!\n\n"
    "Choose an option below to get started 👇"
)

DETAILS_MSG = (
    "🎆 <b>New Year 150% Bonus Details</b>\n\n"
    "📅 Duration: <b>Dec 25, 2025 – Jan 8, 2026</b>\n"
    "💎 Offer: Get a <b>150% Slot Deposit Bonus</b> instantly.\n"
    "🏏 Games: Cricket slots, sports themes, and festive spins!\n\n"
    "⚠️ <i>For entertainment only. 18+ Terms apply.</i>\n\n"
    "👉 Tap below to claim your bonus."
)

# --- START HANDLER ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Claim 150% Bonus", callback_data="claim")],
        [InlineKeyboardButton("ℹ️ Event Details", callback_data="details")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        text=WELCOME_MSG,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

# --- CALLBACK HANDLER ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "claim":
        keyboard = [[InlineKeyboardButton("🌐 Open Website", url=EVENT_LINK)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="🎁 <b>Claim Your 150% Bonus Now!</b>\n\n"
                 "Visit our official site to activate your bonus 👇",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

    elif query.data == "details":
        keyboard = [[InlineKeyboardButton("🎁 Claim Bonus", callback_data="claim")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=DETAILS_MSG,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

# --- MAIN FUNCTION ---
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 BIGWIN959 Event Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
