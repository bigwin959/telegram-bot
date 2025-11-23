# pip install python-telegram-bot==21.4

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
BOT_TOKEN = "8299721660:AAGdgLFa2cTuIhpNqTHhcxHGspJlWaCjj-Y"   # ← 换成你的 Bot Token（⚠️ 建议重置）

# 真实链接（全部要以 https:// 开头）
REGISTER_URL = "https://channel1.bigwin959.com/register.html"

ANDROID_APP_URL = "https://images.738382910483.com/wsd-images-prod/bigbdtf7/app_pack/android/bigbdtf7_2.4.76_20251105095117.apk"
IOS_APP_URL = "https://images.738382910483.com/wsd-images-prod/bigbdtf7/app_pack/mobileconfig/bigbdtf7_2.4.3_20251105095116.mobileconfig"

FB_URL = "https://www.facebook.com/share/v/1ahKqXg3W7/"
YOUTUBE_URL = "https://www.youtube.com/@bigwin959official"
TIKTOK_URL = "https://vt.tiktok.com/ZSfhRqErW/"
WHATSAPP_COMMUNITY_URL = "https://chat.whatsapp.com/J1SnH9iCPvR7lyh7j4vNAO"
TELEGRAM_CHANNEL_URL = "https://t.me/bigwin959/11"

CS_WHATSAPP_URL = "https://wa.me/qr/Y5LGYED5VPXZE1"     # 如果客服用同一个群，可以共用
CS_TELEGRAM_URL = "https://t.me/Superbigwin959_bot" 
CS_LIVECHAT_URL = "https://www.bigwin619.com/"  # 没有就先随便填你网站

# 用户完成 STEP 3 后，点击按钮跳转到“提交截图拿 200 BDT”的 Telegram Bot
# 👉 把下面这个链接改成你要跳到的 另一个 Telegram Bot 链接
CS_SUBMIT_SCREENSHOT_URL = "https://t.me/Superbigwin959_bot"


# ========== /start：只显示选择语言 ==========

def build_language_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton("🇧🇩 বাংলা", callback_data="lang_bn")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        " ✨ Welcome to **BigWin9️⃣5️⃣9️⃣**!\n\n"
        "Please choose your language.\n\n"
        "✨ **বিগউইন৯৫৯-এ স্বাগতম!**\n\n"
        "দয়া করে আপনার ভাষা নির্বাচন করুন।"
    )

    if update.message:
        await update.message.reply_text(
            text,
            parse_mode="Markdown",
            reply_markup=build_language_keyboard(),
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            text,
            parse_mode="Markdown",
            reply_markup=build_language_keyboard(),
        )


# ========== 语言选好后，只出现 “Get 20 Free Spins” ==========

