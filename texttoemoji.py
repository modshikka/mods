from .. import loader, utils
import logging

logger = logging.getLogger(__name__)


@loader.tds
class TextToEmojiMod(loader.Module):
    '''Text to Emoji'''


    strings = {"name": "TextToEmojiMod", "notext": "Please reply to text or pass arguments"}

    strings_ru = {"notext": "Пожалуйста ответьте на текст или впишите аргументом"}

    emojis = {
        "а": 5456128055414103034,
        "б": 5456434780503548020,
        "в": 5456256891548081456,
        "г": 5454330491341643548,
        "д": 5456670806136332319,
        "е": 5456638048420767252,
        "ё": 5456546939279514692,
        "ж": 5454311039434759616,
        "з": 5456509650373451167,
        "и": 5456623527136336113,
        "й": 5456505132067855523,
        "к": 5456371910772269309,
        "л": 5456140738452528837,
        "м": 5453930556871941888,
        "н": 5453937347215238994,
        "о": 5456502344634079449,
        "п": 5456402237536346480,
        "р": 5456119517019119748,
        "с": 5456490688092838489,
        "т": 5456151875302726462,
        "у": 5454053289857393595,
        "ф": 5454338918067479229,
        "х": 5454359744363895908,
        "ц": 5454131191974207370,
        "ч": 5456480702293877170,
        "ш": 5454080962331680684,
        "щ": 5456518863078301519,
        "ъ": 5454347190174490271,
        "ы": 5453878587767660028,
        "ь": 5454343273164316651,
        "э": 5456437748325948254,
        "ю": 5454207307384626821,
        "я": 5454275588774699252
    }

    async def ttecmd(self, message):
        '''<reply or args> - text to emoji - currently only ru'''

        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        if not reply and not args:
            return await utils.answer(message or reply, self.strings("notext"))
        text = args if not reply else reply.raw_text
        text_emojied = ""

        for _ in text.lower():
            text_emojied += _ if not self.emojis.get(_) else f'<emoji document_id={self.emojis[_]}>🥹</emoji>'

        return await utils.answer(message or reply, text_emojied)
