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
                text="𝖧𝖾𝗆𝖾𝗇 𝗂𝗇𝖽𝗂𝗋",
                callback_data=f"qwertyuiopasdfghjkl {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"song_right F|{query_type}|{query}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗯️ 𝖠𝗋𝖺𝗆𝖺𝗒𝗂 𝖪𝖺𝗉𝖺𝗍",
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


def song_download_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📥 𝖲𝖾𝗌 𝖺𝗅",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📥 𝖵𝗂𝖽𝖾𝗈 𝖺𝗅",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗯️ 𝖬𝖾𝗇𝗎𝗒𝗎 𝖪𝖺𝗉𝖺𝗍",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
