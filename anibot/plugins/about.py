import os
import re
from telethon import events, Button
from anibot import telethn as tbot


@anibot.on_message(~filters.private & filters.command(['about', f'about{BOT_NAME}']))
@control_user
async def awake(event):
  TEXT = f"**Hi, I'm Sagiri Ani-Bot.** \n\n"
  TEXT += "⚪ **I'm Working Properly** \n\n"
  TEXT += f"⚪ **My Master : [Ako](https://t.me/erosei_1)** \n\n"
  TEXT += f"**I can help you get info on Animes, Mangas, Characters, Airings, Schedules, Watch Orders of Animes, etc.** \n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Update", "https://t.me/projectsupdates"), Button.url("Support", "https://t.me/AkoUpdate")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
