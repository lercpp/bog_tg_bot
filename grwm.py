import asyncio
from aiogram import Bot, Dispatcher, filters, types


bot = Bot(token="8562068554:AAFZ9X0JocATveQ2YR58A7NMtMuz7GJPZno")
dp = Dispatcher()
Command = filters.Command

@dp.message(filters.Command("menu"))
async def start(message):
    keyboard = [
        [types.KeyboardButton(text="Досье")],
        [types.KeyboardButton(text="Настройка агента")],
        [types.KeyboardButton(text="Статистика миссий")]
    ]
    keyboard_markup = types.ReplyKeyboardMarkup(keyboard=keyboard)
    await message.reply(
        "Добрый день! Воспользуетесь клавиатурой ниже:",
        reply_markup=keyboard_markup
    )

 @dp.message(lambda message: message.text == "Досье")
async def one(message):   
    await message.reply("Ваш уровень допуска:3")


 @dp.message(lambda message: message.text == "Настройка агента")
async def two(message):   
    await message.reply("Лол, а еще чего")

 @dp.message(lambda message: message.text == "Статистика миссий")
async def tri(message):   
    await message.reply("Статистика миссий:0")


async def main():
    await dp.start_polling(bot)

asyncio.run(main())

#3

bot = Bot(token="8562068554:AAFZ9X0JocATveQ2YR58A7NMtMuz7GJPZno")
dp = Dispatcher()
Command = filters.Command

@dp.message(filters.Command("help"))
async def start(message):
    keyboard = [
        [types.KeyboardButton(text="help")]
    ]
    keyboard_markup = types.ReplyKeyboardMarkup(keyboard=keyboard)
    await message.reply(
        "Доступные команды:",
        reply_markup=keyboard_markup
    )

 @dp.message(lambda message: message.text == "help")
async def one(message):   
    await message.reply("начало программы")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
