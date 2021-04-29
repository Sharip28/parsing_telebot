from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(row_width=4)
for i in range(4):
    btn1 = InlineKeyboardButton(str(i * 4 + 1), callback_data=str(i * 4 + 1))
    btn2 = InlineKeyboardButton(str(i * 4 + 2), callback_data=str(i * 4 + 2))
    btn3 = InlineKeyboardButton(str(i * 4 + 3), callback_data=str(i * 4 + 3))
    btn4 = InlineKeyboardButton(str(i * 4 + 4), callback_data=str(i * 4 + 4))
    inline_keyboard.add(btn1, btn2, btn3, btn4)
