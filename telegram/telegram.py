import logging
import types

from aiogram import *

from keyboards import *
from secret_token import TOKEN
from command import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def call_start(message: types.Message):
    await message.answer(f"виберіть команду /tee_menu або /coffee_menu", reply_markup=buttons_start)


@dp.message_handler(commands=['tee_menu'])
async def call_ok(message: types.Message):
    await message.answer(f'Для замовлення ви вибрали чай {tee_menu}', reply_markup=buttons)


@dp.message_handler(text=order_tee[0])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[0]} ціна {price_tee[0]}!")


@dp.message_handler(text=order_tee[1])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[1]} ціна {price_tee[1]}!")


@dp.message_handler(text=order_tee[2])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[2]} ціна {price_tee[2]}!")


@dp.message_handler(text=order_tee[3])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[3]} ціна {price_tee[3]}!")


@dp.message_handler(text=order_tee[4])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[4]} ціна {price_tee[4]}!")


@dp.message_handler(text=order_tee[5])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[5]} ціна {price_tee[5]}!")


@dp.message_handler(text=order_tee[6])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[6]} ціна {price_tee[6]}!")


@dp.message_handler(text=order_tee[7])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[7]} ціна {price_tee[7]}!")


@dp.message_handler(text=order_tee[8])
async def with_puree(message: types.Message):
    await message.answer(f"Ви замовили {order_tee[8]} ціна {price_tee[8]}!")


@dp.message_handler(commands=['coffee_menu'])
async def call_ok(message: types.Message):
    await message.answer(f'Ви замовили каву виберіть що небудь:-{coffee_menu} ', reply_markup=buttons_coffee)


@dp.message_handler(text=coffee_order[0])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[0]} ціна {coffee_price[0]}')


@dp.message_handler(text=coffee_order[1])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[1]} ціна {coffee_price[1]}')


@dp.message_handler(text=coffee_order[2])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[2]} ціна {coffee_price[2]}')


@dp.message_handler(text=coffee_order[3])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[3]} ціна {coffee_price[3]}')


@dp.message_handler(text=coffee_order[4])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[4]} ціна {coffee_price[4]}')


@dp.message_handler(text=coffee_order[5])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[5]} ціна {coffee_price[5]}')


@dp.message_handler(text=coffee_order[6])
async def with_puree(message: types.Message):
    await message.answer(f'Ви замовили {coffee_order[6]} ціна {coffee_price[6]}')

@dp.message_handler(commands=['location'])
async def call_location(message: types.Message):
    await message.answer('Запити на дозвіл показу локації', reply_markup=buttons_location)

@dp.message_handler(commands=['contact'])
async def call_location(message: types.Message):
    await message.answer('Запити на дозвіл показу телефону', reply_markup=buttons_location_1)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)