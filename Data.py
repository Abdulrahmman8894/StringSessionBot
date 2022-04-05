from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝗛𝗮𝗹𝗼 {}
✠━━━━━━━━❖━━━━━━━━━✠
{} 𝗔𝗱𝗮𝗹𝗮𝗵 𝗕𝗼𝘁 𝗬𝗮𝗻𝗴 𝗗𝗶 𝗕𝘂𝗮𝘁 𝗨𝗻𝘁𝘂𝗸 𝗠𝗲𝗺𝗯𝗮𝗻𝘁𝘂 𝗔𝗻𝗱𝗮 𝗠𝗲𝗻𝗴𝗮𝗺𝗯𝗶𝗹 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗗𝗲𝗻𝗴𝗮𝗻 𝗠𝘂𝗱𝗮𝗵 𝗗𝗮𝗻 𝗔𝗠𝗔𝗡!
━━━━━━━━━━━━━━━━━━━
𝗞𝗮𝗹𝗼 𝗟𝘂 𝗚𝗮𝗸 𝗣𝗲𝗿𝗰𝗮𝘆𝗮 𝗕𝗼𝘁 𝗜𝗻𝗶:
1. 𝗚𝗮𝗸 𝗨𝘀𝗮𝗵 𝗕𝗮𝗰𝗮 𝗣𝗲𝘀𝗮𝗻 𝗜𝗻𝗶 𝗔𝗻𝗷
2. 𝗕𝗹𝗼𝗸𝗶𝗿 𝗕𝗼𝘁 𝗔𝘁𝗮𝘂 𝗗𝗲𝗹𝗲𝘁𝗲 𝗖𝗵𝗮𝘁 𝗬𝗮 𝗧𝗼𝗱
✠━━━━━━━━❖━━━━━━━━━✠
𝗠𝗮𝗻𝗮𝗴𝗲𝗱 𝗕𝘆 @Ngapain_Ngetag
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")],
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
