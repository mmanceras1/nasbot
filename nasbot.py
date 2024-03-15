#!/home/miguel/venv_miguel/bin/python3

import json
import telebot
import requests

def getToken():
    path = "/home/miguel/venv_miguel/cfg/token.json"
    try:
        with open(path) as file:
            doc = json.load(file)
            return doc['token']
    except:
         print("No se ha encontrado el fichero token.json")
         return False

def recieve_file(message, file_id):
    file_info = bot.get_file(file_id)
    print(file_id)
    
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(getToken(), file_info.file_path))
    open("/fotos/import/{}_test.jpg".format(file_id), "wb").write(file.content)
    bot.reply_to(message, "Escrito archivo: /fotos/import/" + str(file_id) + "_test.jpg" )
    

if (getToken() != False):
    bot = telebot.TeleBot(getToken())
else:
    print("No se ha podido instanciar el bot")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
     
@bot.message_handler(commands=['/directory', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
     
@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
	recieve_file(message,message.photo[0].file_id)