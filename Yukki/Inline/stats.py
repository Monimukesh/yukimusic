from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖲𝗂𝗌𝗍𝖾𝗆 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗉𝗈𝗅𝖺𝗆𝖺 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖡𝗈𝗍 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖦𝖾𝗇𝖾𝗅 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗉𝗈𝗅𝖺𝗆𝖺 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖡𝗈𝗍 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖲𝗂𝗌𝗍𝖾𝗆 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝖦𝖾𝗇𝖾𝗅 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖡𝗈𝗍 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖲𝗂𝗌𝗍𝖾𝗆 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗉𝗈𝗅𝖺𝗆𝖺 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖦𝖾𝗇𝖾𝗅 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖲𝗂𝗌𝗍𝖾𝗆 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗉𝗈𝗅𝖺𝗆𝖺 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖡𝗈𝗍 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝖦𝖾𝗇𝖾𝗅 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖲𝗂𝗌𝗍𝖾𝗆 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝖣𝖾𝗉𝗈𝗅𝖺𝗆𝖺 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖡𝗈𝗍 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝖦𝖾𝗇𝖾𝗅 𝗂𝗌𝗍𝖺𝗍𝗂𝗌𝗍𝗂𝗄", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝖠𝗌𝗂𝗌𝗍𝖺𝗇 𝗂𝗌𝗍𝖺𝗍𝗂𝗄𝗅𝖾𝗋𝗂𝗇𝗂 𝖠𝗅𝗆𝖺....",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
