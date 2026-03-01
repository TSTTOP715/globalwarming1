import telebot
import random
import time

bot = telebot.TeleBot("8288633325:AAHB23BF1PCDYet3aoIaOtssxU9CeP9uxcM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот специализирующийся на всём что связано с глобальным потеплением. Чтобы узнать актуальные новости о глобальном потеплении напишите команду /news. Чтобы пожертвовать деньги на борьбу с глобальным потеплением напишите команду /donate. Чтобы узнать актуальное повышение температуры от нормы напишите команду /temp/")

@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    

@bot.message_handler(commands=['news'])
def send_hello(message):
    news_class = { "news1": ["По этой ссылке вы сможете прочитать статью о предположении российского синоптика с чем связана снежная зима 2026 года (https://iz.ru/2047157/2026-02-22/sinoptik-predpolozhil-sviaz-mezhdu-snezhnoi-zimoi-v-rf-i-globalnym-potepleniem)"], 
                  "news2": ["В этой статье вы сможете узнать о судьбе Антарктиды в XXI веке (https://news.rambler.ru/tech/56072404-raskryt-naihudshiy-klimaticheskiy-stsenariy-dlya-antarktidy-v-xxi-veke/)"], 
                  "news3": ["В этой статье в сможете узнать о мутациях, которые происходят с белыми медведями из-за глобального потепления (https://news.rambler.ru/tech/55782859-poteplenie-vyzyvaet-mutatsii-v-genome-belyh-medvedey-otkrytie/)"]
                  }
    news_act = random.choice(news_class["news1","news2","news3"])
    bot.reply_to(message, news_act)

@bot.message_handler(commands=['donate'])
def send_bye(message):
    bot.reply_to(message, "ФОНД ПОЖЕРТВОВАНИЙ 'НАЗВАНИЕ ФОНДА':"
    "Т-банк: [ДАННЫЕ КАРТЫ]"
    "Сбербанк: [ДАННЫЕ КАРТЫ]"
    "Альфабанка: [ДАННЫЕ КАРТЫ]")

@bot.message_handler(commands=['temp'])
def send_password(message):
    bot.reply_to(message, "В настоящее время температура отклонилась на 1 C. По предположениям учёных в течение века температура отклониться от нормы ещё на 2 градуса.")
