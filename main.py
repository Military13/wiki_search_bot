import telebot
import telebot.types as typ
from libs.message import messages
import wikipedia as wk
from telebot.apihelper import ApiTelegramException
from wikipedia.exceptions import PageError
BOT_TOKEN = "5956028445:AAGnFkWYAo1xv84IcaQpppyFww8lY4XDnjE"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=["start"])
def welcome_message(msg):
    language_keyboard = typ.InlineKeyboardMarkup(row_width=2)
    UZ = typ.InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="UZ")
    RU = typ.InlineKeyboardButton("🇷🇺 Русский", callback_data="RU")
    EN = typ.InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="EN")
    language_keyboard.add(UZ, RU, EN)
    print(msg.from_user)

    bot.send_message(msg.chat.id, messages(msg).select_language(), reply_markup=language_keyboard)

@bot.callback_query_handler(func= lambda call: True)
def callback_handlear(call):
    if call.data == "UZ":
        wk.set_lang("uz")
        bot.edit_message_text("O'zbek tili tanlandi.", call.from_user.id, call.message.id)
        bot.send_message(call.from_user.id, messages(call).welcome("UZ"))
    elif call.data == 'RU':
        wk.set_lang("ru")
        bot.edit_message_text("Был выбран русский язык.", call.from_user.id, call.message.id)
        bot.send_message(call.from_user.id, messages(call).welcome("RU"))
    elif call.data == 'EN':
        wk.set_lang("en")
        bot.edit_message_text("English was chosen.", call.from_user.id, call.message.id)
        bot.send_message(call.from_user.id, messages(call).welcome("EN"))


@bot.message_handler(func= lambda message: True)
def messsage_handlear(msg):
    if msg.text != "BACK":
        try:
            back_key = typ.ReplyKeyboardMarkup(resize_keyboard=True)
            back = typ.KeyboardButton("BACK")
            back_key.add(back)

            res = wk.summary(msg.text)
            bot.send_message(msg.chat.id, res, reply_markup=back_key)
        
        except Exception as e:
            back_key = typ.ReplyKeyboardMarkup(resize_keyboard=True)
            back = typ.KeyboardButton("BACK")
            back_key.add(back)

            if str(e) == "A request to the Telegram API was unsuccessful. Error code: 400. Description: Bad Request: message is too long":
                bot.send_message(msg.chat.id, messages(msg).TelegramParse("ALL"), reply_markup=back_key)
            else:
                bot.send_message(msg.chat.id, messages(msg).wiki_error(), reply_markup=back_key)
    else:
        language_keyboard = typ.InlineKeyboardMarkup(row_width=2)
        UZ = typ.InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="UZ")
        RU = typ.InlineKeyboardButton("🇷🇺 Русский", callback_data="RU")
        EN = typ.InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="EN")
        language_keyboard.add(UZ, RU, EN)

        bot.send_message(msg.chat.id, messages(msg).select_language(), reply_markup=language_keyboard)

print("Working...")
bot.polling(non_stop=True)
print("Stopped bot.")
