from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
👋 ¦ مرحبـاً بـك عزيـزي  {}
✠━━━━━━━━❖━━━━━━━━━✠
{} 📮 ¦ في بوت 📬!
━━━━━━━━━━━━━━━━━━━
🕹 ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس والبايروجرام تم انشـاء هـذا البـوت بواسطـة : @MR_X_10
✠━━━━━━━━❖━━━━━━━━━✠

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 ⚜️¦ بدأ استخراج الكود 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="⚜️¦ رجــوع", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 ⚜️¦ بدأ استخراج الكود 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 ⚜️¦ بدأ استخراج الكود 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("¦📬 كيف تستخدمني", callback_data="help"),
            InlineKeyboardButton("⚜️ ¦ حــول", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **📬 ¦ كـيف تستخـدمني** ✨

× /about - حول البوت
× /help - لتسوي روحك كلشي متعرف
× /start - حتى تشغل البوت
× /generate - حتى تبدا بأستخراج البوت
× /cancel - لألغاء الاستخراج
× /restart - اعادة تشغيل البوت
"""

    # About Message
    ABOUT = """
**⚜️¦حـول البـوت** 

𝗦𝗲𝗯𝘂𝗮𝗵 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗯𝗼𝘁 𝘂𝗻𝘁𝘂𝗸 𝗺𝗲𝗻𝗴𝗮𝗺𝗯𝗶𝗹 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗱𝗮𝗻 𝘁𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗯𝘆 @RzydxStringbot

𝗚𝗿𝗼𝘂𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 : [ɢᴀʙᴜɴɢ](https://t.me/Rzydx_Support)

𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [Pyrogram](docs.pyrogram.org)

𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [Python](www.python.org)

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : [Rzydx](https://t.me/Ngapain_Ngetag)
    """
