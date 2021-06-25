import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, utils, types
from aiogram.types import ParseMode
from config import TOKEN, URL
from db import process_search_model, init_db, find_id_search, find_all_cards
from parser import ParseVideoCard
from logger import MyLogger
# from db import users

logger = MyLogger('Custom')

logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'go'])
# def start_handler(message):
#     ids = {}# массив с айди пользователей, которые допущены
#     if message.from_user.id not in ids:
#         dp.send_message(message.chat.id, 'Ошибка доступа')
#     else:
#         msg = dp.send_message(message.chat.id, "Привет:)", reply_markup=action)
#         dp.register_next_step_handler(msg, chosen)

#
# @dp.message_handler(commands=['start', 'go'])
# def start_handler(message):
#     msg = dp.send_message(message.chat.id, "Привет, отправь логин и пароль")
#     dp.register_next_step_handler(msg, auth)


# def auth(message):
#     data = message.text.split() # создаем список ['логин', 'пароль']
#
#     check = users.find_one({ # проверяем наличие в базе комбинации логина и пароля
#         'username': str(data['username']),
#         'password': str(data['password']),
#     })
#
#     if check is None: # если такой комбинации не существует, ждём команды /start Опять
#         dp.send_message(message.chat.id, r'Неправильно введен логин\пароль')
#
#     else: # а если существует, переходим к следующему шагу
#         msg = dp.send_message(message.chat.id, 'Что будем делать?')
#         dp.register_next_step_handler(msg, next_step_func)



@dp.message_handler(commands='list')
async def send_list(message: types.Message):
    logger.message('Running list function')
    search_models = find_id_search(message.chat.id)
    print("find_id_search type is: {0}".format(type(find_id_search(message.chat.id))))
    cards = find_all_cards()
    print("find_all_cards type is: {0}".format(type(find_all_cards())))
    for card in cards:
        card_title = card.title
        for search_model in search_models:
            search_title = search_model.title
            if card_title.find(search_title) >= 0:
                message_text = 'Строка поиска {} \r\n Найдено {}'.format(search_title, utils.markdown.hlink(card_title,
                                                                                                            card.url))
                await message.answer(text=message_text, parse_mode=ParseMode.HTML)


@dp.message_handler(commands='search')
async def send_search(message: types.Message):
    search_models = find_id_search(message.chat.id)
    await process_search_model(message)
    print("process_search_model type is: {0}".format(type(process_search_model(message))))
    for search_model in search_models:
        await message.answer(text=search_model.title)
    logger.message('Showed list of queries')


@dp.message_handler()
async def echo(message: types.Message):
    await process_search_model(message)
    print("process_search_model type is: {0}".format(type(process_search_model(message))))
    logger.message('Sended data to db')


async def scheduled(wait_for, parser):
    logger.message('Checking item enable')
    while True:
        await asyncio.sleep(wait_for)
        await parser.parse()


if __name__ == '__main__':
    init_db()
    parser = ParseVideoCard(url=URL, bot=bot)
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10, parser))
    executor.start_polling(dp, skip_updates=True)
    send_list('/list')
