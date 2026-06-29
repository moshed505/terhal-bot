from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "ضع_توكن_البوت_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🚖 اطلب رحلة")],
        [KeyboardButton("🧑‍✈️ تسجيل كابتن")],
    ]
    await update.message.reply_text(
        "مرحباً بك في ترحال 👋\nاختر الخدمة:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True),
    )

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🚖 اطلب رحلة":
        await update.message.reply_text(
            "📍 أرسل موقع الانطلاق باستخدام زر إرفاق الموقع."
        )

    elif text == "🧑‍✈️ تسجيل كابتن":
        await update.message.reply_text(
            "أرسل اسمك ورقم جوالك. الاشتراك الشهري 19 ريال."
        )

    else:
        await update.message.reply_text("استخدم الأزرار الموجودة بالأسفل.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages))

app.run_polling()
