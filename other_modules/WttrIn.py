from .. import loader, utils
import requests
def register(cb):
    cb(WttrInMod())
class WttrInMod(loader.Module):
    """WttrIn"""
    strings = {'name': 'WttrIn'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def wthrcmd(self, m):
        """.wthr <Город если надо>
        Получить текущую погоду
        """
        rr = utils.get_args_raw(m)
        await m.edit("<code>{}</code>".format(requests.get(f"https://wttr.in/{rr if rr != None else ''}?0Tq&lang=ru").text))