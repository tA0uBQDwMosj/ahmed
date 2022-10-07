from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="↯︙اضفني على مجموعتك .",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="↯︙↯︙الاعدادات .",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="↯︙الاوامر .", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↯︙المالك .", user_id=OWNER),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="↯︙اضفني على مجموعتك .",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="↯︙الاعدادات .", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="↯︙المالك .", user_id=OWNER),           
        ],
     ]
    return buttons
