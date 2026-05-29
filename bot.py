from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler, CallbackQueryHandler

TOKEN = "8677431523:AAEi6j_XFxuji_EHo-q3sTrAWgpXEH5CfAk"

MENU, BANK_MENU, MELLI_MENU, MEHR_MENU, SEPAH_MENU = range(5)

main_menu = [
    ["🏦 تسهیلات بانکی", "📊 اعتبارسنجی(رتبه اعتباری)"],
    ["📋 توضیحات تکمیلی", "📞 تماس با ما"]
]

bank_menu = [
    ["🏛 تسهیلات بانک ملی"],
    ["🌸 تسهیلات بانک قرض‌الحسنه مهر"],
    ["⚔️ تسهیلات بانک سپه"],
    ["🏦 سایر بانک‌ها"],
    ["🔙 بازگشت"]
]

melli_menu = [
    ["💚 تسهیلات قرض‌الحسنه مهربانی"],
    ["💳 تسهیلات اعتبار ملی"],
    ["🔙 بازگشت"]
]

mehr_menu = [
    ["🌸 تسهیلات قرض‌الحسنه نیلوفر"],
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["🔙 بازگشت"]
]

sepah_menu = [
    ["💎 تسهیلات قرض‌الحسنه نگین امید"],
    ["🌟 تسهیلات قرض‌الحسنه زرین امید"],
    ["🔙 بازگشت"]
]

