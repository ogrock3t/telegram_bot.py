import time
import logging
import random

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "..."

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}! \nЯ Бот для игры Правда или Действие")
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Клик", url="https://t.me/..._proverka"))
    await bot.send_message(message.chat.id, "Подпишись на канал, чтобы мной пользоваться\nПотом напиши мне /help", reply_markup=markup)


@dp.message_handler(commands=['help'])
async def website(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    TRY = types.KeyboardButton("Правда")
    ACT = types.KeyboardButton("Действие")
    markup.add(TRY, ACT)
    await bot.send_message(message.chat.id, "Посмотри подсказки", reply_markup=markup)

@dp.message_handler()
async def get_user_text(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    if message.text ==  "Правда":
        await bot.send_message(message.chat.id, (random.choice(list(open('try.txt', encoding='utf-8')))))
    elif message.text == "Действие":
        await bot.send_message(message.chat.id, (random.choice(list(open('act.txt', encoding='utf-8')))))
    else:
        await bot.send_message(message.chat.id, "Такой команды не существует.")



if __name__ == '__main__':
    executor.start_polling(dp)

