import telebot

TOKEN = '8089904975:AAGCWLZSQpo-EHUFHUoLgQt1w3xHYEcd_u4'
CHANNEL_ID = -1005127409847 
SECRET_LINK = 'https://rrrrrr.vercel.app/'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = telebot.types.InlineKeyboardMarkup()
    # Замени на свою реальную ссылку на канал!
    btn = telebot.types.InlineKeyboardButton("Подписаться 📢", url="https://t.me/cicitimoxi")
    chk = telebot.types.InlineKeyboardButton("Проверить ✅", callback_data="c")
    kb.add(btn); kb.add(chk)
    bot.send_message(m.chat.id, "Привет! Подпишись на канал, чтобы увидеть итоги года в МЭШ!", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data == "c")
def check(c):
    try:
        s = bot.get_chat_member(CHANNEL_ID, c.from_user.id).status
        if s in ['member', 'administrator', 'creator']:
            bot.send_message(c.message.chat.id, f"Проверка пройдена! Твои итоги года здесь: {SECRET_LINK}")
        else:
            bot.answer_callback_query(c.id, "Вы не подписаны! ❌", show_alert=True)
    except:
        bot.send_message(c.message.chat.id, "Админка! Сделай бота админом в канале.")

bot.polling(none_stop=True)
