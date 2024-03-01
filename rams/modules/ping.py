# Ping From <\ram-ubot/>
# From @lahsiajg <starboy/>

""" rams module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

from speedtest import Speedtest

from rams import CMD_HANDLER as cmd, DEVS
from rams.utils import edit_or_reply, ram_cmd
from rams import CMD_HELP, BOT_VER, DEVG, REPO_NAME, StartTime, branch
from rams.events import register

gesss = [
    "Eh ada Owner keren",
    "Hadir ganteng 😍",
    "Hi Tuan, kemana sj? 🤗",
    "Hadir kak 😉",
    "Hadir bang 😁",
    "Hadir bang maap telat 🥺",
    "Saya slalu ada buat Tuan Owner🥵",
    "Jangan kemana mana lagi ya bang",
    "Pas banget bang, aku lagi kangen",
    "Bang owner on juga akhirnya🥵",
]

brb = [
    "Bang owner mau off.",
    "Jangan off dong bang.",
    "Bang, mau kemana?",
    "Jangan lama lama bang",
    "Siap bang.",
    "Yah udah off aja bang.",
    "Off lagi, mau ngewe ya?",
    "Bang developer, lagi ange kah? ",
    "Jangan lupa makan bang.",
    "Yah pasti mao bucin ni.",
    "Jangan off terus lah bang.",
    "Mau nonton bokep kah?",
    "Bang Ganteng telah off.",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 50
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@ram_cmd(pattern="ping$")
async def _(ping):
    """ For.ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.reply(
            f"**❏ ᴢᴀʀ ᴘɪɴɢᴇʀ**\n"
            f"`%sms`" % (duration)
    )

@ram_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**8✊===D**")
    await ram.edit("8=✊==D")
    await ram.edit("8==✊=D")
    await ram.edit("8===✊D")
    await ram.edit("8==✊=D")
    await ram.edit("8=✊==D")
    await ram.edit("8✊===D")
    await ram.edit("8=✊==D")
    await ram.edit("8==✊=D")
    await ram.edit("8===✊D")
    await ram.edit("8==✊=D")
    await ram.edit("8=✊==D")
    await ram.edit("8✊===D")
    await ram.edit("8=✊==D")
    await ram.edit("8==✊=D")
    await ram.edit("8===✊D")
    await ram.edit("8===✊D💦")
    await ram.edit("8=====D💦💦")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await pong.reply(
            f"**♡ CROOTTTT PINGGGG!**\n"
            f"`%sms`" % (duration)
    )

@ram_cmd(pattern="pink$")
async def redis(pingx):
    """For .ping command, ping the rams from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pingx, "**𓀐.....................................𓂸**")
    await ram.edit("**𓀐..................................𓂸..**")
    await ram.edit("**𓀐................................𓂸....**")
    await ram.edit("**𓀐..............................𓂸......**")
    await ram.edit("**𓀐............................𓂸........**")
    await ram.edit("**𓀐..........................𓂸..........**")
    await ram.edit("**𓀐.......................𓂸.............**")
    await ram.edit("**𓀐.....................𓂸...............**")
    await ram.edit("**𓀐...................𓂸.................**")
    await ram.edit("**𓀐..................𓂸..................**")
    await ram.edit("**𓀐................𓂸....................**")
    await ram.edit("**𓀐..............𓂸......................**")
    await ram.edit("**𓀐............𓂸........................**")
    await ram.edit("**𓀐..........𓂸..........................**")
    await ram.edit("**𓀐........𓂸............................**")
    await ram.edit("**𓀐.......𓂸.............................**")
    await ram.edit("**𓀐....𓂸...............................**")
    await ram.edit("**𓀐..𓂸.................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓀐𓂸...................................**")
    await ram.edit("**𓀐.𓂸..................................**")
    await ram.edit("**𓂺**")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pingx.client.get_me()
    await pingx.reply(
            f"**⛥ ᴢᴀʀ ᴘɪɴɢᴇʀ**\n"
            f"`%sms`\n"
            f"**⛥ ᴜᴘᴛɪᴍᴇ**"
            f"`{uptime}`" % (duration)
    )

def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"




CMD_HELP.update({
    "ping": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ping` or `{cmd}rping` or `{cmd}pink`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}pong`\
         \n↳ : Sama Seperti Perintah {cmd}pink."})
