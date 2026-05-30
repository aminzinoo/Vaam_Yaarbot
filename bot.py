from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler, CallbackQueryHandler

# =============================================
# 🔑 تنظیمات
# =============================================
TOKEN = "8677431523:AAEi6j_XFxuji_EHo-q3sTrAWgpXEH5CfAk"

ADMIN_IDS = []  # آیدی عددی ادمین‌ها رو اینجا بذار

# =============================================
# حالت‌های مکالمه
# =============================================
(MENU, BANK_MENU, MELLI_MENU, MEHR_MENU, SEPAH_MENU,
 CREDIT_MENU, RESULT_MENU, GRADE_A_MENU, GRADE_B_MENU,
 GRADE_C_MENU, GRADE_D_MENU, TOZIHAT_MENU,
 SABT_MENU, MADAREK_MENU, WAITING_FRONT_ID, WAITING_BACK_ID,
 WAITING_SELFIE, LOAN_SELECT_MENU, WAITING_NAME, WAITING_NATIONAL_ID_REQ) = range(20)

# =============================================
# منوها
# =============================================
main_menu = [
    ["🔍 اعتبارسنجی", "🏦 شرایط تسهیلات"],
    ["📋 توضیحات تکمیلی", "📝 ثبت درخواست"],
    ["📞 تماس با ما"]
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

credit_menu = [
    ["🔍 استعلام رتبه اعتباری"],
    ["📋 مشاهده نتیجه + مشاوره وام‌یار"],
    ["🔙 بازگشت"]
]

result_menu = [
    ["🟢 رتبه A"],
    ["🔵 رتبه B"],
    ["🟡 رتبه C"],
    ["🔴 رتبه D و سایر"],
    ["🔙 بازگشت"]
]

grade_a_menu = [
    ["💚 تسهیلات قرض‌الحسنه مهربانی"],
    ["💳 تسهیلات اعتبار ملی"],
    ["🌸 تسهیلات قرض‌الحسنه نیلوفر"],
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["💎 تسهیلات قرض‌الحسنه نگین امید"],
    ["🌟 تسهیلات قرض‌الحسنه زرین امید"],
    ["🔙 بازگشت"]
]

grade_b_menu = [
    ["💚 تسهیلات قرض‌الحسنه مهربانی"],
    ["💳 تسهیلات اعتبار ملی"],
    ["🌸 تسهیلات قرض‌الحسنه نیلوفر"],
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["💎 تسهیلات قرض‌الحسنه نگین امید"],
    ["🌟 تسهیلات قرض‌الحسنه زرین امید"],
    ["🔙 بازگشت"]
]

grade_c_menu = [
    ["🌸 تسهیلات قرض‌الحسنه نیلوفر"],
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["💎 تسهیلات قرض‌الحسنه نگین امید"],
    ["🌟 تسهیلات قرض‌الحسنه زرین امید"],
    ["🔙 بازگشت"]
]

grade_d_menu = [
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["🔙 بازگشت"]
]

tozihat_menu = [
    ["💚 مهربانی", "💳 اعتبار ملی"],
    ["🌸 نیلوفر", "🌺 ارکیده"],
    ["💎 نگین امید", "🌟 زرین امید"],
    ["🔙 بازگشت"]
]

sabt_menu = [
    ["📎 بارگذاری مدارک"],
    ["🏦 انتخاب وام مد نظر"],
    ["🔙 بازگشت"]
]

loan_select_menu = [
    ["💚 تسهیلات قرض‌الحسنه مهربانی"],
    ["💳 تسهیلات اعتبار ملی"],
    ["🌸 تسهیلات قرض‌الحسنه نیلوفر"],
    ["🌺 تسهیلات قرض‌الحسنه ارکیده"],
    ["💎 تسهیلات قرض‌الحسنه نگین امید"],
    ["🌟 تسهیلات قرض‌الحسنه زرین امید"],
    ["🔙 بازگشت"]
]

# =============================================
# متون وام‌ها
# =============================================
WELCOME = """
✨⚡️ 🌟 وام‌ـیار 🌟 ⚡️✨

به ربات وام‌ـیار خوش آمدید 🙏

امتیاز تسهیلات حاصل از سپرده‌گذاری می‌باشد.

با وام‌ـیار، نسبت به شرایط خود و نوع امتیازهای موجود اقدام به کسب اطلاعات از بخش تسهیلات بانکی نمایید و در نهایت ثبت درخواست برای شروع مراحل تکمیلی اخذ وام اقدام کنید.

در صورت نیاز به هر گونه راهنمایی بیشتر به بخش تماس با ما مراجعه کنید 🙏

⚠️ اکثریت تسهیلات شرط رتبه اعتباری شخص و ضامن (در صورت نیاز)، رتبه‌های A، B، C می‌باشد.
"""

CREDIT_INTRO = """
📊 *اعتبارسنجی (رتبه اعتباری)*

⚠️ پیش از هر اقدامی برای دریافت وام، ابتدا نسبت به استعلام رتبه اعتباری خود اقدام کنید.

📌 *مراحل استعلام:*
۱. از لینک سامانه رده اقدام کنید
۲. کد ملی و شماره موبایل به نام خود وارد کنید
۳. کد پیامک‌شده را تأیید کنید
۴. نتیجه به شماره موبایل شما ارسال می‌شود

📎 پس از دریافت نتیجه، *فایل یا تصویر* آن را آماده کنید.

✅ سپس از بخش *مشاهده نتیجه + مشاوره* وام‌های متناسب با رتبه خود را مشاهده کنید.

💰 هزینه استعلام: ۸,۰۰۰ تومان
⚠️ رتبه‌های A، B، C شرط اکثر تسهیلات می‌باشد.
"""

# وام‌ها رتبه A
A_MEHRABANI = """
💚 *تسهیلات قرض‌الحسنه مهربانی - بانک ملی*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۳۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه

📋 *شرایط:*
- رتبه اعتباری A یا B (شخص)
- یک ضامن با حساب فعال بانک ملی (رتبه ضامن A تا D قابل قبول است)
- چک دیجیتال فعال (شخص یا ضامن)
- امضای دیجیتال فعال (شخص و ضامن)

⚠️ پرداخت معوق مجاز نیست
⚠️ (طبق قانون جدید فقط به گردش حساب A و B تسهیلات تعلق می‌گیرد)

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت داشتن شرایط به بخش 📞 تماس با ما مراجعه کنید.
"""

A_ETEBAR = """
💳 *تسهیلات اعتبار ملی - بانک ملی*

تسهیلات با کارمزد ۲۳٪ سالانه تا سقف ۷۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه

📋 *شرایط:*
- رتبه اعتباری A یا B (شخص)
- دو ضامن (رتبه ضامنین A تا D قابل قبول است)
- چک دیجیتال فعال (شخص یا ضامن)
- امضای دیجیتال فعال (شخص و ضامن)

⚠️ پرداخت معوق مجاز نیست
⚠️ (طبق قانون جدید فقط به گردش حساب A و B تسهیلات تعلق می‌گیرد)

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت داشتن شرایط به بخش 📞 تماس با ما مراجعه کنید.
"""

A_NILOOFAR = """
🌸 *تسهیلات قرض‌الحسنه نیلوفر - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۵۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات بدون ضامن و قابل دریافت در چند مرحله تا سقف ۵۰۰ میلیون تومان می‌باشد

✅ برای رتبه A نیاز به ضامن نیست

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

A_ORKIDE = """
🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۴۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات به صورت یک‌تیکه ۴۰۰ میلیون تومان انتقال داده می‌شود
- یک ضامن با چک دیجیتال بانک مهر نیاز است (رتبه ضامن A تا D قابل قبول است)

💡 درخواست چک دیجیتال مهر از داخل کیوبانک به صورت غیرحضوری قابل انجام است.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

A_NEGIN = """
💎 *تسهیلات قرض‌الحسنه نگین امید - بانک سپه*

تسهیلات با کارمزد ۲٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب قرض‌الحسنه نگین دیجیتال
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه A نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

A_ZARRIN = """
🌟 *تسهیلات قرض‌الحسنه زرین امید - بانک سپه*

تسهیلات با کارمزد ۴٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب جاری زرین امید
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه A نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

# وام‌ها رتبه B
B_MEHRABANI = """
💚 *تسهیلات قرض‌الحسنه مهربانی - بانک ملی*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۳۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه

📋 *شرایط:*
- رتبه اعتباری A یا B (شخص)
- یک ضامن با حساب فعال بانک ملی (رتبه ضامن باید A، B یا C باشد)
- چک دیجیتال فعال (شخص یا ضامن)
- امضای دیجیتال فعال (شخص و ضامن)

⚠️ پرداخت معوق مجاز نیست
⚠️ (طبق قانون جدید فقط به گردش حساب A و B تسهیلات تعلق می‌گیرد)

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت داشتن شرایط به بخش 📞 تماس با ما مراجعه کنید.
"""

B_ETEBAR = """
💳 *تسهیلات اعتبار ملی - بانک ملی*

تسهیلات با کارمزد ۲۳٪ سالانه تا سقف ۷۰۰ میلیون تومان با بازپرداخت ۳۶ ماهه

📋 *شرایط:*
- رتبه اعتباری A یا B (شخص)
- دو ضامن (رتبه ضامنین باید A، B یا C باشد)
- چک دیجیتال فعال (شخص یا ضامن)
- امضای دیجیتال فعال (شخص و ضامن)

⚠️ پرداخت معوق مجاز نیست
⚠️ (طبق قانون جدید فقط به گردش حساب A و B تسهیلات تعلق می‌گیرد)

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت داشتن شرایط به بخش 📞 تماس با ما مراجعه کنید.
"""

B_NILOOFAR = """
🌸 *تسهیلات قرض‌الحسنه نیلوفر - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۵۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات بدون ضامن و قابل دریافت در چند مرحله تا سقف ۵۰۰ میلیون تومان می‌باشد

✅ برای رتبه B نیاز به ضامن نیست

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

B_ORKIDE = """
🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۴۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات به صورت یک‌تیکه ۴۰۰ میلیون تومان انتقال داده می‌شود
- یک ضامن با چک دیجیتال بانک مهر (رتبه ضامن A، B یا C باشد)

💡 درخواست چک دیجیتال مهر از داخل کیوبانک به صورت غیرحضوری قابل انجام است.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

B_NEGIN = """
💎 *تسهیلات قرض‌الحسنه نگین امید - بانک سپه*

تسهیلات با کارمزد ۲٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب قرض‌الحسنه نگین دیجیتال
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه B نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

B_ZARRIN = """
🌟 *تسهیلات قرض‌الحسنه زرین امید - بانک سپه*

تسهیلات با کارمزد ۴٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب جاری زرین امید
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه B نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

# وام‌ها رتبه C
C_NILOOFAR = """
🌸 *تسهیلات قرض‌الحسنه نیلوفر - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۵۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات بدون ضامن و قابل دریافت در چند مرحله تا سقف ۵۰۰ میلیون تومان می‌باشد

✅ برای رتبه C نیاز به ضامن نیست

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

C_ORKIDE = """
🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۴۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات به صورت یک‌تیکه ۴۰۰ میلیون تومان انتقال داده می‌شود
- یک ضامن با چک دیجیتال بانک مهر (رتبه ضامن باید A یا B باشد)

⚠️ برای رتبه C ضامن با رتبه A یا B الزامی است
💡 درخواست چک دیجیتال مهر از داخل کیوبانک به صورت غیرحضوری قابل انجام است.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

C_NEGIN = """
💎 *تسهیلات قرض‌الحسنه نگین امید - بانک سپه*

تسهیلات با کارمزد ۲٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب قرض‌الحسنه نگین دیجیتال
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه C نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

C_ZARRIN = """
🌟 *تسهیلات قرض‌الحسنه زرین امید - بانک سپه*

تسهیلات با کارمزد ۴٪ سالانه با بازپرداخت ۱۲ ماهه

📋 *شرایط:*
- افتتاح حساب جاری زرین امید
- اعتبارسنجی از داخل امیدبانک بخش تسهیلات (استعلام ایرانیان)

✅ برای رتبه C نیاز به ضامن نیست
✅ پس از استعلام، رتبه‌های A، B، C قابلیت خرید امتیاز را دارند.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

# وام رتبه D
D_ORKIDE = """
🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک قرض‌الحسنه مهر*

تسهیلات با کارمزد ۴٪ سالانه تا سقف ۴۰۰ میلیون تومان با بازپرداخت ۲۴ ماهه

📋 *شرایط:*
- افتتاح حساب دیجیتال کیوبانک مهر
- اعتبارسنجی از داخل اپلیکیشن کیوبانک بخش تسهیلات (ظرف ۱ تا ۳ روز کاری)
- تسهیلات به صورت یک‌تیکه ۴۰۰ میلیون تومان انتقال داده می‌شود
- یک ضامن با چک دیجیتال بانک مهر (رتبه ضامن باید A، B یا C باشد)

⚠️ برای رتبه D و سایر، ضامن با رتبه A، B یا C الزامی است
💡 در صورت رد شدن اعتبارسنجی داخل اپلیکیشن کیوبانک، همچنان امکان دریافت این تسهیلات وجود دارد.
💡 درخواست چک دیجیتال مهر از داخل کیوبانک به صورت غیرحضوری قابل انجام است.

💬 برای اطلاع از قیمت روز امتیاز با ادمین تماس بگیرید.
در صورت نیاز به راهنمایی به بخش 📞 تماس با ما مراجعه کنید.
"""

# جدول خلاصه توضیحات تکمیلی هر وام
TOZIHAT_MEHRABANI = """
💚 *تسهیلات قرض‌الحسنه مهربانی - بانک ملی*

┌─────────────────────────┐
│ 💰 سقف وام: ۳۰۰ میلیون تومان   │
│ 📅 بازپرداخت: ۳۶ ماهه          │
│ 📊 کارمزد: ۴٪ سالانه           │
│ 👥 ضامن: ۱ نفر (بانک ملی)      │
│ 🏦 بانک: ملی                    │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی و شناسنامه (شخص و ضامن)
- چک دیجیتال فعال
- امضای دیجیتال فعال
- رتبه اعتباری A یا B

⚠️ رتبه ضامن: A تا D قابل قبول (برای رتبه B متقاضی، ضامن باید A، B یا C باشد)
⚠️ طبق قانون جدید فقط به گردش حساب A و B تعلق می‌گیرد

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_ETEBAR = """
💳 *تسهیلات اعتبار ملی - بانک ملی*

┌─────────────────────────┐
│ 💰 سقف وام: ۷۰۰ میلیون تومان   │
│ 📅 بازپرداخت: ۳۶ ماهه          │
│ 📊 کارمزد: ۲۳٪ سالانه          │
│ 👥 ضامن: ۲ نفر                  │
│ 🏦 بانک: ملی                    │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی و شناسنامه (شخص و ضامنین)
- چک دیجیتال فعال
- امضای دیجیتال فعال
- رتبه اعتباری A یا B

⚠️ رتبه ضامنین: A تا D (برای رتبه B متقاضی، ضامنین باید A، B یا C باشند)
⚠️ طبق قانون جدید فقط به گردش حساب A و B تعلق می‌گیرد

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_NILOOFAR = """
🌸 *تسهیلات قرض‌الحسنه نیلوفر - بانک مهر*

┌─────────────────────────┐
│ 💰 سقف وام: ۵۰۰ میلیون تومان   │
│ 📅 بازپرداخت: ۲۴ ماهه          │
│ 📊 کارمزد: ۴٪ سالانه           │
│ 👥 ضامن: نیاز نیست (A,B,C)     │
│ 🏦 بانک: قرض‌الحسنه مهر        │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی
- افتتاح حساب کیوبانک مهر
- اعتبارسنجی از داخل اپ کیوبانک

✅ قابل دریافت در چند مرحله
✅ بدون ضامن برای رتبه‌های A، B، C

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_ORKIDE = """
🌺 *تسهیلات قرض‌الحسنه ارکیده - بانک مهر*

┌─────────────────────────┐
│ 💰 سقف وام: ۴۰۰ میلیون تومان   │
│ 📅 بازپرداخت: ۲۴ ماهه          │
│ 📊 کارمزد: ۴٪ سالانه           │
│ 👥 ضامن: ۱ نفر (چک دیجیتال مهر)│
│ 🏦 بانک: قرض‌الحسنه مهر        │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی
- افتتاح حساب کیوبانک مهر
- چک دیجیتال بانک مهر (ضامن)
- اعتبارسنجی از داخل اپ کیوبانک

⚠️ رتبه ضامن: A تا D (برای رتبه C متقاضی، ضامن باید A یا B باشد)
💡 یک‌جا ۴۰۰ میلیون انتقال می‌شود
💡 در صورت رد اعتبارسنجی داخل اپ هم قابل دریافت است

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_NEGIN = """
💎 *تسهیلات قرض‌الحسنه نگین امید - بانک سپه*

┌─────────────────────────┐
│ 💰 سقف وام: بر اساس امتیاز      │
│ 📅 بازپرداخت: ۱۲ ماهه          │
│ 📊 کارمزد: ۲٪ سالانه           │
│ 👥 ضامن: نیاز نیست (A,B,C)     │
│ 🏦 بانک: سپه                    │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی
- افتتاح حساب نگین دیجیتال
- اعتبارسنجی از امیدبانک (استعلام ایرانیان)

✅ بدون ضامن برای رتبه‌های A، B، C
✅ پس از استعلام، قابلیت خرید امتیاز فعال می‌شود

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_ZARRIN = """
🌟 *تسهیلات قرض‌الحسنه زرین امید - بانک سپه*

┌─────────────────────────┐
│ 💰 سقف وام: بر اساس امتیاز      │
│ 📅 بازپرداخت: ۱۲ ماهه          │
│ 📊 کارمزد: ۴٪ سالانه           │
│ 👥 ضامن: نیاز نیست (A,B,C)     │
│ 🏦 بانک: سپه                    │
└─────────────────────────┘

📋 *مدارک لازم:*
- کارت ملی
- افتتاح حساب جاری زرین امید
- اعتبارسنجی از امیدبانک (استعلام ایرانیان)

✅ بدون ضامن برای رتبه‌های A، B، C
✅ پس از استعلام، قابلیت خرید امتیاز فعال می‌شود

💬 قیمت امتیاز روزانه آپدیت می‌شود - برای اطلاع از قیمت با ادمین تماس بگیرید.
"""

TOZIHAT_DARBARE = """
📌 *درباره وام‌ـیار*

هدف از ربات وام‌ـیار، تهیه امتیاز برای اشخاص بدون واسطه است.

شرایط برای متقاضیان به صورت تک‌نفره، هم به صورت *نقد* و هم *پس‌پرداخت از روی وام* در دسترس می‌باشد.

این شرایط بستگی به شهر متقاضی و شرایط تیم وام‌ـیار دارد و از طریق ادمین قابل بحث و مشخص شدن است.

برای اطلاعات بیشتر به بخش 📞 تماس با ما مراجعه کنید.
"""

# =============================================
# هندلرها
# =============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME,
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )
    return MENU

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🏦 شرایط تسهیلات":
        await update.message.reply_text(
            "🏦 *شرایط تسهیلات*\n\nیک بانک را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True)
        )
        return BANK_MENU

    elif text == "🔍 اعتبارسنجی":
        await update.message.reply_text(
            CREDIT_INTRO,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(credit_menu, resize_keyboard=True)
        )
        return CREDIT_MENU

    elif text == "📋 توضیحات تکمیلی":
        await update.message.reply_text(
            "📋 *توضیحات تکمیلی*\n\nیکی از وام‌ها را برای مشاهده جدول کامل انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(tozihat_menu, resize_keyboard=True)
        )
        return TOZIHAT_MENU

    elif text == "📝 ثبت درخواست":
        await update.message.reply_text(
            "📝 *ثبت درخواست*\n\nیکی از گزینه‌های زیر را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sabt_menu, resize_keyboard=True)
        )
        return SABT_MENU

    elif text == "📞 تماس با ما":
        await update.message.reply_text(
            "📞 *تماس با ما*\n\n"
            "برای ارتباط با تیم وام‌ـیار با یکی از ادمین‌ها تماس بگیرید:\n\n"
            "👤 وام‌یار ۱: به زودی\n"
            "👤 وام‌یار ۲: به زودی\n"
            "👤 وام‌یار ۳: به زودی\n\n"
            "⏰ ساعات پاسخگویی: روزهای کاری",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        return MENU

    return MENU

# =============================================
# هندلر اعتبارسنجی
# =============================================
async def credit_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    elif text == "🔍 استعلام رتبه اعتباری":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔗 استعلام از سامانه رده", url="https://www.rade.ir/credit-scoring/")]
        ])
        await update.message.reply_text(
            "📊 *استعلام رتبه اعتباری*\n\n"
            "برای استعلام رتبه اعتباری روی دکمه زیر کلیک کنید:\n\n"
            "📌 *مراحل:*\n"
            "۱. کد ملی و شماره موبایل خود را وارد کنید\n"
            "۲. کد پیامک‌شده را تأیید کنید\n"
            "۳. نتیجه به شماره موبایل شما ارسال می‌شود\n\n"
            "💰 هزینه: ۸,۰۰۰ تومان\n\n"
            "📎 پس از دریافت نتیجه، *فایل یا تصویر* آن را آماده کنید و به بخش *مشاهده نتیجه + مشاوره* مراجعه کنید.",
            parse_mode='Markdown',
            reply_markup=keyboard
        )
        await update.message.reply_text("بازگشت به منو:",
            reply_markup=ReplyKeyboardMarkup(credit_menu, resize_keyboard=True))
        return CREDIT_MENU

    elif text == "📋 مشاهده نتیجه + مشاوره وام‌یار":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 پرداخت ۳۹,۰۰۰ تومان", url="https://YOUR-PAYMENT-LINK")]
        ])
        await update.message.reply_text(
            "📋 *مشاوره وام‌ـیار*\n\n"
            "💰 قیمت: ~~۴۴,۰۰۰~~ *۳۹,۰۰۰ تومان* (با تخفیف ویژه)\n\n"
            "✅ *چی دریافت می‌کنید:*\n"
            "• تفسیر کامل رتبه اعتباری شما\n"
            "• معرفی تمام وام‌های متناسب با رتبه‌تان\n"
            "• راهنمایی کامل شرایط و مدارک هر وام\n"
            "• راهنمایی انتخاب ضامن مناسب\n\n"
            "🔒 اطلاعات شما کاملاً محرمانه است\n\n"
            "برای فعال‌سازی مشاوره، پرداخت را انجام دهید:",
            parse_mode='Markdown',
            reply_markup=keyboard
        )
        await update.message.reply_text(
            "✅ پس از پرداخت، دکمه تأیید را بزنید:",
            reply_markup=ReplyKeyboardMarkup(
                [["✅ تأیید پرداخت"], ["🔙 بازگشت"]],
                resize_keyboard=True
            )
        )
        return CREDIT_MENU

    elif text == "✅ تأیید پرداخت":
        await update.message.reply_text(
            "✅ *پرداخت تأیید شد!*\n\n"
            "🎉 به بخش مشاوره وام‌ـیار خوش آمدید!\n\n"
            "رتبه اعتباری خود را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(result_menu, resize_keyboard=True)
        )
        return RESULT_MENU

    return CREDIT_MENU

# =============================================
# هندلر منوی نتیجه رتبه
# =============================================
async def result_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    elif text == "🟢 رتبه A":
        await update.message.reply_text(
            "🟢 *رتبه A — بهترین رتبه اعتباری*\n\n"
            "تبریک! با رتبه A تمام تسهیلات موجود به شما تعلق می‌گیرد.\n\n"
            "یکی از وام‌های زیر را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_a_menu, resize_keyboard=True))
        return GRADE_A_MENU

    elif text == "🔵 رتبه B":
        await update.message.reply_text(
            "🔵 *رتبه B — رتبه اعتباری خوب*\n\n"
            "با رتبه B تمام تسهیلات موجود به شما تعلق می‌گیرد.\n\n"
            "⚠️ در صورت نیاز به ضامن، رتبه ضامن باید A، B یا C باشد.\n\n"
            "یکی از وام‌های زیر را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_b_menu, resize_keyboard=True))
        return GRADE_B_MENU

    elif text == "🟡 رتبه C":
        await update.message.reply_text(
            "🟡 *رتبه C — رتبه اعتباری متوسط*\n\n"
            "❌ تسهیلات بانک ملی فعلاً به رتبه C تعلق نمی‌گیرد.\n"
            "⚠️ در صورت نیاز به ضامن، رتبه ضامن باید A یا B باشد.\n\n"
            "یکی از وام‌های زیر را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_c_menu, resize_keyboard=True))
        return GRADE_C_MENU

    elif text == "🔴 رتبه D و سایر":
        await update.message.reply_text(
            "🔴 *رتبه D و سایر*\n\n"
            "❌ تسهیلات قرض‌الحسنه مهربانی - بانک ملی\n"
            "❌ تسهیلات اعتبار ملی - بانک ملی\n"
            "❌ تسهیلات قرض‌الحسنه نیلوفر - بانک مهر\n"
            "✅ تسهیلات قرض‌الحسنه ارکیده - بانک مهر\n"
            "❌ تسهیلات قرض‌الحسنه نگین امید - بانک سپه\n"
            "❌ تسهیلات قرض‌الحسنه زرین امید - بانک سپه\n\n"
            "برای اطلاعات بیشتر انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_d_menu, resize_keyboard=True))
        return GRADE_D_MENU

    return RESULT_MENU

# =============================================
# هندلر رتبه A
# =============================================
async def grade_a_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("انتخاب رتبه:",
            reply_markup=ReplyKeyboardMarkup(result_menu, resize_keyboard=True))
        return RESULT_MENU
    msgs = {
        "💚 تسهیلات قرض‌الحسنه مهربانی": A_MEHRABANI,
        "💳 تسهیلات اعتبار ملی": A_ETEBAR,
        "🌸 تسهیلات قرض‌الحسنه نیلوفر": A_NILOOFAR,
        "🌺 تسهیلات قرض‌الحسنه ارکیده": A_ORKIDE,
        "💎 تسهیلات قرض‌الحسنه نگین امید": A_NEGIN,
        "🌟 تسهیلات قرض‌الحسنه زرین امید": A_ZARRIN,
    }
    if text in msgs:
        await update.message.reply_text(msgs[text], parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_a_menu, resize_keyboard=True))
    return GRADE_A_MENU

# =============================================
# هندلر رتبه B
# =============================================
async def grade_b_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("انتخاب رتبه:",
            reply_markup=ReplyKeyboardMarkup(result_menu, resize_keyboard=True))
        return RESULT_MENU
    msgs = {
        "💚 تسهیلات قرض‌الحسنه مهربانی": B_MEHRABANI,
        "💳 تسهیلات اعتبار ملی": B_ETEBAR,
        "🌸 تسهیلات قرض‌الحسنه نیلوفر": B_NILOOFAR,
        "🌺 تسهیلات قرض‌الحسنه ارکیده": B_ORKIDE,
        "💎 تسهیلات قرض‌الحسنه نگین امید": B_NEGIN,
        "🌟 تسهیلات قرض‌الحسنه زرین امید": B_ZARRIN,
    }
    if text in msgs:
        await update.message.reply_text(msgs[text], parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_b_menu, resize_keyboard=True))
    return GRADE_B_MENU

# =============================================
# هندلر رتبه C
# =============================================
async def grade_c_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("انتخاب رتبه:",
            reply_markup=ReplyKeyboardMarkup(result_menu, resize_keyboard=True))
        return RESULT_MENU
    msgs = {
        "🌸 تسهیلات قرض‌الحسنه نیلوفر": C_NILOOFAR,
        "🌺 تسهیلات قرض‌الحسنه ارکیده": C_ORKIDE,
        "💎 تسهیلات قرض‌الحسنه نگین امید": C_NEGIN,
        "🌟 تسهیلات قرض‌الحسنه زرین امید": C_ZARRIN,
    }
    if text in msgs:
        await update.message.reply_text(msgs[text], parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_c_menu, resize_keyboard=True))
    return GRADE_C_MENU

# =============================================
# هندلر رتبه D
# =============================================
async def grade_d_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("انتخاب رتبه:",
            reply_markup=ReplyKeyboardMarkup(result_menu, resize_keyboard=True))
        return RESULT_MENU
    if text == "🌺 تسهیلات قرض‌الحسنه ارکیده":
        await update.message.reply_text(D_ORKIDE, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(grade_d_menu, resize_keyboard=True))
    return GRADE_D_MENU

# =============================================
# هندلر توضیحات تکمیلی
# =============================================
async def tozihat_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU
    msgs = {
        "💚 مهربانی": TOZIHAT_MEHRABANI,
        "💳 اعتبار ملی": TOZIHAT_ETEBAR,
        "🌸 نیلوفر": TOZIHAT_NILOOFAR,
        "🌺 ارکیده": TOZIHAT_ORKIDE,
        "💎 نگین امید": TOZIHAT_NEGIN,
        "🌟 زرین امید": TOZIHAT_ZARRIN,
    }
    if text in msgs:
        await update.message.reply_text(msgs[text], parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(tozihat_menu, resize_keyboard=True))
        await update.message.reply_text(
            TOZIHAT_DARBARE,
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(tozihat_menu, resize_keyboard=True)
        )
    return TOZIHAT_MENU

# =============================================
# هندلر ثبت درخواست
# =============================================
async def sabt_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    elif text == "📎 بارگذاری مدارک":
        await update.message.reply_text(
            "📎 *بارگذاری مدارک*\n\n"
            "لطفاً *تصویر جلوی کارت ملی* خود را ارسال کنید:\n\n"
            "⚠️ تصویر باید واضح و خوانا باشد",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup([["🔙 انصراف"]], resize_keyboard=True)
        )
        return WAITING_FRONT_ID

    elif text == "🏦 انتخاب وام مد نظر":
        await update.message.reply_text(
            "🏦 *انتخاب وام مد نظر*\n\n"
            "ابتدا *نام و نام خانوادگی* خود را وارد کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup([["🔙 انصراف"]], resize_keyboard=True)
        )
        return WAITING_NAME

    return SABT_MENU

# =============================================
# دریافت مدارک
# =============================================
async def waiting_front_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 انصراف":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    if update.message.photo:
        context.user_data['front_id'] = update.message.photo[-1].file_id
        await update.message.reply_text(
            "✅ تصویر جلو دریافت شد!\n\n"
            "حالا *تصویر پشت کارت ملی* خود را ارسال کنید:",
            parse_mode='Markdown'
        )
        return WAITING_BACK_ID
    else:
        await update.message.reply_text("❌ لطفاً یک تصویر ارسال کنید:")
        return WAITING_FRONT_ID

async def waiting_back_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 انصراف":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    if update.message.photo:
        context.user_data['back_id'] = update.message.photo[-1].file_id
        await update.message.reply_text(
            "✅ تصویر پشت دریافت شد!\n\n"
            "✅ *مدارک شما با موفقیت ثبت شد!*\n\n"
            "تیم وام‌ـیار در اسرع وقت با شما تماس خواهد گرفت.\n"
            "همچنین می‌توانید از بخش 📞 تماس با ما پیگیری کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )
        # ارسال به ادمین‌ها
        user = update.message.from_user
        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    admin_id,
                    f"📎 *مدارک جدید*\n\n"
                    f"👤 کاربر: {user.full_name}\n"
                    f"🆔 آیدی: @{user.username or user.id}",
                    parse_mode='Markdown'
                )
                await context.bot.send_photo(admin_id, context.user_data['front_id'],
                    caption="جلوی کارت ملی")
                await context.bot.send_photo(admin_id, context.user_data['back_id'],
                    caption="پشت کارت ملی")
            except:
                pass
        return MENU
    else:
        await update.message.reply_text("❌ لطفاً یک تصویر ارسال کنید:")
        return WAITING_BACK_ID

# =============================================
# دریافت اطلاعات انتخاب وام
# =============================================
async def waiting_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 انصراف":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU
    context.user_data['full_name'] = update.message.text
    await update.message.reply_text(
        f"✅ نام: *{update.message.text}*\n\n"
        "حالا *کد ملی* خود را وارد کنید:",
        parse_mode='Markdown'
    )
    return WAITING_NATIONAL_ID_REQ

async def waiting_national_id_req(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 انصراف":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    text = update.message.text
    if not text.isdigit() or len(text) != 10:
        await update.message.reply_text("❌ کد ملی نامعتبر است! لطفاً ۱۰ رقم وارد کنید:")
        return WAITING_NATIONAL_ID_REQ

    context.user_data['national_id'] = text
    await update.message.reply_text(
        f"✅ کد ملی: *{text}*\n\n"
        "حالا *تصویر کارت ملی* خود را ارسال کنید:",
        parse_mode='Markdown'
    )
    return WAITING_SELFIE

async def waiting_selfie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 انصراف":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    if update.message.photo:
        context.user_data['selfie'] = update.message.photo[-1].file_id
        await update.message.reply_text(
            "✅ تصویر دریافت شد!\n\n"
            "🏦 حالا *وام مد نظر* خود را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(loan_select_menu, resize_keyboard=True)
        )
        return LOAN_SELECT_MENU
    else:
        await update.message.reply_text("❌ لطفاً یک تصویر ارسال کنید:")
        return WAITING_SELFIE

async def loan_select_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU

    loans = [
        "💚 تسهیلات قرض‌الحسنه مهربانی",
        "💳 تسهیلات اعتبار ملی",
        "🌸 تسهیلات قرض‌الحسنه نیلوفر",
        "🌺 تسهیلات قرض‌الحسنه ارکیده",
        "💎 تسهیلات قرض‌الحسنه نگین امید",
        "🌟 تسهیلات قرض‌الحسنه زرین امید",
    ]

    if text in loans:
        context.user_data['selected_loan'] = text
        user = update.message.from_user
        full_name = context.user_data.get('full_name', '-')
        national_id = context.user_data.get('national_id', '-')

        await update.message.reply_text(
            f"✅ *درخواست شما ثبت شد!*\n\n"
            f"👤 نام: {full_name}\n"
            f"🪪 کد ملی: {national_id}\n"
            f"🏦 وام انتخابی: {text}\n\n"
            f"تیم وام‌ـیار در اسرع وقت با شما تماس خواهد گرفت.\n"
            f"همچنین می‌توانید از بخش 📞 تماس با ما پیگیری کنید.",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

        # ارسال به ادمین‌ها
        for admin_id in ADMIN_IDS:
            try:
                await context.bot.send_message(
                    admin_id,
                    f"📝 *درخواست وام جدید*\n\n"
                    f"👤 نام: {full_name}\n"
                    f"🪪 کد ملی: {national_id}\n"
                    f"🏦 وام: {text}\n"
                    f"📱 آیدی: @{user.username or user.id}",
                    parse_mode='Markdown'
                )
                if context.user_data.get('selfie'):
                    await context.bot.send_photo(admin_id,
                        context.user_data['selfie'],
                        caption=f"تصویر کارت ملی - {full_name}")
            except:
                pass
        return MENU

    return LOAN_SELECT_MENU

# =============================================
# هندلرهای شرایط تسهیلات (منوی بانک‌ها)
# =============================================
async def bank_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("منوی اصلی:",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))
        return MENU
    elif text == "🏛 تسهیلات بانک ملی":
        await update.message.reply_text("🏛 *تسهیلات بانک ملی*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True))
        return MELLI_MENU
    elif text == "🌸 تسهیلات بانک قرض‌الحسنه مهر":
        await update.message.reply_text("🌸 *تسهیلات بانک قرض‌الحسنه مهر*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True))
        return MEHR_MENU
    elif text == "⚔️ تسهیلات بانک سپه":
        await update.message.reply_text("⚔️ *تسهیلات بانک سپه*\n\nنوع تسهیلات را انتخاب کنید:",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True))
        return SEPAH_MENU
    elif text == "🏦 سایر بانک‌ها":
        await update.message.reply_text("🏦 *سایر بانک‌ها*\n\nبه زودی تکمیل می‌شود...",
            parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True))
        return BANK_MENU
    return BANK_MENU

async def melli_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True))
        return BANK_MENU
    elif text == "💚 تسهیلات قرض‌الحسنه مهربانی":
        await update.message.reply_text(A_MEHRABANI, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True))
    elif text == "💳 تسهیلات اعتبار ملی":
        await update.message.reply_text(A_ETEBAR, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(melli_menu, resize_keyboard=True))
    return MELLI_MENU

async def mehr_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True))
        return BANK_MENU
    elif text == "🌸 تسهیلات قرض‌الحسنه نیلوفر":
        await update.message.reply_text(A_NILOOFAR, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True))
    elif text == "🌺 تسهیلات قرض‌الحسنه ارکیده":
        await update.message.reply_text(A_ORKIDE, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(mehr_menu, resize_keyboard=True))
    return MEHR_MENU

async def sepah_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🔙 بازگشت":
        await update.message.reply_text("🏦 تسهیلات بانکی:",
            reply_markup=ReplyKeyboardMarkup(bank_menu, resize_keyboard=True))
        return BANK_MENU
    elif text == "💎 تسهیلات قرض‌الحسنه نگین امید":
        await update.message.reply_text(A_NEGIN, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True))
    elif text == "🌟 تسهیلات قرض‌الحسنه زرین امید":
        await update.message.reply_text(A_ZARRIN, parse_mode='Markdown',
            reply_markup=ReplyKeyboardMarkup(sepah_menu, resize_keyboard=True))
    return SEPAH_MENU

# =============================================
# اجرای ربات
# =============================================
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
            CREDIT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, credit_menu_handler)],
            RESULT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, result_menu_handler)],
            GRADE_A_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, grade_a_handler)],
            GRADE_B_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, grade_b_handler)],
            GRADE_C_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, grade_c_handler)],
            GRADE_D_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, grade_d_handler)],
            TOZIHAT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, tozihat_menu_handler)],
            SABT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, sabt_menu_handler)],
            WAITING_FRONT_ID: [
                MessageHandler(filters.PHOTO, waiting_front_id),
                MessageHandler(filters.TEXT, waiting_front_id)
            ],
            WAITING_BACK_ID: [
                MessageHandler(filters.PHOTO, waiting_back_id),
                MessageHandler(filters.TEXT, waiting_back_id)
            ],
            WAITING_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, waiting_name)],
            WAITING_NATIONAL_ID_REQ: [MessageHandler(filters.TEXT & ~filters.COMMAND, waiting_national_id_req)],
            WAITING_SELFIE: [
                MessageHandler(filters.PHOTO, waiting_selfie),
                MessageHandler(filters.TEXT, waiting_selfie)
            ],
            LOAN_SELECT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, loan_select_handler)],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    app.add_handler(conv_handler)
    print("ربات وام‌یار در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()
