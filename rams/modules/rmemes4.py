# RAM-UBOT

import asyncio
from time import sleep


from rams import CMD_HELP, GROUP_LINK, IG_ALIVE, REPO_NAME, owner
from rams.utils import edit_or_reply, ram_cmd
from rams import CMD_HANDLER as cmd


@ram_cmd(pattern="terkadang(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")

@ram_cmd(pattern="ny(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, "**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")

@ram_cmd(pattern="bulan$")
async def _(event):
    event = await edit_or_reply(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("🌖")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ram_cmd(pattern="heli(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ HALO ANAK YATIM, AKU DATANG :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tembak(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="bundir(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "`DIDUGA BUNDIR KARNA DI GHOSTING...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tawa(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n**Awkwokwokwok Ngentod..**", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="ular(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()


@ram_cmd(pattern="ya(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tank(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="babi(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="ajg(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()


@ram_cmd(pattern="tolol(?: |$)(.*)")
async def _(tolol):
    typew = await edit_or_reply(tolol, "`TOLOL...`")
    sleep(2)
    await typew.edit("`Pertama Kamu tolol....`")
    sleep(1)
    await typew.edit("`Kedua Kamu memang tolol...`")
    sleep(1)
    await typew.edit("`Ketiga Kamu benar benar tolol..`")
    sleep(1)
    await typew.edit("`Dan kamu di lahirkan Dalam keadaan tolol...`")
    sleep(1)
    await typew.edit("`Dasar kamu anak TOLOL...`")
    sleep(1)
    await typew.edit("`T`")
    await typew.edit("`TO`")
    await typew.edit("`TOL`")
    await typew.edit("`TOLO`")
    await typew.edit("`TOLOL`")
    await typew.edit("`TOLOL!!!!`")


@ram_cmd(pattern="fck(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, ".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\    fuck you anjinnnggg")

CMD_HELP.update({
    "memes7":
    f"`{cmd}bulan` ; `{cmd}hati`\
    \nUsage: liat aja.\
    \n\n`{cmd}heli` ; `{cmd}tank` ; `{cmd}tembak`\n`{cmd}bundir`\
    \nUsage: liat sendiri."
})

CMD_HELP.update({
    "memes8":
    f"`.y`\
    \nUsage: jempol\
    \n\n`{cmd}tawa` ; `{cmd}fck`\
    \nUsage: ketawa lari , fvck.\
    \n\n`{cmd}ular` ; `{cmd}babi` ; `{cmd}ajg`\
    \nUsage: liat sendiri."
})

CMD_HELP.update(
    {
    "islamic":
    f"**plugin: **Islamic.\
    \n\n  • **Syntax :** `{cmd}alq`\
    \nUsage: Memberikan Voice Al-Qur'an yang menyejukan hati.\
    \n\n  • **Syntax :** `{cmd}sholawat`\
    \nUsage: Memberikan Voice Sholawat Yang membuat Tenang.\
    "
    }
)
