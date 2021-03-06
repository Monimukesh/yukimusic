from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"π¦πππ» π―ππΊππ«πππ",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} π―ππΊππ«πππ",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Ι’Κα΄Κ α΄Κα΄ΚΚΙͺsα΄",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} α΄Κα΄ΚΚΙͺsα΄Ιͺ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Bollywood",
                callback_data=f"play_playlist {user_id}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"Hollywood",
                callback_data=f"play_playlist {user_id}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Party",
                callback_data=f"play_playlist {user_id}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"Lofi",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Sad",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"Weeb",
                callback_data=f"play_playlist {user_id}|{type}|Weeb",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Punjabi",
                callback_data=f"play_playlist {user_id}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"Others",
                callback_data=f"play_playlist {user_id}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="π οΈ Ι’α΄ΚΙͺ Ι’Ιͺα΄",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"β Weeb",
                callback_data=f"add_playlist {videoid}|{type}|Weeb",
            ),
            InlineKeyboardButton(
                text=f"β Sad",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β Party",
                callback_data=f"add_playlist {videoid}|{type}|Party",
            ),
            InlineKeyboardButton(
                text=f"β Lofi",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β Bollywood",
                callback_data=f"add_playlist {videoid}|{type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"β Hollywood",
                callback_data=f"add_playlist {videoid}|{type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"β Punjabi",
                callback_data=f"add_playlist {videoid}|{type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"β Others",
                callback_data=f"add_playlist {videoid}|{type}|Others",
            ),
        ],
        [
            InlineKeyboardButton(
                text="π οΈ Ι’α΄ΚΙͺ Ι’Ιͺα΄", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Weeb", callback_data=f"check_playlist {type}|Weeb"
            ),
            InlineKeyboardButton(
                text=f"Sad", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Party", callback_data=f"check_playlist {type}|Party"
            ),
            InlineKeyboardButton(
                text=f"Lofi", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Bollywood",
                callback_data=f"check_playlist {type}|Bollywood",
            ),
            InlineKeyboardButton(
                text=f"Hollywood",
                callback_data=f"check_playlist {type}|Hollywood",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Punjabi",
                callback_data=f"check_playlist {type}|Punjabi",
            ),
            InlineKeyboardButton(
                text=f"Others", callback_data=f"check_playlist {type}|Others"
            ),
        ],
        [InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Ι’Κα΄Κ α΄Κα΄ΚΚΙͺsα΄",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]} α΄Κα΄ΚΚΙͺsα΄Ιͺ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]} α΄Κα΄ΚΚΙͺsα΄Ιͺ",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="π―οΈ α΄α΄α΄α΄α΄", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="βΆοΈ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="βΈοΈ", callback_data=f"pausecb"),
            InlineKeyboardButton(text="β­οΈ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="βΉοΈ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Checkout Queued Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Checkout Playlist", url=f"{url}")],
        [InlineKeyboardButton(text="π―οΈ α΄α΄Ι΄α΄Κα΄ α΄α΄α΄α΄α΄", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Yes! Delete",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="No!", callback_data=f"close"),
        ],
    ]
    return buttons