def build_lang_en_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("💲 Get 20 Free Spins + 200 BDT", callback_data="promo_en")],
        [InlineKeyboardButton("🔁 Change Language", callback_data="back_lang")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def show_lang_en_menu(query):
    text = (
        "✅ You selected **English**.\n\n"
        "✨Tap the button below⬇️ to see how to get **20 Free Spins + 💲200 BDT**✨"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_lang_en_menu(),
    )


def build_lang_bn_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("💲 ২০ ফ্রি স্পিন + ২০০ টাকা", callback_data="promo_bn")],
        [InlineKeyboardButton("🔁 ভাষা পরিবর্তন করুন", callback_data="back_lang")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def show_lang_bn_menu(query):
    text = (
        "✅ আপনি **বাংলা** নির্বাচন করেছেন।\n\n"
        "✨নিচের বাটনে ক্লিক ⬇️করে দেখুন কীভাবে **২০ ফ্রি স্পিন + 💲২০০ টাকা** পাবেন।✨"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_lang_bn_menu(),
    )


# ========== 点 Get 20 Free Spins 之后：STEP 风格 + 进度按钮 ==========

def build_promo_en_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("STEP 1️⃣ – Register", url=REGISTER_URL)],
        [
            InlineKeyboardButton("STEP 2️⃣ – Android App", url=ANDROID_APP_URL),
            InlineKeyboardButton("STEP 2️⃣ – iOS App", url=IOS_APP_URL),
        ],
        [InlineKeyboardButton("STEP 3️⃣ – Like & Share Tasks", callback_data="social_en")],
        [InlineKeyboardButton("📞 STEP 4️⃣ – Customer Service", callback_data="cs_en")],
        [InlineKeyboardButton("⬅️Back", callback_data="lang_en")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def send_promo_en(query):
    text = (
        "💲 **20 Free Spins + 200 BDT BONUS**\n\n"
        "🚦 **Follow these steps in order (1 → 4):**\n\n"
        "📌 **REGISTER**\n"
        "Tap ** STEP 1 – Register**, verify your **phone number**, and get **10 Free Spins**.\n\n"
        "📌 **APP DOWNLOAD**\n"
        "Tap **STEP 2 – Android App / iOS App** to download the app and get **10 more Free Spins instantly**.\n\n"
        "📌 **LIKE & SHARE**\n"
        "Tap **STEP 3 – Like & Share Tasks** and finish all Social Media tasks.\n\n"
        "🔓 **CUSTOMER SERVICE**\n"
        "Tap **💲 STEP 4 – Customer Service** and send your screenshots to claim **💲FREE 200 BDT**.\n\n"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_promo_en_keyboard(),
        disable_web_page_preview=True,
    )


def build_promo_bn_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(" ধাপ 1️⃣– রেজিস্টার", url=REGISTER_URL)],
        [
            InlineKeyboardButton(" ধাপ2️⃣ – অ্যান্ড্রয়েড অ্যাপ", url=ANDROID_APP_URL),
            InlineKeyboardButton(" ধাপ2️⃣ – আইওএস অ্যাপ", url=IOS_APP_URL),
        ],
        [InlineKeyboardButton("ধাপ 3️⃣ – Like & Share টাস্ক", callback_data="social_bn")],
        [InlineKeyboardButton("📞 ধাপ 4️⃣ – কাস্টমার সার্ভিস", callback_data="cs_bn")],
        [InlineKeyboardButton("⬅️ পিছনে যান", callback_data="lang_bn")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def send_promo_bn(query):
    text = (
        "💲 **২০ ফ্রি স্পিন + ২০০ টাকা বোনাস**\n\n"
        "🚦 **ধাপগুলো সিরিয়াল অনুযায়ী করুন (১ → ৪):**\n\n"
        "📌 **রেজিস্টার**\n"
        "নিচের ** ধাপ ১ – রেজিস্টার** বাটনে ক্লিক করে **ফোন নম্বর ভেরিফাই** করুন এবং **১০ ফ্রি স্পিন** নিন।\n\n"
        "📌 **অ্যাপ ডাউনলোড**\n"
        "**ধাপ ২ – অ্যান্ড্রয়েড অ্যাপ / আইওএস অ্যাপ** বাটনে ক্লিক করে অ্যাপ ডাউনলোড করুন এবং আরও **১০ ফ্রি স্পিন** পান।\n\n"
        "📌 **Like & Share**\n"
        "**ধাপ ৩ – Like & Share টাস্ক** বাটনে ক্লিক করে সব সোশ্যাল মিডিয়া টাস্ক সম্পন্ন করুন।\n\n"
        "🔓 **কাস্টমার সার্ভিস**\n"
        "**💲 ধাপ ৪ – কাস্টমার সার্ভিস** বাটনে ক্লিক করে স্ক্রিনশট পাঠান এবং **ফ্রি ২০০ টাকা (BDT)** নিন।\n\n"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_promo_bn_keyboard(),
        disable_web_page_preview=True,
    )


# ========== Like & Share：社交链接 + “Finish & Send Screenshot” 按钮 ==========

def build_social_en_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("👍 Facebook", url=FB_URL),
            InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_URL),
            InlineKeyboardButton("🎵 TikTok", url=TIKTOK_URL),
        ],
        [
            InlineKeyboardButton("🛫 Telegram", url=TELEGRAM_CHANNEL_URL),
            InlineKeyboardButton("📞 WhatsApp", url=WHATSAPP_COMMUNITY_URL),
        ],
        [
            InlineKeyboardButton(
                "✅ Finish & Send Screenshots to Get 200 BDT Free Bonus",
                url=CS_SUBMIT_SCREENSHOT_URL,  # 直接跳到“提交截图领 200 BDT”的 Telegram Bot
            )
        ],
        [InlineKeyboardButton("💬 Go to Customer Service", callback_data="cs_en")],
        [InlineKeyboardButton("⬅️ Back to Bonus", callback_data="promo_en")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def send_social_en(query):
    text = (
        "✨ **STEP 3 – Like, Share & Subscribe Tasks**\n\n"
        "✅ Please do ALL of the following using the buttons below:\n"
        "• Like & Share our posts\n"
        "• Follow / Subscribe our pages\n\n"
        "📸 After finishing, take screenshots.\n"
        "➡️ Then tap **✅ Finish & Send Screenshots to Get 200 BDT Free Bonus** "
        "to submit your proofs."
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_social_en_keyboard(),
        disable_web_page_preview=True,
    )


def build_social_bn_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📱 Facebook", url=FB_URL),
            InlineKeyboardButton("▶️ YouTube", url=YOUTUBE_URL),
            InlineKeyboardButton("🎵 TikTok", url=TIKTOK_URL),
        ],
        [
            InlineKeyboardButton("🛫 Telegram", url=TELEGRAM_CHANNEL_URL),
            InlineKeyboardButton("📞 WhatsApp", url=WHATSAPP_COMMUNITY_URL),
        ],
        [
            InlineKeyboardButton(
                "✅ স্ক্রিনশট পাঠিয়ে ফ্রি ২০০ টাকা বোনাস নিন",
                url=CS_SUBMIT_SCREENSHOT_URL,  # 同样跳到“提交截图领 200 BDT”的 Bot
            )
        ],
        [InlineKeyboardButton("💬 কাস্টমার সার্ভিসে যান", callback_data="cs_bn")],
        [InlineKeyboardButton("⬅️ বোনাস পেজে ফিরে যান", callback_data="promo_bn")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def send_social_bn(query):
    text = (
        "✨ **ধাপ ৩ – Like, Share & Subscribe টাস্ক**\n\n"
        "✅ নিচের বাটনগুলো ব্যবহার করে সব কাজগুলো করুনঃ\n"
        "• পোস্টে Like ও Share করুন\n"
        "• পেজ/চ্যানেল Follow বা Subscribe করুন\n\n"
        "📸 সব শেষ হলে স্ক্রিনশট নিন।\n"
        "➡️ তারপর **✅ স্ক্রিনশট পাঠিয়ে ফ্রি ২০০ টাকা বোনাস নিন** বাটনে ক্লিক করে "
        "আপনার প্রমাণ পাঠান।"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_social_bn_keyboard(),
        disable_web_page_preview=True,
    )


# ========== Customer Service ==========

def build_cs_keyboard(back_data: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("💬 WhatsApp CS", url=CS_WHATSAPP_URL),
            InlineKeyboardButton("📢 Telegram CS", url=CS_TELEGRAM_URL),
        ],
        [
            InlineKeyboardButton("🌐 Live Chat", url=CS_LIVECHAT_URL),
        ],
        [
            InlineKeyboardButton("⬅️ Back", callback_data=back_data),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def send_customer_service_en(query):
    text = (
        "💬 **STEP 4 – Customer Service (English)**\n\n"
        "Send your screenshots and any questions using the buttons below.\n\n"
        "💰 After verification, you will receive your **FREE 200 BDT**.\n\n"
        "📊 Progress: ✅ Step 1 / ✅ Step 2 / ✅ Step 3 / ⬜ Step 4 → *in progress*"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_cs_keyboard("promo_en"),
        disable_web_page_preview=True,
    )


async def send_customer_service_bn(query):
    text = (
        "💬 **ধাপ ৪ – কাস্টমার সার্ভিস (বাংলা)**\n\n"
        "নিচের বাটনগুলো ব্যবহার করে আপনার স্ক্রিনশট এবং যেকোনো প্রশ্ন সাপোর্ট টিমে পাঠান।\n\n"
        "💰 যাচাই শেষে আপনি পাবেন আপনার **ফ্রি ২০০ টাকা (BDT)**।\n\n"
        "📊 প্রগ্রেস: ✅ ধাপ ১ / ✅ ধাপ ২ / ✅ ধাপ ৩ / ⬜ ধাপ ৪ → *চলমান*"
    )
    await query.message.reply_text(
        text,
        parse_mode="Markdown",
        reply_markup=build_cs_keyboard("promo_bn"),
        disable_web_page_preview=True,
    )


# ========== CALLBACK 路由 ==========

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "lang_en":
        await show_lang_en_menu(query)
    elif data == "lang_bn":
        await show_lang_bn_menu(query)
    elif data == "back_lang":
        await start(update, context)
    elif data == "promo_en":
        await send_promo_en(query)
    elif data == "promo_bn":
        await send_promo_bn(query)
    elif data == "social_en":
        await send_social_en(query)
    elif data == "social_bn":
        await send_social_bn(query)
    elif data == "cs_en":
        await send_customer_service_en(query)
    elif data == "cs_bn":
        await send_customer_service_bn(query)


# ========== MAIN ==========

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(menu_handler))

    print("Bot v3 running with STEP progress...")
    app.run_polling()


if __name__ == "__main__":
    main()
