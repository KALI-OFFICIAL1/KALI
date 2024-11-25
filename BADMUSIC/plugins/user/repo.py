import asyncio

from BADMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command(["repo"], prefixes=["."]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://envs.sh/zeZ.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention} [☆ ʀᴇᴘᴏ 💗](https://github.com/Badhacker98/BADMUSIC/fork)",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ 💗 ", url=f"https://t.me/alone_somu6"
            ),
            InlineKeyboardButton(
                text="☆ ɢʀᴏᴜᴘ 💗", url=f"https://t.me/somueditingzone"
            ),
        ],
          [
            InlineKeyboardButton(
                text="☆ ᴄʜᴀɴɴᴇʟ 💗 ", url=f"https://t.me/somueditingzone"
            ),
            InlineKeyboardButton(
                text="☆ ʀᴇᴘᴏ 💗", url=f"https://envs.sh/Kqv.jpg"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
  
