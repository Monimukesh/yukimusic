from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        if message.chat.type == "private":
            return await mystic(_, message)
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "𝖡𝖺𝗓𝗂 𝗂𝗓𝗂𝗇𝗅𝖾𝗋𝗅𝖾 𝗒𝗈𝗇𝖾𝗍𝗂𝖼𝗂 𝗈𝗅𝗆𝖺𝗆 𝗀𝖾𝗋𝖾𝗄𝗂𝗒𝗈𝗋:\n"
                + "\n- **can_manage_voice_chats:** 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝗂 𝖸𝗈𝗇𝖾𝗍𝗆𝖾𝗄"
                + "\n- **can_delete_messages:** 𝖠𝗋𝖺𝗇𝖺𝗇 𝖠𝗍𝗂𝗄𝗅𝖺𝗋𝗂 𝖳𝖾𝗆𝗂𝗓𝗅𝖾𝗆𝖾𝗄"
                + "\n- **can_invite_users**: 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖣𝖺𝗏𝖾𝗍 𝖾𝗍𝗆𝖾𝗄"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "𝖡𝗎 𝖤𝗒𝗅𝖾𝗆𝗂 𝖦𝖾𝗋𝖼𝖾𝗄𝗅𝖾𝗌𝗍𝗂𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 𝖦𝖾𝗋𝖾𝗄𝗅𝗂 𝗂𝗓𝗇𝖾 𝖲𝖺𝗁𝗂𝗉 𝖣𝖾𝗀𝗂𝗅𝗂𝗆."
                + "\n**𝗂𝗓𝗂𝗇:** 𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝗂 𝖸𝗈𝗇𝖾𝗍𝗆𝖾"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "𝖡𝗎 𝖤𝗒𝗅𝖾𝗆𝗂 𝖦𝖾𝗋𝖼𝖾𝗄𝗅𝖾𝗌𝗍𝗂𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 𝖦𝖾𝗋𝖾𝗄𝗅𝗂 𝗂𝗓𝗇𝖾 𝖲𝖺𝗁𝗂𝗉 𝖣𝖾𝗀𝗂𝗅𝗂𝗆."
                + "\n**𝗂𝗓𝗂𝗇:** 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖲𝗂𝗅𝗆𝖾 "
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "𝖡𝗎 𝖤𝗒𝗅𝖾𝗆𝗂 𝖦𝖾𝗋𝖼𝖾𝗄𝗅𝖾𝗌𝗍𝗂𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 𝖦𝖾𝗋𝖾𝗄𝗅𝗂 𝗂𝗓𝗇𝖾 𝖲𝖺𝗁𝗂𝗉 𝖣𝖾𝗀𝗂𝗅𝗂𝗆."
                + "\n**𝗂𝗓𝗂𝗇:** 𝖡𝖺𝗀𝗅𝖺𝗇𝗍𝗂 𝖽𝖺𝗏𝖾𝗍 𝖾𝗍𝗆𝖾"
            )
            return
        return await mystic(_, message)

    return wrapper
