from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def song_markup(videoid, duration, user_id, query, query_type):
    buttons = [
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"song_right B|{query_type}|{query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ʜᴇᴍᴇɴ ɪɴᴅɪʀ 𝗂𝗇𝖽𝗂𝗋",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗯️ ᴀʀᴀᴍᴀʏɪ ᴋᴀᴘᴀᴛ",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📥 sᴇs ᴀʟ",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ ᴀʟ",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗯️ ᴍᴇɴᴜʏᴜ ᴋᴀᴘᴀᴛ",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
