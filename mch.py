from .. import loader, utils
import requests

def register(cb):
    cb(MailSearcherMod())

class MailSearcherMod(loader.Module):
    "AntiPublic MYRZ"
    strings = {"name": "AntiPublic MYRZ"}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self.db = db
    async def myrz_keycmd(self, m):
        self.db.set("myrz", "key", str(m.raw_text.split(" ", 1)[1]))
        await m.edit("[AntiPublic MYRZ] Токен установлен")
    async def msrchcmd(self, m):
        "Получить пароли почты/логина"
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        }
        key = self.db.get("myrz", "key", None)
        if not key:
            await m.edit("<b>Укажите ключ из антипаблика myrz!</b>\n\n<code>.myrz_key [KEY]</code>")
            return
        args = utils.get_args_raw(m)
        if args:
            await m.edit("Делаю запрос...")
            data = requests.post("http://myrz.org/api/email_search.php", data={"key":key, "email":args}, headers=headers).json()
            try:
                if data['success'] == True:
                    psswds = "\n".join([f"<code>{i['line']}</code>" for i in data['results']])
                    psswds += f"\n\nОсталось запросов: {data['awailableQueries']}\nНайдено: {data['resultCount']}\nЗапрос: <code>{args}</code>"
                    await utils.answer(m, str(psswds))
                else:
                    await m.edit(f"Ничего не найдено по запросу <code>{args}</code>\nОсталось запросов: {data['awailableQueries']}")
            except:
                await m.edit(str(data))
        else:
            await m.edit("shit...")
            
      
