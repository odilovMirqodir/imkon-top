from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart
from message_text.text import *
from buttons.buttons import *
from database.database import UserDatabase
from aiogram.types import FSInputFile
from states.states import Form, CheckForm
from aiogram.fsm.context import FSMContext
import re
from aiogram import F
from config.config import IMKON_TOP_DATABASE, IMKON_TOP_CHECK, ALLOWED_ADMIN_ID

db = UserDatabase()
message_router = Router(name=__name__)


@message_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await db.create_table()
    user_id = message.from_user.id
    user = await db.get_user(user_id)

    if user:
        language = user[-1]
        await message.answer(await command_start_text_2(language), reply_markup=await main_button(language))
    else:
        full_name = message.from_user.full_name
        await message.answer(await command_start_text(full_name), parse_mode='markdown',
                             reply_markup=await language_keyboard())


@message_router.message(lambda message: message.text in ["🇺🇿 Uzbek", "🇷🇺 Русский"])
async def language_select_message(message: Message) -> None:
    user_id = message.from_user.id
    language = await get_user_language(message.text)

    all_info_users = await db.get_user(user_id)
    user_exists = await db.user_exists(user_id)

    if all_info_users and user_exists:
        await db.update_language(user_id, language)
        await message.answer(
            "✅ Til o‘zgartirildi!" if language == "uz" else "✅ Язык изменен!",
            reply_markup=await main_button(language)
        )
    else:
        username = '@' + (message.from_user.username or "no_username")
        first_name = message.from_user.first_name or ""
        full_name = message.from_user.full_name or ""

        await db.add_user(user_id, username, first_name, full_name, language)

        shartnoma_path = 'shartnoma/shartnoma.docx'
        document = FSInputFile(shartnoma_path)
        await message.answer_document(
            document,
            caption=await shartnoma_text(language),
            reply_markup=await shartnoma_button(language)
        )


