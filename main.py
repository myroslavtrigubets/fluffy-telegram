import config
import telebot
import os
import datetime

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def commands(message): 
	if message.chat.id in config.admins:
		if message.text == "/start": 
			bot.send_message(message.chat.id, "message.text")

		elif "uptime" in message.text:   
			f = os.popen('uptime').read()
			bot.send_message(message.chat.id, f)

		elif "/ssh" in message.text: 
			ssh = message.text.replace("/ssh", "") 
			f = os.popen(ssh).read()
			bot.send_message(message.chat.id, f)

		elif "/photo" in message.text: 

			bot.send_message(message.chat.id, "Send Photo")

			bot.send_photo(message.chat.id, open('/root/fluffy-telegram/test.png', 'rb'))

		else:
			bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)