import os
import re

import lyricsgenius
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from Yukki import MUSIC_BOT_NAME, app

__MODULE__ = "𝖲𝖺𝗋𝗄𝗂 𝖲𝗈𝗓𝗎"
__HELP__ = """

/Lyrics [ 𝖬𝗎𝗓𝗂𝗄 𝖺𝖽𝗂 ]
- Web'de belirli bir Müzik için Şarkı Sözleri arar.

"""


@app.on_callback_query(filters.regex(pattern=r"lyrics"))
async def lyricssex(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    try:
        id, user_id = callback_request.split("|")
    except Exception as e:
        return await CallbackQuery.message.edit(
            f"Error Occured\n**Possible reason could be**:{e}"
        )
    url = f"https://www.youtube.com/watch?v={id}"
    print(url)
    try:
        results = VideosSearch(url, limit=1)
        for result in results.result()["result"]:
            title = result["title"]
    except Exception as e:
        return await CallbackQuery.answer(
            "Ses bulunamadı. Youtube sorunları.", show_alert=True
        )
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    t = re.sub(r"[^\w]", " ", title)
    y.verbose = False
    S = y.search_song(t, get_full_info=False)
    if S is None:
        return await CallbackQuery.answer(
            "şarkı bulunamadı :p", show_alert=True
        )
    await CallbackQuery.message.delete()
    userid = CallbackQuery.from_user.id
    usr = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    xxx = f"""
**Lyrics Search Powered By {MUSIC_BOT_NAME}**

**Arayan:-** {usr}
**Aranan Şarkı:-** __{title}__

**Bulunan Şarkı Sözleri:-** __{S.title}__
**Sanatçı:-** {S.artist}

**Şarkı sözleri:**

{S.lyrics}"""
    if len(xxx) > 4096:
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await CallbackQuery.message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await CallbackQuery.message.reply_text(xxx)


@app.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n/lyrics [ Music Name]")
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found :p")
    xxx = f"""
**Şarkı Sözü Arama {MUSIC_BOT_NAME}**

**Aranan Şarkı:-** __{query}__
**Bulunan Şarkı Sözleri:-** __{S.title}__
**Sanatçı:-** {S.artist}

**Şarkı sözleri:**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)
