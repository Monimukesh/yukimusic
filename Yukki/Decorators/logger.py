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
                what = "𝖮𝗓𝖾𝗅 𝖦𝗋𝗎𝖻"
            except:
                try:
                    if not message.reply_to_message:
                        what = "𝖸𝖺𝗅𝗇𝗂𝗓𝖼𝖺 𝖵𝖾𝗋𝗂𝗅𝖾𝗇 𝖪𝗈𝗆𝗎𝗍"
                    else:
                        what = "Herhangi bir dosyaya yanıt verdi."
                except:
                    what = "𝖪𝗈𝗆𝗎𝗍"
            logger_text = f"""
**𝖸𝖾𝗇𝗂 {what}**

**𝖦𝗋𝗎𝖻:** {message.chat.title} [`{message.chat.id}`]
**𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂:** {message.from_user.mention}
**𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂 𝖠𝖽𝗂:** @{message.from_user.username}
**𝖪𝗎𝗅𝗅𝖺𝗇𝗂𝖼𝗂 ID:** `{message.from_user.id}`
**𝖦𝗋𝗎𝖻 Link:** {chatusername}
**𝖲𝗈𝗋𝗀𝗎:** {message.text}"""
            if LOG_CLIENT != "None":
                await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
        return await mystic(_, message)

    return wrapper
