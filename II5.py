from .. import loader
import asyncio
from collections import deque


def register(cb):
    cb(ProjectsMod())

class ProjectsMod(loader.Module):
    strings = {'name': 'Smilesss'}

    async def mhrtcmd(self, message):
        m = ("👊🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👊🏿\n"
             "👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿\n"
             "👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👉🏽👉🏼👉🏻♥👈🏻👈🏼👈🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿\n"
             "👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿\n"
             "👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿\n"
             "👊🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👊🏿")
        hrt = "♥"
        for _ in range(10):
            for i in ["❤️", "🧡", "💛","💚", "💙", "💜", "🖤", "🤍", "🤎"]:
                m = m.replace(hrt, i)
                await message.edit(m)
                hrt = i
                await asyncio.sleep(0.5)
                
                
    async def boatcmd(self, message):
        deq = deque(list("🚣‍♀🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"))
        for _ in range(32):
            await asyncio.sleep(0.1)
            await message.edit("".join(deq))
            deq.rotate(1)