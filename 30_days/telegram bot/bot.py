import telepot
token = 'Tafuta yako'
TelegramBot = telepot.Bot(token)
#print (TelegramBot.getMe())

print (TelegramBot.getUpdates(13890781+1))


