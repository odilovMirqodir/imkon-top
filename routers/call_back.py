from aiogram import Router
from aiogram.types import CallbackQuery
from database.database import UserDatabase
from message_text.text import *
from buttons.buttons import *

call_back = Router(name=__name__)
db = UserDatabase()


@call_back.callback_query(lambda call: call.data == 'rekvizit')
async def rekvizit_reaction(call: CallbackQuery):
    user_id = call.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await call.message.answer(await rekvizit_text(user_language), parse_mode="markdown")
    await call.answer()


@call_back.callback_query(lambda call: call.data == 'karta')
async def karta_reaction(call: CallbackQuery):
    user_id = call.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await call.message.answer(await payment_text(user_language), parse_mode="markdown",
                              reply_markup=await payment_button(user_language))
