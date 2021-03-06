from config import LOG_GROUP_ID
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Database import is_on_off


def logging(mystic):
    async def wrapper(_, message):
        if await is_on_off(5):
            if message.chat.username:
                chatusername = f"@{message.chat.username}"
            else:
                chatusername = ""
            try:
                query = message.text.split(None, 1)[1]
                what = "๐ฎ๐๐พ๐ ๐ฆ๐๐๐ป"
            except:
                try:
                    if not message.reply_to_message:
                        what = "๐ธ๐บ๐๐๐๐๐ผ๐บ ๐ต๐พ๐๐๐๐พ๐ ๐ช๐๐๐๐"
                    else:
                        what = "Herhangi bir dosyaya yanฤฑt verdi."
                except:
                    what = "๐ช๐๐๐๐"
            logger_text = f"""
**๐ธ๐พ๐๐ {what}**

**๐ฆ๐๐๐ป:** {message.chat.title} [`{message.chat.id}`]
**๐ช๐๐๐๐บ๐๐๐ผ๐:** {message.from_user.mention}
**๐ช๐๐๐๐บ๐๐๐ผ๐ ๐ ๐ฝ๐:** @{message.from_user.username}
**๐ช๐๐๐๐บ๐๐๐ผ๐ ID:** `{message.from_user.id}`
**๐ฆ๐๐๐ป Link:** {chatusername}
**๐ฒ๐๐๐๐:** {message.text}"""
            if LOG_CLIENT != "None":
                await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
        return await mystic(_, message)

    return wrapper
