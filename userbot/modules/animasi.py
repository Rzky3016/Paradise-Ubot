from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.rizky(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Rizky`")
    sleep(3)
    await typew.edit("`16 Tahun`")
    sleep(1)
    await typew.edit("`Owner Dari Paradise Userbot, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^ilyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu, Kamu Sangat Berharga Dan Berarti Di Hidupku`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@register(outgoing=True. pattern='^.ganteng(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Lu Mau Tau Semua Fakta?`")
    sleep(3)
    await typew.edit("`Fakta Yang Belum Terbongkar Selama Ini`")
    sleep(3)
    await typew.edit("`GUA GANTENG FIX NO DEBATπ`")


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.wibu(?: |$)(.*)')
async def typewriter(type):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Kata Emak`")
    sleep(2)
    await typew.edit("`Kalo Ketemu Wibuu`")
    sleep(2)
    await typew.edit("`Harus Lari Sekenceng Mungkinππ»`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€γ€γ€γ€γ€γ€ππ»`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€γ€γ€γ€γ€ππ»π¨`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€γ€γ€γ€ππ»π¨γ€`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€γ€γ€ππ»π¨γ€γ€`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€γ€ππ»π¨γ€γ€γ€`")
    sleep(1)
    await typew.edit("`γ€γ€γ€γ€ππ»π¨γ€γ€γ€γ€`")
    sleep(1)
    await typew.edit("`γ€γ€γ€ππ»π¨γ€γ€γ€γ€γ€`")
    sleep(1)
    await typew.edit("`γ€γ€ππ»π¨γ€γ€γ€γ€γ€γ€`")
    sleep(1)
    await typew.edit("`γ€ππ»π¨γ€γ€γ€γ€γ€γ€γ€`")
    sleep(1)
    await typew.edit("`ππ»π¨γ€γ€γ€γ€γ€γ€γ€γ€`")


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Udang`")
    sleep(2)
    await typew.edit("`Cuma Sendiri nih Senggol Dong`")


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Awali perkataan dengan dengan salam`")
    sleep(1)
    await typew.edit("`Assalamualaikum Sayang`")


CMD_HELP.update({
    "animasi3":
    "πΏCMDπΏ`.pe`\
\nPenjelasan: Cek lah asw.\
\n\nπΏCMDπΏ`.feri`\
\nPenjelasan: Cek lah asw.\
\n\nπΏCMDπΏ`.ilyu`\
\nPenjelasan: Cek lah asw.\
\n\nπΏCMDπΏ`p`\
\nPenjelasan: Cek lah asw.\
\n\nπΏCMDπΏ`.semangat`\
\nPenjelasan: Cek lah asw.\
\n\nπΏCMDπΏ`.wibu`\
\nPenjelasan: Lari Dari Wibu.\
\n\nπΏCMDπΏ`.ganteng`\
\nPenjelasan: Gua Ganteng."
})
