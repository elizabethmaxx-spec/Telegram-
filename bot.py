import telebot

# Твои данные
TOKEN = '8089904975:AAGCWLZSQpo-EHUFHUoLgQt1w3xHYEcd_u4'
CHANNEL_ID = -1005127409847 
CHANNEL_URL = 'https://t.me/cicitimoxi'
SECRET_LINK = 'https://rrrrrr.vercel.app/'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    # Создаем кнопки
    kb = telebot.types.InlineKeyboardMarkup()
    
    # Кнопка подписаться (теперь ведет на твой канал)
    btn = telebot.types.InlineKeyboardButton("Подписаться на МЭШ Инфо 📢", url=CHANNEL_URL)
    
    # Кнопка проверки
    chk = telebot.types.InlineKeyboardButton("Я подписался! ✅", callback_data="c")
    
    kb.add(btn)
    kb.add(chk)
    
    welcome_text = (
        "<b>Добро пожаловать в систему проверки итогов года МЭШ!</b>\n\n"
        "Чтобы получить доступ к своим оценкам и годовой статистике, "
        "необходимо быть подписанным на наш официальный канал."
    )
    
    bot.send_message(m.chat.id, welcome_text, parse_mode="HTML", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "c")
def check(c):
    try:
        # Проверяем статус пользователя в канале
        s = bot.get_chat_member(CHANNEL_ID, c.from_user.id).status
        
        if s in ['member', 'administrator', 'creator']:
            bot.answer_callback_query(c.id, "Доступ разрешен!")
            bot.send_message(
                c.message.chat.id, 
                f"✅ Проверка пройдена! Твои персональные итоги года доступны по ссылке:\n\n{SECRET_LINK}"
            )
        else:
            bot.answer_callback_query(
                c.id, 
                "Вы не подписаны на канал! ❌\nСначала подпишитесь, а потом нажмите кнопку проверки.", 
                show_alert=True
            )
    except Exception as e:
        # Если бота не добавили в админы
        bot.send_message(c.message.chat.id, "Ошибка: бот должен быть администратором канала @cicitimoxi для проверки подписки!")

# Запуск бота
print("Бот запущен...")
bot.polling(none_stop=True)