@message_router.message(lambda message: message.text in ["Tanishdim ✅", "Ознакомился ✅"])
async def tanishdim(message: Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    lang_result = await db.get_user_language(user_id)

    user_language = lang_result[0] if lang_result else 'uz'
    await message.answer(await ism_familya_text(user_language), parse_mode='markdown',
                         reply_markup=ReplyKeyboardRemove())

    await state.set_state(Form.ism_familya)


@message_router.message(Form.ism_familya)
async def process_ism_familya(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'

    if len(message.text.split()) == 2:
        await state.update_data(ism_familya=message.text.strip())
        await message.answer(await phone_number_text(user_language), parse_mode='markdown',
                             reply_markup=await send_phone_number(user_language))
        await state.set_state(Form.phone_number)
    else:
        await message.answer(await error_ism_familya_text(user_language), parse_mode='markdown')


@message_router.message(Form.phone_number)
async def process_phone_number(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'

    if message.contact and message.contact.phone_number:
        phone_number = message.contact.phone_number
        await state.update_data(phone_number=phone_number)
        await message.answer(await passport_id_text(user_language), parse_mode='markdown',
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.passport_id)
    else:
        await message.answer(await error_phone_number(user_language), parse_mode='markdown')


@message_router.message(Form.passport_id)
async def process_passport_id(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'

    passport_id = message.text.strip().upper()

    if re.fullmatch(r'[A-Z]{2}\d{7}', passport_id):
        await state.update_data(passport_id=passport_id)
        await message.answer(await passport_image_text(user_language), parse_mode='markdown')
        await state.set_state(Form.passport_image)
    else:
        await message.answer(await error_passport_id(user_language), parse_mode='markdown')


@message_router.message(Form.passport_image)
async def process_passport_image(message: Message, state: FSMContext):
    if message.photo:
        user_id = message.from_user.id
        language_result = await db.get_user_language(user_id)
        user_language = language_result[0] if language_result else 'uz'

        photo = message.photo[-1]
        file_id = photo.file_id
        await state.update_data(passport_image=file_id)

        data = await state.get_data()
        ism_familya = data.get('ism_familya', 'Noma’lum')
        phone_number = data.get('phone_number', 'Noma’lum')
        passport_id = data.get('passport_id', 'Noma’lum')

        await message.answer_photo(file_id, caption=await confirm_info(language=user_language, ism_familya=ism_familya,
                                                                       phone_number=phone_number,
                                                                       passport_id=passport_id), parse_mode="Markdown",
                                   reply_markup=await yes_no_button(user_language))
        await state.set_state(Form.confirmation)
    else:
        user_id = message.from_user.id
        language_result = await db.get_user_language(user_id)
        user_language = language_result[0] if language_result else 'uz'
        await message.answer(await error_passport_image(user_language), parse_mode='markdown')


@message_router.message(Form.confirmation)
async def process_confirmation(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    user_text = message.text.strip()

    yes_answers = ["✅ To‘g‘ri", "✅ Да"]

    if user_text in yes_answers:
        data = await state.get_data()
        ism_familya = data.get('ism_familya', 'Noma’lum')
        phone_number = data.get('phone_number', 'Noma’lum')
        passport_id = data.get('passport_id', 'Noma’lum')
        passport_image = data.get('passport_image')
        all_info_for_user = await db.get_user(user_id)
        username = all_info_for_user[1]
        first_name = all_info_for_user[2]
        full_name = all_info_for_user[3]
        telegram_lanaguage = all_info_for_user[-1]

        await message.answer(await success_text(user_language), reply_markup=await main_button(user_language))
        await message.bot.send_photo(chat_id=IMKON_TOP_DATABASE, photo=passport_image,
                                     caption=await send_caption(ism_familya=ism_familya, username=username,
                                                                first_name=first_name, full_name=full_name,
                                                                telegram_lanaguage=telegram_lanaguage,
                                                                passport_id=passport_id, phone_number=phone_number),
                                     parse_mode="markdown")

        await state.clear()

    else:
        if user_language == 'uz':
            await message.answer("🔄 Qaytadan boshlash uchun ismingiz va familiyangizni kiriting:")
        else:
            await message.answer("🔄 Введите свое имя и фамилию для повторного ввода:")

        await state.set_state(Form.ism_familya)


@message_router.message(lambda message: message.text in ['✅ Chekni yuborish', '✅ Отправить чек'])
async def get_check_reaction(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(await send_check_image_text(user_language), parse_mode='markdown')
    await state.set_state(CheckForm.image)


@message_router.message(CheckForm.image)
async def handle_check_image(message: Message, state: FSMContext):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'

    if not message.photo:
        await message.answer(await warning_text_image(user_language), parse_mode='markdown')
        return

    photo = message.photo[-1]

    user_data = await db.get_user(user_id)
    if user_data:
        full_name = user_data[-2]
        username = user_data[1]
        first_name = user_data[2]
    else:
        full_name = message.from_user.full_name
        username = message.from_user.username or "yo'q"
        first_name = message.from_user.first_name or "Noma'lum"

    caption = await success_check_text(
        language=user_language,
        full_name=full_name,
        first_name=first_name,
        username=username,
        user_id=user_id
    )

    await message.bot.send_photo(
        chat_id=IMKON_TOP_CHECK,
        photo=photo.file_id,
        caption=caption
    )

    await message.answer(await confirm_text(user_language), parse_mode='markdown')

    await state.clear()


@message_router.message(lambda message: message.text in ['🌐 Сменить язык', '🌐 Tilni o\'zgartirish'])
async def get_check_reaction(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(await select_language_text(user_language), parse_mode='markdown',
                         reply_markup=await language_keyboard())


@message_router.message(lambda message: message.text in ['💳 To\'lov', '💳 Оплата'])
async def get_payment_reaction(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(await payment_text(user_language), parse_mode='markdown',
                         reply_markup=await rekvizit_and_karta(user_language))


@message_router.message(lambda message: message.text in ['📍 Наш адрес', '📍 Bizning Manzil'])
async def get_location_reaction(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(
        await location_text(user_language),
        parse_mode='markdown',
        reply_markup=await main_button(user_language)
    )
    await message.bot.send_location(
        chat_id=message.chat.id,
        latitude=41.356066,
        longitude=69.204727
    )


@message_router.message(lambda message: message.text == 'Rekvizit')
async def rekvizit_reaction(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(await rekvizit_text(user_language), parse_mode="markdown")


@message_router.message(lambda message: message.text == 'Karta')
async def karta_reaction(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(
        await payment_text(user_language),
        parse_mode="markdown",
        reply_markup=await payment_button(user_language)
    )


@message_router.message(lambda message: message.text in ['⬅️ Назад', '⬅️ Ortga'])
async def go_back_button(message: Message):
    user_id = message.from_user.id
    language_result = await db.get_user_language(user_id)
    user_language = language_result[0] if language_result else 'uz'
    await message.answer(await command_start_text_2(user_language), reply_markup=await main_button(user_language))


@message_router.message(F.text == "/select_users")
async def select_users_command(message: Message):
    if message.from_user.id != int(ALLOWED_ADMIN_ID):
        await message.answer("❌ Sizda bu komandani ishlatishga ruxsat yo'q.")
        return

    all_users = await db.select_all_users_count()
    await message.answer(f"👥 Foydalanuvchilar soni: {all_users} ta")
