import re
import conf
import random
import telebot

def get_sentences(path, regex=".*?[.!?]\s"):
    with open(path, "r", encoding="utf-8") as f:
        sents = re.findall(regex, f.read(), re.DOTALL)
    return sents

def random_quote(sents):
    i = random.randint(0, len(sents)-1)
    return sents[i]

bot = telebot.TeleBot(conf.TOKEN) 
sents = get_sentences("onegin.txt")

@bot.message_handler(commands=['send'])
def send_quote(message):
    bot.send_message(message.chat.id, random_quote(sents))
    
@bot.message_handler(func=lambda m: True) 
def query_quote(message):
    query = message.text
    res = [sent for sent in sents if query.lower() in sent.lower()]
    if len(res) != 0:
        bot.send_message(message.chat.id, random_quote(res))
    else:
        bot.send_message(message.chat.id, "Об этом Пушкин не писал!")

if __name__ == '__main__':
    bot.polling(none_stop=True)