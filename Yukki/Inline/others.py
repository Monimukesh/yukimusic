from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 𝖲𝖺𝗋𝗄𝗂 𝖲𝗈𝗓𝗅𝖾𝗋𝗂",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ 𝖲𝗂𝗓𝗂𝗇 𝖯𝗅𝖺𝗒𝖫𝗂𝗌𝗍 ",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ 𝖦𝗋𝗎𝖻 𝖯𝗅𝖺𝗒𝖫𝗂𝗌𝗍",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 𝖲𝖾𝗌/𝖵𝗂𝖽𝖾𝗈 𝗂𝗇𝖽𝗂𝗋",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="🛠️ 𝖦𝖾𝗋𝗂 𝖦𝗂𝗍",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗯️ 𝖬𝖾𝗇𝗎 𝖪𝖺𝗉𝖺𝗍",
                callback_data=f"close",
            ),
        ],
    ]
    return buttons


def download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📥 𝖲𝖾𝗌 𝖠𝗅 ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📥 𝖵𝗂𝖽𝖾𝗈 𝖠𝗅 ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🛠️ 𝖦𝖾𝗋𝗂 𝖦𝗂𝗍 ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗯️ 𝖬𝖾𝗇𝗎𝗒𝗎 𝖪𝖺𝗉𝖺𝗍 ", callback_data=f"close"),
        ],
    ]
    return buttons
