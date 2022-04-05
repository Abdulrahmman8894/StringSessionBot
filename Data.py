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
        [InlineKeyboardButton("🔥 ⚜️¦ ابدأ استخراح الكود 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ]
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

× /about - 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗕𝗼𝘁 𝗶𝗻𝗶
× /help - 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲
× /start - 𝗠𝘂𝗹𝗮𝗶 𝗕𝗼𝘁
× /generate - 𝗠𝘂𝗹𝗮𝗶 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝘁𝗿𝗶𝗻𝗴
× /cancel - 𝗠𝗲𝗺𝗯𝗮𝘁𝗮𝗹𝗸𝗮𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀
× /restart - 𝗠𝗲𝗺𝗯𝗮𝘁𝗮𝗹𝗸𝗮𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀
"""

    # About Message
    ABOUT = """
**About This Bot** 

𝗦𝗲𝗯𝘂𝗮𝗵 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗯𝗼𝘁 𝘂𝗻𝘁𝘂𝗸 𝗺𝗲𝗻𝗴𝗮𝗺𝗯𝗶𝗹 𝗽𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗱𝗮𝗻 𝘁𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝘀𝘁𝗿𝗶𝗻𝗴 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗯𝘆 @RzydxStringbot

𝗚𝗿𝗼𝘂𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 : [ɢᴀʙᴜɴɢ](https://t.me/Rzydx_Support)

𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [Pyrogram](docs.pyrogram.org)

𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : [Python](www.python.org)

𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 : [Rzydx](https://t.me/Ngapain_Ngetag)
    """
