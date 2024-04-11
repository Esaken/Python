import telepot
token = '6955735455:AAFarTCA4qKJU7ndh9xOF6htRQPM91v3hq8'
TelegramBot = telepot.Bot(token)
#print (TelegramBot.getMe())

print (TelegramBot.getUpdates(13890781+1))


