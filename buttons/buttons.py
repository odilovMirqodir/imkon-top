from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


async def language_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇺🇿 Uzbek")],
            [KeyboardButton(text="🇷🇺 Русский")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard


async def shartnoma_button(language):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Tanishdim ✅" if language == 'uz' else "Ознакомился ✅")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard


async def send_phone_number(language):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Telefon raqam ☎️" if language == 'uz' else "Номер телефона ☎️",
                            request_contact=True)],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard


async def yes_no_button(language):
    if language == 'uz':
        yes_text = "✅ To‘g‘ri"
        no_text = "❌ Qaytadan kiritish"
    else:
        yes_text = "✅ Да"
        no_text = "❌ Ввести заново"

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=yes_text), KeyboardButton(text=no_text)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard


async def main_button(language):
    if language == "uz":
        buttons = [
            [
                KeyboardButton(text="📍 Bizning Manzil"),
                KeyboardButton(text="✅ Chekni yuborish")
            ],
            [
                KeyboardButton(text="💳 To'lov"),
                KeyboardButton(text="ℹ️ Biz haqimizda")
            ],

            [
                KeyboardButton(text="🌐 Tilni o'zgartirish")
            ]
        ]
    else:
        buttons = [
            [
                KeyboardButton(text="📍 Наш адрес"),
                KeyboardButton(text="✅ Отправить чек")
            ],
            [
                KeyboardButton(text="💳 Оплата"),
                KeyboardButton(text="ℹ️ О нас")
            ],
            [KeyboardButton(text="🌐 Сменить язык")]
        ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return keyboard


async def payment_button(language: str) -> InlineKeyboardMarkup:
    if language == "uz":
        payme_text = "💳 Payme"
        click_text = "💳 Click"
    else:
        payme_text = "💳 Payme"
        click_text = "💳 Click"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=payme_text, url="https://payme.uz/"),
            InlineKeyboardButton(text=click_text, url="https://click.uz/")
        ]
    ])
    return keyboard


async def rekvizit_and_karta(language):
    if language == "uz":
        rekvizit_text = "Rekvizit"
        karta_text = "Karta"
    else:
        rekvizit_text = "Реквизит"
        karta_text = "Карта"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=rekvizit_text, callback_data="rekvizit"),
            InlineKeyboardButton(text=karta_text, callback_data='karta')
        ]
    ])
    return keyboard
