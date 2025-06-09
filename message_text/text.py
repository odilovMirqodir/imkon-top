async def command_start_text(full_name):
    text = f"*Assalomu alaykum,{full_name}!\nBotga xush kelibsiz\n\nЗдравствуйте,{full_name}!\nДобро пожаловать в бота*"
    return text


async def command_start_text_2(language):
    text = "👋 Xush kelibsiz, siz avval ro‘yxatdan o‘tgansiz!" if language == 'uz' else "👋 Добро пожаловать, вы уже зарегистрировались!"
    return text


async def get_user_language(language):
    return 'uz' if language == '🇺🇿 Uzbek' else 'ru'


async def shartnoma_text(language):
    return '📄 Shartnoma bilan tanishing' if language == 'uz' else '📄 Ознакомиться с договором'


async def ism_familya_text(user_language):
    text = "*Ismingizni kiriting\nNamuna: Aziz Azizov*" if user_language == "uz" else "*Введите ваше имя и фамилию\nПример: Азиз Азизов*"
    return text


async def phone_number_text(user_language):
    text = "*Telefon raqamingizni yuboring*" if user_language == "uz" else "*Отправьте свой номер*"
    return text


async def error_ism_familya_text(user_language):
    text = "*Ismingizni namuna bo‘yicha kiriting: Aziz Azizov*" if user_language == "uz" else "*Введите имя и фамилию, например: Азиз Азизов*"
    return text


async def error_phone_number(language):
    text = "*Telefon raqamingizni qaytadan yuboring*" if language == 'uz' else "*Отправьте свой номер телефона еще раз*"
    return text


async def passport_id_text(language):
    text = "*Passport ID ni kiriting: AB1234567*" if language == 'uz' else "*Введите идентификатор вашего паспорта: AB1234567*"
    return text


async def passport_image_text(language):
    text = "*Passport rasmingizni yuboring*" if language == 'uz' else "*Отправьте фото паспорта*"
    return text


async def error_passport_id(language):
    text = "❌ Pasport seriyasini quyidagi ko‘rinishda kiriting: *AB1234567*" if language == 'uz' else "❌ Введите серию паспорта в формате: *AB1234567*"
    return text


async def error_passport_image(language):
    text = "*Iltimos, passport rasmini yuboring!*" if language == 'uz' else "*Пожалуйста, отправьте фото паспорта!*"
    return text


async def confirm_info(language, ism_familya, phone_number, passport_id):
    text_uz = (
        f"*Kiritgan ma’lumotlaringiz:*\n\n"
        f"*Ism Familya:* {ism_familya}\n"
        f"*Telefon:* {phone_number}\n"
        f"*Passport ID:* {passport_id}\n\n"
        f"✅ *Ma’lumotlar to‘g‘rimi?*"
    )

    text_ru = (
        f"*Введённые вами данные:*\n\n"
        f"*Имя и Фамилия:* {ism_familya}\n"
        f"*Телефон:* {phone_number}\n"
        f"*Паспорт ID:* {passport_id}\n\n"
        f"✅ *Данные верны?*"
    )

    return text_uz if language == 'uz' else text_ru


async def success_text(language):
    text = "✅ Ma’lumotlaringiz yuborildi. Rahmat!" if language == 'uz' else "✅ Ваши данные отправлены. Спасибо!"
    return text


async def send_caption(ism_familya, username, first_name, full_name, telegram_lanaguage, phone_number, passport_id):
    caption = (
        f"*Yangi foydalanuvchi ma’lumoti:*\n\n"
        f"*Ism Familya:* {ism_familya}\n"
        f"*Username:* {username}\n"
        f"*FirstName:* {first_name}\n"
        f"*FullName:* {full_name}\n"
        f"*Telegram Language:* {telegram_lanaguage}\n"
        f"*Telefon:* {phone_number}\n"
        f"*Passport ID:* {passport_id}"
    )
    return caption


async def send_check_image_text(language):
    text = "*Check rasmini yuboring*" if language == 'uz' else "*Отправьте фото чека*"
    return text


async def success_check_text(language, full_name, first_name, username, user_id):
    caption_uz = (
        f"🧾 Yangi chek!\n"
        f"👤 To‘liq ism: {full_name}\n"
        f"🧑‍💼 Ism: {first_name}\n"
        f"🔗 Username: {username}\n"
        f"🌐 Til: {language}\n"
        f"🆔 ID: {user_id}"
    )
    return caption_uz


async def warning_text_image(language):
    warning_text = "*❌ Iltimos, faqat rasm yuboring.*" if language == 'uz' else "*❌ Пожалуйста, отправьте только фото.*"
    return warning_text


async def confirm_text(language):
    confirm_text = "*✅ Rasm qabul qilindi va adminga yuborildi. Rahmat!*" if language == 'uz' else "*✅ Фото получено и отправлено администратору. Спасибо!*"
    return confirm_text


async def select_language_text(language):
    confirm_text = "*Tillardan birini tanlang*" if language == 'uz' else "*Выберите один из языков*"
    return confirm_text


async def payment_text(language):
    text = f"*To'lov turini tanlang*" if language == 'uz' else "*Выберите тип платежа*"
    return text


async def location_text(language):
    text = f"*Bizning manzil 📍\nKamariniso ko'chasi, Toshkent, Yunusobod, O'zbekiston*" if language == 'uz' else "*Наш адрес 📍\nКамаринисо улица, Ташкент, Yunusabad, Узбекистан*"
    return text


async def rekvizit_text(language):
    if language == "uz":
        text = (
            "*МЧЖ 'MED INVEST KLASTER'*\n"
            "📍 *Yuridik manzil:*\n"
            "O‘zbekiston Respublikasi, Sirdaryo viloyati,\n"
            "Sirdaryo tumani, Baxt, Yuqumli kasalliklar binosi, 1-qavat.\n\n"
            "🏦 *Hisob raqami:* 2020 8000 9054 6819 8001\n"
            "AKIB \"Ipoteka bank\",\n"
            "Toshkent shahar, Yakkasaroy filiali\n\n"
            "🏢 *MFO:* 01017\n"
            "💼 *STIR:* 309101935\n"
            "📂 *OKED:* 47290\n\n"
            "‼️ Bank xodimiga *ism-familiyangizni* va *to‘liq maqsadi* degan joyida\n"
            "'*Biznes g‘oyani o‘rganish maqsadida*' deb yozib qoldiring."
        )
    else:
        text = (
            "*ООО 'MED INVEST KLASTER'*\n"
            "📍 *Юридический адрес:*\n"
            "Республика Узбекистан, Сырдарьинская область,\n"
            "Сырдарьинский район, Бахт, здание инфекционных болезней, 1 этаж.\n\n"
            "🏦 *Расчётный счёт:* 2020 8000 9054 6819 8001\n"
            "АКИБ \"Ипотека банк\",\n"
            "г. Ташкент, филиал Яккасарай\n\n"
            "🏢 *МФО:* 01017\n"
            "💼 *ИНН:* 309101935\n"
            "📂 *ОКЭД:* 47290\n\n"
            "‼️ Сотруднику банка укажите *ФИО* и в графе *цель платежа* напишите:\n"
            "'*В целях изучения бизнес-идеи*'."
        )

    return text
