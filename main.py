import telebot
import scrap


API_KEY = '5303349328:AAFI-h0jhu3qx4Aw_JKeEBpcge7vXPe-zMo'
bot = telebot.TeleBot(API_KEY)

valute_list = ['bitcoin', 'ethereum', 'tether', 'bnb', 'dogecoin', 'solana', 'maker']

def hello(message):
    request = message.text.split()
    if request[0] == 'Hello' or request[0] == 'hello':
        return True
    else:
        return False

def get_command(message):
    request = message.text.split()
    if valute_list.count(request[0]) > 0 and len(request) > 1:
        return True
    else:
        return False
def get_list(message):
    request = message.text.split()
    if (request[0] == 'valutes' or request[0] == 'Valutes') and request[1] == 'list':
        return True
    else:
        return False

@bot.message_handler(func=hello)
def greet(message):
    bot.send_message(message.chat.id, "Hello!, please enter the name of crypto valute and how much you want to purchase.")
    bot.send_message(message.chat.id, "In this moment available crypo valutes are bitcoin, ethereum, tether, bnb, dogecoir, solana and maker")

@bot.message_handler(func=get_command)
def count(message):
    request = message.text.split()
    cost = float(scrap.information(request[0]))
    amount = float(request[1]) * cost
    bot.send_message(message.chat.id, f"It will cost {amount} USD")
    bot.send_message(message.chat.id, "The prices update every 60 sencods!")

@bot.message_handler(func=get_list)
def give_list(message):
    bot.send_message(message.chat.id, "bitcoin \nethereum \ntether \nbnb \ndogecoir \nsolana \nmaker")

bot.polling()
