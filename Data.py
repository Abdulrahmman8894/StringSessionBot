from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ مرحبـاً بـك عزيـزي {}

  📮 ¦ في بوت 📬 {}


🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : MR_X_N_3
 
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 ابدأ بتوليد الجلسة 🔥", callback_data="انشاء")], 
        [InlineKeyboardButton(text="🏠 رجـــوع 🏠", callback_data="الصفحة الرئيسية")]
    ]
    
        generate_button = [
        [InlineKeyboardButton("🔥 ابدأ بتوليد الجلسة 🔥", callback_data="انشاء")]
    ]
        
    # Rest Buttons
    buttons  = [
        [InlineKeyboardButton("🔥 ابدأ بتوليد الجلسة 🔥", callback_data="انشاء")],
        [InlineKeyboardButton("✨ حالة البوت والمزيد من الروبوتات ✨", url="https://t.me/MR_X_N_3")],
        [
            InlineKeyboardButton("كيف تستعمل ❔", callback_data="مساعدة"),
            InlineKeyboardButton("🎪 حول 🎪", callback_data="حول")
        ],
        [InlineKeyboardButton("♥ المزيد من الروبوتات المذهلة ♥", url="https://t.me/MR_X_N_3")],
    ]

    # كـيف يـمكنـك اسـتخدامـي
    HELP = """
✨ **كـيف تستخـدمني** ✨

/about - حول البوت
/help - لتسوي روحك كلشي متعرف
/start - حتى تشغل البوت
/generate - حتى تبدا بأستخراج البوت
/cancel - لألغاء الاستخراج
/restart - اعادة تشغيل البوت
"""

    # حـول
    ABOUT = """
**حـول البوت . ** 

 بـوت استخـراج كـود تيرمكـس خـاص بســورس المـسـتـر 

قناة البوت: @MR_X_N_3

مصدر البوت : [Click Here](https://github.com/Abdulrahmman8894/StringSessionBot)

استخدم البوت : [Pyrogram](docs.pyrogram.org)

لغة البوت : [Python](www.python.org)

مطور البوت : https://t.me/MR_X_N_3
    """
