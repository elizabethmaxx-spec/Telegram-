import telebot

# Твои финальные данные
TOKEN = '8089904975:AAGCWLZSQpo-EHUFHUoLgQt1w3xHYEcd_u4'
CHANNEL_ID = -1003558370707 
CHANNEL_URL = 'https://t.me/cicitimoxi'
# Новая правильная ссылка на твой сайт
SECRET_LINK = 'https://mash-this-year.vercel.app/'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("Подписаться на МЭШ Инфо 📢", url=CHANNEL_URL)
    chk = telebot.types.InlineKeyboardButton("Я подписался! ✅", callback_data="c")
    kb.add(btn)
    kb.add(chk)
    
    welcome_text = (
        "<b>📊 Итоги года в МЭШ 2024-2025</b>\n\n"
        "Для получения доступа к аналитике ваших оценок, прогулов и рейтинга в классе, "
        "необходимо подтвердить подписку на информационный канал."
    )
    bot.send_message(m.chat.id, welcome_text, parse_mode="HTML", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "c")
def check(c):
    try:
        # Проверка подписки по правильному ID канала
        status = bot.get_chat_member(CHANNEL_ID, c.from_user.id).status
        if status in ['member', 'administrator', 'creator']:
            bot.answer_callback_query(c.id, "Доступ разрешен!")
            bot.send_message(
                c.message.chat.id, 
                f"✅ <b>Проверка пройдена!</b>\n\nВаша персональная статистика сформирована и доступна по ссылке:\n👉 {SECRET_LINK}",
                parse_mode="HTML"
            )
        else:
            bot.answer_callback_query(
                c.id, 
                "Ошибка! Вы не подписаны на канал ❌", 
                show_alert=True
            )
    except Exception:
        bot.send_message(c.message.chat.id, "Ошибка: Бот должен быть админом в @cicitimoxi")

bot.polling(none_stop=True)
