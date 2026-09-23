from time import time

from ..helper.ext_utils.bot_utils import new_task
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.message_utils import send_message, edit_message, send_file
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.bot_commands import BotCommands


@new_task
async def start(_, message):
    buttons = ButtonMaker()
    buttons.url_button(
        "𝕎𝕚𝕜𝕚", "https://t.me/TheOnlyMrLucifer"
    )
    buttons.url_button(
        "𝔸𝕗𝕥𝕖𝕣 𝔻𝕒𝕣𝕜 𝕊𝕠𝕔𝕚𝕖𝕥𝕪", "https://theonlymrlucifer.nl/"
    )
    reply_markup = buttons.build_menu(2)
    if await CustomFilters.authorized(_, message):
        start_string = f"""
Welcome Too ℂ𝕠𝕟𝕥𝕖𝕟𝕥 𝔹𝕠𝕥 This Bot Is Owned By: ⛥ 𝓦𝓲𝓴𝓲 ⛥ .
Type /{BotCommands.HelpCommand} to get a list of available commands
"""
        await send_message(message, start_string, reply_markup)
    else:
        await send_message(
            message,
            "Welcome Too ℂ𝕠𝕟𝕥𝕖𝕟𝕥 𝔹𝕠𝕥 This Bot Is Owned By: ⛥ 𝓦𝓲𝓴𝓲 ⛥.\n\n⚠️ You Are Not Authorized ! For Authorization ⛥ 𝓦𝓲𝓴𝓲 ⛥ ⚠️",
            reply_markup,
        )


@new_task
async def ping(_, message):
    start_time = int(round(time() * 1000))
    reply = await send_message(message, "Starting Ping")
    end_time = int(round(time() * 1000))
    await edit_message(reply, f"{end_time - start_time} ms")


@new_task
async def log(_, message):
    await send_file(message, "log.txt")
