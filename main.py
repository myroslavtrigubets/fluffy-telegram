import config
import telebot
import os

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
	if message.text == "/start": 
		bot.send_message(message.chat.id, "message.text")

	elif "uptime" in message.text:   
		f = os.popen('uptime').read()
		bot.send_message(message.chat.id, f)

	elif "/ssh" in message.text: 
		ssh = message.text.replace("/ssh", "") 
		f = os.popen(ssh).read()
		bot.send_message(message.chat.id, f)

	else:
		bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)

