from pyrogram import Client, filters

from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]

    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]

    random.shuffle(members)

    app.send_message(chat, "Щелчок Таноса ... *щёлк*")

    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)

    app.send_message(chat, "Но какой ценой?")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply_text(f"Привет {message.from_user.mention}!\nПривет, вам пишет автоответчик. Владелец аккаунта сейчас не в сети или занят.\nЯ уже передал ваше сообщение, ожидайте! Полезные ссылки для вас\nhttps://telegra.ph/Pravila-igry-09-08-4\nhttps://telegra.ph/FAQ-po-igre-v-Mafiyu-09-23\nhttps://telegra.ph/Kak-stat-adminom-v-Mafia-Bonds-09-27\n")

app.run()