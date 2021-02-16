from .. import loader, utils
import re
from asyncio import sleep


@loader.tds
class KarmaBomberMod(loader.Module):
    """Плюсует/минусует юзера на которого реплай. Количество плюсов/минусов: 2048\nЕсли указать в аргументы целое число - плюсует/минусует n-раз подряд"""
    strings = {'name': 'KarmaBomber',
               'usage': 'Бомбит плюсами/минусами человека в чате где есть карма-бот'}

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def pluscmd(self, message):
        """Плюсует юзера на которого реплай\nИспользование: .plus <n>; ничего"""
        args = utils.get_args_raw(message)
        a = re.compile(r"^\d+$")
        reply = await message.get_reply_message()
        symbol = '+'
        if not reply: return await message.edit("А кого плюсовать то?")
        await message.edit("+")
        if not a.match(args):
            args = 1
        for i in range(int(args)):
            m = await message.client.send_message(message.to_id, symbol*2048, reply_to=reply)
            await sleep(0.2)
            await message.client.delete_messages(message.chat.id, m.id)
            await sleep(1)

    async def minuscmd(self, message):
        """Минусует юзера на которого реплай\nИспользование: .minus <n>; ничего"""
        args = utils.get_args_raw(message)
        a = re.compile(r"^\d+$")
        reply = await message.get_reply_message()
        symbol = '-'
        if not reply: return await message.edit("А кого минусовать то?")
        await message.edit("-")
        if not a.match(args):
            args = 1
        for i in range(int(args)):
            m = await message.client.send_message(message.to_id, symbol*2048, reply_to=reply)
            await sleep(0.2)
            await message.client.delete_messages(message.chat.id, m.id)
            await sleep(1)
