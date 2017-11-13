import os
import config
import datetime
import requests
import telebot
import time

bot = telebot.TeleBot(config.token)
def webcamera():
	f = os.popen("fswebcam -r 640x480 --jpeg 85 -D 1 /home/pi/Project/fluffy-telegram/cam.jpg").read()
	try:file = open('/home/pi/Project/fluffy-telegram/cam.jpg')
	except IOError as e:
		webcamera()
	else:
		with file:return 0

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

		elif message.text == "/temp" : 
			f = os.popen("vcgencmd measure_temp").read()
			bot.send_message(message.chat.id, f)

		elif "/photo" in message.text: 
			web = webcamera()
			bot.send_photo(message.chat.id, open('/home/pi/Project/fluffy-telegram/cam.jpg', 'rb'))
			os.remove('/home/pi/Project/fluffy-telegram/cam.jpg')
		else:
			bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)