import time
import telebot
from background import keep_alive
from telebot import types

bot = telebot.TeleBot("6923333853:AAGvQRy-mXlgjn0D0kPiCZyCvb-U8slj3P0")

def start_markup():
  markup = types.InlineKeyboardMarkup(row_width=True)
  link_keyboard1 = types.InlineKeyboardButton(text="Канал",
                                              url="https://t.me/instarsxxx")
  link_keyboard2 = types.InlineKeyboardButton(text="Второй канал",
                                              url="https://t.me/yumfolder") # URL второго канала
  check_keyboard = types.InlineKeyboardButton(text="Keronkes",
                                              callback_data="check")
  markup.add(link_keyboard1, link_keyboard2, check_keyboard)
  return markup

@bot.message_handler(commands=["start"])
def start(message):
  chat_id = message.chat.id
  first_name = message.chat.first_name
  time.sleep(1)
  bot.send_message(
      chat_id,
      f"Привет {first_name}!\nЧтобы получить фул подпишитесь на каналы!🤑",
      reply_markup=start_markup())

def is_subscribed(chat_id, user_id):
  try:
    response = bot.get_chat_member(chat_id, user_id)
    if response.status == 'left':
      return False
    else:
      return True
  except telebot.apihelper.ApiTelegramException as e:
    if e.result_json['description'] == 'Bad Request: user not found':
      return False

def check(call):
  if is_subscribed(chat_id="-1001933827160", user_id=call.message.chat.id) and is_subscribed(chat_id="-1002090914980", user_id=call.message.chat.id): # ID второго канала
    time.sleep(1)
    bot.send_message(call.message.chat.id, "Ваша ссылка сэр https://mega.nz/folder/Mi8WSJpR#fKbgFschHDeURNtylTnrYA😉")
  else:
    time.sleep(1)
    bot.send_message(call.message.chat.id,
                     "Подпишитесь",
                     reply_markup=start_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == 'check':
    check(call)

keep_alive()
bot.polling()
