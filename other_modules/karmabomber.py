from .. import loader, utils


@loader.tds
class KarmaBomber(loader.Module):
    strings = {"name": "Карма-бомбер"}
    @loader.owner
    async def pluscmd(self, message):
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not reply:
            await message.edit("Кого плюсить?")
            return
        await message.edit(reply)
        if args is None:
            pass
        else:
            pass
