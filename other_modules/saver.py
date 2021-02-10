from .. import loader, utils
@loader.tds
class SavemeMod(loader.Module):
    """Save anything"""
    strings = {"name": "Saver"}
    @loader.unrestricted
    async def mcmd(self, message):
        """.m - save to me"""
        reply = await message.get_reply_message()
        if not reply:
            return
        await message.client.send_message("me", reply)
        await message.delete()