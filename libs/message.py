class messages:
    def __init__(self, ctx):
        self.ctx = ctx

    def select_language(self):
        return "Tilni tanlang.\nВыберите язык.\nSelect a language.\n\n<b>Developen by <u>@AzizbekDeveloper</u></b>"

    def welcome(self, LANG):
        if LANG == "UZ":
            return "Assalomu Alaykum <b>{}</b> , Bizning bot orqali Telegramdan chiqmasdan turib <b>wikipedia</b> sayti orqali qidirishingiz mumkun😉. Sizni qiziqtirgan savolni yuboring.".format(self.ctx.from_user.first_name)
        elif LANG == "RU":
            return "Здравствуйте, <b>{}</b>, вы можете искать через нашего бота в Википедии, не выходя из Telegram😉. Задайте интересующий вас вопрос.".format(self.ctx.from_user.first_name)
        elif LANG == "EN":
            return "Hello <b>{}</b>, you can search through our bot on wikipedia without leaving Telegram😉. Post a question that interests you.".format(self.ctx.from_user.first_name)
    
    def TelegramParse(self, LANG):
        if LANG == "UZ":
            return "Qadirli <b>{}</b>. Kechirasiz ushbu natijani telegram Tahlil qilolmayapdi. Qaytadan urunib ko'ring.".format(self.ctx.from_user.first_name)
        elif LANG == "RU":
            return "Дорогой <b>{}</b>. Извините, Telegram не может проанализировать этот результат. Пожалуйста, попробуйте еще раз.".format(self.ctx.from_user.first_name)
        elif LANG == "EN":
            return "Dear <b>{}</b>. Sorry <b><i>Telegram</i></b> can't analyze this result. Please try again.".format(self.ctx.from_user.first_name)
        else:
            return """Qadirli <b>{}</b>. Kechirasiz ushbu natijani telegram Tahlil qilolmayapdi. Qaytadan urunib ko'ring.\nДорогой <b>{}</b>. Извините, Telegram не может проанализировать этот результат. Пожалуйста, попробуйте еще раз.\nDear <b>{}</b>. Sorry <b><i>Telegram</i></b> can't analyze this result. Please try again.""".format(self.ctx.from_user.first_name, self.ctx.from_user.first_name, self.ctx.from_user.first_name)
    def wiki_error(self):
        return f"Wikipedia dan ushbu mavzu topilmadi yoku ma'lumot tahrirlanmayapdi. Qaytadan urinib ko'ring.\n\nThis topic could not be found on Wikipedia or the information is not being edited. Please try again.\n\nЭту тему невозможно найти в Википедии или информация не редактируется. Пожалуйста, попробуйте еще раз."