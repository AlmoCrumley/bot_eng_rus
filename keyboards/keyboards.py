from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

to_see_all_words = InlineKeyboardButton(
    text="Список добавленных слов", callback_data="to_see_all_words"
)

add_to_vocabulary_btn = InlineKeyboardButton(
    text="Добавить в словарь", callback_data="add_to_vocabulary"
)


# Создаем объект инлайн-клавиатуры
inline_add_to_vocab = InlineKeyboardMarkup(inline_keyboard=[[add_to_vocabulary_btn], [to_see_all_words]])

#инлайн квлавиатура пагинации
def create_pagination_keyboard():
    forward_btn = InlineKeyboardButton(
        text=">>", callback_data="forward"
    )
    backward_btn = InlineKeyboardButton(
        text="<<", callback_data="backward"
    )

    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(backward_btn, forward_btn)
    return kb_builder.as_markup()