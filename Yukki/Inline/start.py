from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="π Ses kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="π Ses Seviyesi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Yetkili KullanΔ±cΔ±lar", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» GΓΆsterge Paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ πͺπΊππΊπ", callback_data="close"),
        ],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  α΄α΄sα΄α΄α΄ Ι’Κα΄Κα΄  π", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  ΚΙͺΚΙ’Ιͺ α΄α΄Ι΄α΄ΚΙͺ  π", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π§ Settings", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  ΚΙͺΚΙ’Ιͺ α΄α΄Ι΄α΄ΚΙͺ  π", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="π  α΄α΄sα΄α΄α΄ Ι’Κα΄Κα΄  π", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "π  π‘πΎππ π¦πππ»πΊ π€πππΎ  π",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "π  π‘πΎππ π¦πππ»πΊ π€πππΎ  π",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  α΄α΄sα΄α΄α΄ Ι’Κα΄Κα΄  π", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "π  π‘πΎππ π¦πππ»πΊ π€πππΎ  π",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  ΚΙͺΚΙ’Ιͺ α΄α΄Ι΄α΄ΚΙͺ  π", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="π  α΄α΄α΄α΄α΄Κα΄Κ  π", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "π  π‘πΎππ π¦πππ»πΊ π€πππΎ  π",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="π  ΚΙͺΚΙ’Ιͺ α΄α΄Ι΄α΄ΚΙͺ  π", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="π  α΄α΄sα΄α΄α΄ Ι’Κα΄Κα΄  π", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"π  **This is {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="π Ses kalitesi", callback_data="AQ"),
            InlineKeyboardButton(text="π Ses Seviyesi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="π₯ Authorized Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="π» GΓΆsterge Paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="βοΈ Kapat", callback_data="close"),
            InlineKeyboardButton(text="π Geri Git", callback_data="okaybhai"),
        ],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="π Ses Seviyesini SΔ±fΔ±rla π", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="π DΓΌΕΓΌk Hacim", callback_data="LV"),
            InlineKeyboardButton(text="π Orta Hacim", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="π YΓΌksek Hacim", callback_data="HV"),
            InlineKeyboardButton(text="π GΓΌΓ§lendirilmiΕ Cilt", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="π½ Γzel Hacim π½", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="π Geri gitmek", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


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
        [InlineKeyboardButton(text="πΌ Γzel Hacim πΌ", callback_data="AV")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="π₯ Herkes", callback_data="EVE"),
            InlineKeyboardButton(text="π YΓΆneticiler", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="π Yetkili KullanΔ±cΔ± Listeleri", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="π Geri Git", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="βοΈ Γ§alΔ±Εma sΓΌresi", callback_data="UPT"),
            InlineKeyboardButton(text="πΎ Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="π» Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="π½ Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="π Geri git", callback_data="settingm")],
    ]
    return f"π§  **{MUSIC_BOT_NAME} Settings**", buttons
