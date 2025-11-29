# pip install python-telegram-bot==21.4

import os
from dotenv import load_dotenv

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ========== CONFIG ==========

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

application = ApplicationBuilder().token(BOT_TOKEN).build()

# 真实业务链接（全部要 https:// 开头）
REGISTER_URL = "https://channel1.bigwin959.com/register.html"

ANDROID_APP_URL = (
    "https://images.738382910483.com/wsd-images-prod/bigbdtf7/app_pack/android/"
    "bigbdtf7_2.4.76_20251105095117.apk"
)
IOS_APP_URL = (
    "https://images.738382910483.com/wsd-images-prod/bigbdtf7/app_pack/mobileconfig/"
    "bigbdtf7_2.4.3_20251105095116.mobileconfig"
)

FB_URL = "https://www.facebook.com/share/v/1ahKqXg3W7/"
YOUTUBE_URL = "https://www.youtube.com/@bigwin959official"
TELEGRAM_CHANNEL_URL = "https://t.me/bigwin959/11"
WHATSAPP_COMMUNITY_URL = "https://chat.whatsapp.com/J1SnH9iCPvR7lyh7j4vNAO"

# 客服 / 提交截图的 Bot / 链接
CS_SUBMIT_SCREENSHOT_URL = "https://t.me/Superbigwin959_bot"

# GuideBook 链接
GUIDE_URL = "https://fsguidebook.netlify.app"


# ========== KEYBOARDS ==========

def build_step1_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "📝 রেজিস্টার করুন – ১০ ফ্রি স্পিন নিন",
                url=REGISTER_URL,
            )
        ],
        [
            InlineKeyboardButton(
                "✅ আমি ধাপ ১ শেষ করেছি",
                callback_data="step1_done",
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def build_step2_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "📱 অ্যান্ড্রয়েড অ্যাপ ডাউনলোড",
                url=ANDROID_APP_URL,
            )
        ],
        [
            InlineKeyboardButton(
                "🍎 iOS প্রোফাইল ডাউনলোড",
                url=IOS_APP_URL,
            )
        ],
        [
            InlineKeyboardButton(
                "✅ আমি ধাপ ২ শেষ করেছি",
                callback_data="step2_done",
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def build_step3_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_URL),
            InlineKeyboardButton("👍 Facebook", url=FB_URL),
        ],
        [
            InlineKeyboardButton("🛫 Telegram", url=TELEGRAM_CHANNEL_URL),
            InlineKeyboardButton("📞 WhatsApp", url=WHATSAPP_COMMUNITY_URL),
        ],
        [
            InlineKeyboardButton(
                "✅ আমি ধাপ ৩ শেষ করেছি",
                callback_data="step3_done",
            )
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def build_cs_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton(
                "💬 কাস্টমার সার্ভিসে স্ক্রিনশট পাঠান",
                url=CS_SUBMIT_SCREENSHOT_URL,
            )
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


# ========== SEND STEP FUNCTIONS ==========

async def send_step1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎰 *ধাপ ১ – রেজিস্টার করে ১০ ফ্রি স্পিন নিন*\n\n"
        "👉 \"রেজিস্টার\" বাটনে ক্লিক করে নতুন একাউন্ট খুলুন – "
        "সফল রেজিস্টারের পর পাবেন *১০ ফ্রি স্পিন*।\n\n"
        "রেজিস্টার শেষ হলে নিচের \"✅ আমি ধাপ ১ শেষ করেছি\" বাটনে ক্লিক করুন。\n\n"
        f"📘 GuideBook – {GUIDE_URL}"
    )
    msg = update.effective_message
    await msg.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_step1_keyboard(),
        disable_web_page_preview=True,
    )


async def send_step2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📱 *ধাপ ২ – অ্যাপ ডাউনলোড করে আরও ১০ ফ্রি স্পিন নিন*\n\n"
        "👉 নিচের Download App বাটনে ক্লিক করে অ্যান্ড্রয়েড বা iOS এর জন্য "
        "অ্যাপ ডাউনলোড ও ইনস্টল করুন, আপনার একাউন্ট দিয়ে লগইন করলেই "
        "*আরও ১০ ফ্রি স্পিন* পাবেন。\n\n"
        "অ্যাপ ডাউনলোড ও লগইন শেষ হলে \"✅ আমি ধাপ ২ শেষ করেছি\" বাটনে ক্লিক করুন。\n\n"
        f"📘 GuideBook – {GUIDE_URL}"
    )
    msg = update.effective_message
    await msg.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_step2_keyboard(),
        disable_web_page_preview=True,
    )


async def send_step3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💰 *ধাপ ৩ – Like & Share করে ২০০ টাকা (BDT) নিন*\n\n"
        "👉 নিচের YouTube / Facebook / Telegram / WhatsApp বাটনগুলোতে ক্লিক করে "
        "Like, Follow/Subscribe এবং Join করুন。\n"
        "প্রতিটি জায়গায় কাজ শেষ হলে স্ক্রিনশট নিয়ে রাখুন。\n\n"
        "সব কাজ শেষ হলে \"✅ আমি ধাপ ۳ শেষ করেছি\" বাটনে ক্লিক করুন。\n\n"
        f"📘 GuideBook – {GUIDE_URL}"
    )
    msg = update.effective_message
    await msg.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_step3_keyboard(),
        disable_web_page_preview=True,
    )


async def send_cs_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🎉 *অভিনন্দন! সব ধাপ শেষ হয়েছে।*\n\n"
        "এখন আপনার তোলা সব স্ক্রিনশট নিচের বাটনে ক্লিক করে "
        "আমাদের কাস্টমার সার্ভিসে পাঠিয়ে দিন。\n"
        "ভেরিফিকেশন শেষ হলে আপনি পাবেন *ফ্রি ২০০ টাকা (BDT)*。\n\n"
        f"📘 GuideBook – {GUIDE_URL}"
    )
    msg = update.effective_message
    await msg.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_cs_keyboard(),
        disable_web_page_preview=True,
    )


# ========== HANDLERS ==========

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 记录当前步骤（以后如果要做校验可以用）
    context.user_data["step"] = 1
    await send_step1(update, context)


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "step1_done":
        context.user_data["step"] = 2
        await send_step2(update, context)

    elif data == "step2_done":
        context.user_data["step"] = 3
        await send_step3(update, context)

    elif data == "step3_done":
        context.user_data["step"] = 4
        await send_cs_step(update, context)


# ========== MAIN ==========

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_callback))

    print("Step-by-step Bangla promo bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
