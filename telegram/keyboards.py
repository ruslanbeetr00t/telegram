from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from command import *

keyboard_1 = KeyboardButton(order_tee[0])
keyboard_2 = KeyboardButton(order_tee[1])
keyboard_3 = KeyboardButton(order_tee[2])
keyboard_4 = KeyboardButton(order_tee[3])
keyboard_5 = KeyboardButton(order_tee[4])
keyboard_6 = KeyboardButton(order_tee[5])
keyboard_7 = KeyboardButton(order_tee[6])
keyboard_8 = KeyboardButton(order_tee[7])
keyboard_9 = KeyboardButton(order_tee[8])

buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(keyboard_1, keyboard_2, keyboard_3).row(keyboard_4, keyboard_5,
                                                                                                keyboard_6).row(
    keyboard_7, keyboard_8, keyboard_9)

keyboard_coffee_1 = KeyboardButton(coffee_order[0])
keyboard_coffee_2 = KeyboardButton(coffee_order[1])
keyboard_coffee_3 = KeyboardButton(coffee_order[2])
keyboard_coffee_4 = KeyboardButton(coffee_order[3])
keyboard_coffee_5 = KeyboardButton(coffee_order[4])
keyboard_coffee_6 = KeyboardButton(coffee_order[5])
keyboard_coffee_7 = KeyboardButton(coffee_order[6])

buttons_coffee = ReplyKeyboardMarkup(resize_keyboard=True).add(keyboard_coffee_1).add(keyboard_coffee_2).add(
    keyboard_coffee_3).add(keyboard_coffee_4).add(keyboard_coffee_5).add(keyboard_coffee_6).add(keyboard_coffee_7)

start_keyboard = KeyboardButton('/start')
buttons_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_start.add(start_keyboard)


location_keyboard = KeyboardButton('/location', request_location=True)
buttons_location = ReplyKeyboardMarkup(resize_keyboard=True)
buttons_location.add(location_keyboard)

location_keyboard_1 = KeyboardButton('/phone', request_contact=True)
buttons_location_1 = ReplyKeyboardMarkup(resize_keyboard=True)
buttons_location_1.add(location_keyboard_1)