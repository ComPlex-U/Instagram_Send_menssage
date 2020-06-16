import instabot
bot = instabot.Bot()
bot.login(username='user', password='pass')
bot.send_message(text="hello world", user_ids='@id')
bot.logout()