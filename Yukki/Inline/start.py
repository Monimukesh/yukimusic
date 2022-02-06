from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Seviyesi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Yetkili Kullanıcılar", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Gösterge Paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ 𝖪𝖺𝗉𝖺𝗍", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋  𝖣𝖾𝗌𝗍𝖾𝗄 𝖦𝗋𝗎𝖻𝗎  📋", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝  𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅𝗂  📝", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝  𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅𝗂  📝", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📋  𝖣𝖾𝗌𝗍𝖾𝗄 𝖦𝗋𝗎𝖻𝗎  📋", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "🎉  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  🎉",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "🎉  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  🎉",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📋  𝖣𝖾𝗌𝗍𝖾𝗄 𝖦𝗋𝗎𝖻𝗎  📋", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "🎉  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  🎉",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝  𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅𝗂  📝", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📚  𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋  📚", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "🎉  𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾  🎉",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📝  𝖡𝗂𝗅𝗀𝗂 𝖪𝖺𝗇𝖺𝗅𝗂  📝", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📋  𝖣𝖾𝗌𝗍𝖾𝗄 𝖦𝗋𝗎𝖻𝗎  📋", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Ses kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Ses Seviyesi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Gösterge Paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Kapat", callback_data="close"),
            InlineKeyboardButton(text="🔙 Geri Git", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Ses Seviyesini Sıfırla 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Düşük Hacim", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Orta Hacim", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Yüksek Hacim", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Güçlendirilmiş Cilt", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Özel Hacim 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri gitmek", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 Özel Hacim 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Herkes", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Yöneticiler", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Yetkili Kullanıcı Listeleri", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Geri Git", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ çalışma süresi", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Geri git", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Settings**", buttons
