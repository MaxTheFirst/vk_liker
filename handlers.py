from dispatcher import dp, clients
from aiogram.types import Message
import textes


@dp.message_handler(commands=[textes.START_COMMAND], commands_prefix=textes.PREFIX)
async def on_start(message: Message):
    await message.answer(textes.HELLOW)


@dp.message_handler()
async def like(messange: Message):
    if 'https://vk.com/' in messange.text:
        domain = messange.text.split('/')[-1]
        data = await clients.add_likes(domain)
        if data[0] != 0:
            await messange.answer(textes.OK_TEXT.format(*data))
            return
    await messange.answer(textes.ERROR_TEXT)
