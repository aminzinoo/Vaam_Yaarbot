from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

TOKEN = "8677431523:AAEi6j_XFxuji_EHo-q3sTrAWgpXEH5CfAk"

# مراحل مکالمه
MENU, GET_NAME, GET_PHONE, GET_MELLI, GET_PHOTO = range(5)

# منوی اصلی
main_menu = [
    ["📋 اطلاعات وام‌ها", "📝 ثبت درخواست"],
    ["📞 تماس با ما", "❓ راهنما"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! به ربات وام‌یار خوش آمدید 🏦\n\nاز منوی زیر انتخاب کنید:",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )
    return MENU

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📋 اطلاعات وام‌ها":
        await update.message.reply_text(
            "🏦 *وام‌های موجود:*\n\n"
            "1️⃣ *بانک ملی* - امتیاز وام مسکن\n"
            "مبلغ: تا ۱ میلیارد تومان\n"
            "بازپرداخت: ۱۲۰ ماه\n\n"
            "2️⃣ *بانک صادرات* - وام ازدواج\n"
            "مبلغ: تا ۳۰۰ میلیون تومان\n"
            "بازپرداخت: ۶۰ ماه\n\n"
            "3️⃣ *بانک مسکن* - امتیاز صندوق\n"
            "مبلغ: تا ۵۰۰ میلیون تومان\n"
            "بازپرداخت: ۱۸۰ ماه\n\n"
            "برای ثبت درخواست گزینه 📝 را انتخاب کنید",
            parse_mode='Markdown'
        )
        return MENU

    elif text == "📝 ثبت درخواست":
        await update.message.reply_text("لطفاً نام و نام خانوادگی خود را وارد کنید:")
        return GET_NAME

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "📞 *تماس با ما:*\n\n"
            "تلفن: ۰۹۱۲۰۰۰۰۰۰۰\n"
            "ساعت کاری: ۹ صبح تا ۶ عصر",
            parse_mode='Markdown'
        )
        return MENU

    elif text == "❓ راهنما":
        await update.message.reply_text(
            "راهنمای استفاده:\n\n"
            "1. اطلاعات وام‌ها را مشاهده کنید\n"
            "2. درخواست خود را ثبت کنید\n"
            "3. مدارک را ارسال کنید\n"
            "4. منتظر تماس کارشناس باشید"
        )
        return MENU

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("شماره موبایل خود را وارد کنید:")
    return GET_PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("کد ملی خود را وارد کنید:")
    return GET_MELLI

async def get_melli(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['melli'] = update.message.text
    await update.message.reply_text(
        "عکس کارت ملی خود را ارسال کنید 📷"
    )
    return GET_PHOTO

async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['photo'] = update.message.photo[-1].file_id
    name = context.user_data['name']
    phone = context.user_data['phone']
    melli = context.user_data['melli']
    
    await update.message.reply_text(
        f"✅ درخواست شما ثبت شد!\n\n"
        f"نام: {name}\n"
        f"موبایل: {phone}\n"
        f"کد ملی: {melli}\n\n"
        f"کارشناس ما در اسرع وقت با شما تماس می‌گیرد 🙏",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )
    return MENU

def main():
    app = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler)],
            GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            GET_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            GET_MELLI: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_melli)],
            GET_PHOTO: [MessageHandler(filters.PHOTO, get_photo)],
        },
        fallbacks=[CommandHandler('start', start)]
    )
    
    app.add_handler(conv_handler)
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()