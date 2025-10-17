from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, URLInputFile
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, CallbackQuery)
from aiogram.utils.keyboard import InlineKeyboardBuilder


from db_bot.app import new_user, get_word, add_word_to_the_vocabulary, get_vocabulary
from keyboards.keyboards import inline_add_to_vocab, create_pagination_keyboard


router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    image = URLInputFile(
        "https://avatars.dzeninfra.ru/get-zen_brief/6488213/pub_62d159f2ebe438762b152033_62d159f2ebe438762b152034/scale_1200",
        filename="python-logo.png"
    )
    new_user(message.from_user.id)
    await message.answer_photo(image)
    await message.answer(text='ЕБАННЫЙ РОТ ПОГНАЛИ НАХУЙ\n\n<<<Введите слово для поиска>>>')

@router.callback_query(F.data=='add_to_vocabulary')
async def add_to_the_vocabulary(callback: CallbackQuery):
    #print(callback.message.text)
    result = add_word_to_the_vocabulary(get_word(callback.message.text.split(' ')[0]), user=callback.from_user.id)
    await callback.message.answer(text=f'{result}')

@router.callback_query(F.data=='to_see_all_words')
async def to_see_all_words(callback: CallbackQuery):
    words = get_vocabulary(callback.from_user.id)
    text = ''
    if len(words)>10:

        for index, value in enumerate(words[-10:]):
            text+=f'{index+1}) {value}\n'

        await callback.message.answer(text=text)
    elif not words:
        await callback.message.answer(text='Словарь пуст')
    else:
        for index, value in enumerate(words):
            text += f'{index + 1}) {value}\n'
        await callback.message.answer(text=text)


@router.message()
async def find_the_word(message: Message):
    word = get_word(message.text.lower())
    if word:
        await message.answer(text=f'{word.english} -- {word.russian}', reply_markup=inline_add_to_vocab)
    else:
        await message.answer(text='Пока что такого слова нет в словаре')