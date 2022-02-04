import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

from Yukki import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Inline import song_download_markup, song_markup
from Yukki.Utilities.url import get_url
from Yukki.Utilities.youtube import get_yt_info_query, get_yt_info_query_slider

loop = asyncio.get_event_loop()

__MODULE__ = "𝖡𝗎𝗅"
__HELP__ = """


/Bul [𝖬𝗎𝗓𝗂𝗄 𝖺𝖽𝗂]
- Belirli bir sorguyu ses veya video formatında indirin.



"""


@app.on_message(
    filters.command(["bul", "song", f"bul@{BOT_USERNAME}"])
)
@PermissionCheck
async def play(_, message: Message):
    if message.chat.type == "private":
        pass
    else:
        if message.sender_chat:
            return await message.reply_text(
                "Bu Sohbet Grubunda __Anonim Yönetici__siniz!\nYönetici Haklarından Kullanıcı Hesabına geri dönün."
            )
    try:
        await message.delete()
    except:
        pass
    url = get_url(message)
    if url:
        mystic = await message.reply_text("🔄 𝖴𝖱𝖫 𝗒𝗎𝗄𝗅𝖾𝗇𝗂𝗒𝗈𝗋, 𝖫𝗎𝗍𝖿𝖾𝗇 𝖡𝖾𝗄𝗅𝖾𝗒𝗂𝗇 !")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(None, get_yt_info_query, query)
        if str(duration_min) == "None":
            return await mystic.edit("Sorry! Its a Live Video")
        await mystic.delete()
        buttons = song_download_markup(videoid, message.from_user.id)
        return await message.reply_photo(
            photo=thumb,
            caption=f"📋𝖡𝖺𝗌𝗅𝗂𝗄: **{title}\n\n⌚𝖲𝗎𝗋𝖾:** {duration_min} 𝖣𝖺𝗄𝗂𝗄𝖺\n\n[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            await message.reply_text(
                "**𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝗆:**\n\n/bul [ 𝖬𝗎𝗓𝗂𝗄 𝖺𝖽𝗂 ]\n\n 𝖬𝗎𝗓𝗂𝗄 𝗂𝗇𝖽𝗂𝗋𝗂𝗋."
            )
            return
        mystic = await message.reply_text("🔍")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(None, get_yt_info_query, query)
        if str(duration_min) == "None":
            return await mystic.edit("Üzgünüm! Bu bir Canlı Video")
        await mystic.delete()
        buttons = song_markup(
            videoid, duration_min, message.from_user.id, query, 0
        )
        return await message.reply_photo(
            photo=thumb,
            caption=f"📋 𝖡𝖺𝗌𝗅𝗂𝗄: **{title}\n\n⌚ 𝖲𝗎𝗋𝖾:** {duration_min} 𝖣𝖺𝗄𝗂𝗄𝖺\n\n__[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(filters.regex("qwertyuiopasdfghjkl"))
async def qwertyuiopasdfghjkl(_, CallbackQuery):
    print("234")
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid, user_id)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"song_right"))
async def song_right(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, type, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Kendi Müziğinizi Arayın. Bu düğmeyi kullanmanıza izin verilmiyor.",
            show_alert=True,
        )
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        await CallbackQuery.answer("𝖣aha fazla sonuç", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📋 𝖡𝖺𝗌𝗅𝗂𝗄: **{title}\n\n⌚ 𝖲𝗎𝗋𝖾:** {duration_min} 𝖣𝖺𝗄𝗂𝗄𝖺\n\n__[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("Getting Previous Result", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = await loop.run_in_executor(
            None, get_yt_info_query_slider, query, query_type
        )
        buttons = song_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📋 𝖡𝖺𝗌𝗅𝗂𝗄: **{title}\n\n⌚ 𝖲𝗎𝗋𝖾:** {duration_min} 𝖣𝖺𝗄𝗂𝗄𝖺\n\n__[Video Hakkında Ek Bilgi Alın](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