WELCOME = """
✨⚡️ 🌟 وام‌یار 🌟 ⚡️✨

به ربات وام‌یار خوش آمدید

امتیاز تسهیلات حاصل از سپرده‌گذاری می‌باشد.

با وام‌یار، نسبت به شرایط خود و نوع امتیازهای موجود در ربات اقدام به کسب اطلاعات از بخش تسهیلات بانکی، و در نهایت ثبت درخواست برای شروع مراحل تکمیلی اخذ وام اقدام کنید. در صورت نیاز به هر گونه راهنمایی بیشتر به بخش تماس با ما مراجعه کنید 🙏

پیش از هر اقدامی برای وام‌ها، برای اطلاع از رتبه اعتباری خود و استعلام رتبه، از لینک زیر استفاده کنید:
🔗 https://www.rade.ir/credit-scoring/

⚠️ اکثریت تسهیلات شرط رتبه اعتباری شخص و ضامن (در صورت نیاز)، رتبه‌های A، B، C می‌باشد.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME,
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )
    return MENU

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🏦 تسهیلات بانکی":
        await update.message.reply_text(
            "🏦 *تسهیلات بانکی*\n\nیک بانک را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    elif text == "📊 اعتبارسنجی(رتبه اعتباری)":
        await update.message.reply_text(
            "📊 *استعلام رتبه اعتباری*\n\n"
            "برای استعلام رتبه اعتباری خود از لینک زیر استفاده کنید:\n\n"
            "🔗 https://www.rade.ir/credit-scoring/\n\n"
            "کد ملی و شماره تماس خود را وارد کنید، کد پیامک را تایید کنید و نتیجه به شما پیامک می‌شود.\n\n"
            "💰 هزینه: ۹,۰۰۰ تومان\n\n"
            "⚠️ رتبه‌های A، B، C شرط اکثر تسهیلات می‌باشد.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        return MENU

    elif text == "📋 توضیحات تکمیلی":
        await update.message.reply_text(
            "📋 *توضیحات تکمیلی*\n\nبه زودی تکمیل می‌شود...",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        return MENU

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "📞 *تماس با ما*\n\nبه زودی تکمیل می‌شود...",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        return MENU

    return MENU

async def bank_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text(
            "منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        return MENU

    elif text == "🏛 تسهیلات بانک ملی":
        await update.message.reply_text(
            "🏛 *تسهیلات بانک ملی*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True)
        )
        return MELLI_MENU

    elif text == "🌸 تسهیلات بانک قرض‌الحسنه مهر":
        await update.message.reply_text(
            "🌸 *تسهیلات بانک قرض‌الحسنه مهر*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True)
        )
        return MEHR_MENU

    elif text == "⚔️ تسهیلات بانک سپه":
        await update.message.reply_text(
            "⚔️ *تسهیلات بانک سپه*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True)
        )
        return SEPAH_MENU

    elif text == "🏦 سایر بانک‌ها":
        await update.message.reply_text(
            "🏦 *سایر بانک‌ها*\n\nبه زودی تکمیل می‌شود...",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    return BANK_MENU

async def melli_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text(
            "🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    elif text == "💚 تسهیلات قرض‌الحسنه مهربانی":
        await update.message.reply_text(
            "💚 *تسهیلات قرض‌الحسنه مهربانی - بانک ملی*\n\n"
            "تسهیلات با کارمزد ۴٪ سالانه تا سقف ۳۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- رتبه اعتباری A یا B (شخص و یک ضامن)\n"
            "- چک دیجیتال فعال (شخص یا ضامن)\n"
            "- امضای دیجیتال فعال (شخص و ضامن)\n\n"
            "⚠️ پرداخت معوق مجاز نیست\n\n"
            "در صورت داشتن شرایط یا نیاز به اطلاعات بیشتر به بخش 📞 تماس با ما مراجعه کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True)
        )
        return MELLI_MENU

    elif text == "💳 تسهیلات اعتبار ملی":
        await update.message.reply_text(
            "💳 *تسهیلات اعتبار ملی - بانک ملی*\n\n"
            "تسهیلات با کارمزد ۲۳٪ سالانه تا سقف ۷۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- رتبه اعتباری A یا B (شخص و دو ضامن)\n"
            "- چک دیجیتال فعال (شخص یا ضامن)\n"
            "- امضای دیجیتال فعال (شخص و ضامن)\n\n"
            "⚠️ پرداخت معوق مجاز نیست\n\n"
            "در صورت داشتن شرایط یا نیاز به اطلاعات بیشتر به بخش 📞 تماس با ما مراجعه کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True)
        )
        return MELLI_MENU

    return MELLI_MENU

async def mehr_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text(
            "🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    elif text == "🌸 تسهیلات قرض‌الحسنه نیلوفر":
        await update.message.reply_text(
            "🌸 *تسهیلات قرض‌الحسنه نیلوفر - بانک مهر*\n\n"
            "تسهیلات با کارمزد ۴٪ سالانه تا سقف ۵۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- افتتاح حساب دیجیتال کیوبانک مهر\n"
            "- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)\n"
            "- تسهیلات بدون ضامن و قابل دریافت در چند مرحله تا سقف ۵۰۰ میلیون تومان می‌باشد\n\n"
            "در صورت نیاز به هر گونه راهنمایی و توضیحات بیشتر از بخش 📞 تماس با ما اقدام و ثبت درخواست کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True)
        )
        return MEHR_MENU

    elif text == "🌺 تسهیلات قرض‌الحسنه ارکیده":
        await update.message.reply_text(
            "🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک مهر*\n\n"
            "تسهیلات با کارمزد ۴٪ سالانه تا سقف ۴۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- افتتاح حساب دیجیتال کیوبانک مهر\n"
            "- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)\n"
            "- تسهیلات به صورت یک‌تیکه ۴۰۰ میلیون تومان انتقال داده می‌شود\n"
            "- یک ضامن با چک دیجیتال بانک مهر نیاز است\n\n"
            "💡 درخواست چک دیجیتال مهر با حساب ضامن از داخل کیوبانک به صورت غیرحضوری قابل انجام است.\n\n"
            "در صورت نیاز به هر گونه راهنمایی و توضیحات بیشتر از بخش 📞 تماس با ما اقدام و ثبت درخواست کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True)
        )
        return MEHR_MENU

    return MEHR_MENU

async def sepah_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text(
            "🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    elif text == "💎 تسهیلات قرض‌الحسنه نگین امید":
        await update.message.reply_text(
            "💎 *تسهیلات قرض‌الحسنه نگین امید - بانک سپه*\n\n"
            "تسهیلات با کارمزد ۲٪ سالانه با بازپرداخت ۱۲ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- افتتاح حساب قرض‌الحسنه نگین دیجیتال\n"
            "- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)\n\n"
            "✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.\n\n"
            "در صورت نیاز به هر گونه راهنمایی و توضیحات بیشتر از بخش 📞 تماس با ما اقدام و ثبت درخواست کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True)
        )
        return SEPAH_MENU

    elif text == "🌟 تسهیلات قرض‌الحسنه زرین امید":
        await update.message.reply_text(
            "🌟 *تسهیلات قرض‌الحسنه زرین امید - بانک سپه*\n\n"
            "تسهیلات با کارمزد ۴٪ سالانه با بازپرداخت ۱۲ ماهه\n\n"
            "📋 *شرایط:*\n"
            "- افتتاح حساب جاری زرین امید\n"
            "- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)\n\n"
            "✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.\n\n"
            "در صورت نیاز به هر گونه راهنمایی و توضیحات بیشتر از بخش 📞 تماس با ما اقدام و ثبت درخواست کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True)
        )
        return SEPAH_MENU

    return SEPAH_MENU

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler)],
            BANK_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, bank_menu_handler)],
            MELLI_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, melli_menu_handler)],
            MEHR_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, mehr_menu_handler)],
            SEPAH_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, sepah_menu_handler)],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    app.add_handler(conv_handler)
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()