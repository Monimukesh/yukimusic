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
                text="🔎 sᴀʀᴋɪ sᴏᴢʟᴇʀɪ",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ sɪᴢɪɴ ᴘʟᴀʏʟɪsᴛɪɴɪᴢ ",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="✚ ɢʀᴜʙ ᴘʟᴀʏʟɪsᴛ",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📩 sᴇs/ᴠɪᴅᴇᴏ ɪɴᴅɪʀ",
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
                text="📥 sᴇs ᴀʟ ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ ᴀʟ ",
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
