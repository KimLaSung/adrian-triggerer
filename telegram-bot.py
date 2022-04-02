from telegram.ext import Updater, CommandHandler
from engine import get_random_quote

# Your bot token (from BotFather)
token = "5282694697:AAFICpNo6zAiDM3WeowGAlocLkgLu80OFAE"

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=("Ae %s. Scrivi /cane per prendere per il culo Adrian." %
														  update.message.from_user.name))

def quote(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,
					text=get_random_quote())

def main():
	updater = Updater(token);
	dp = updater.dispatcher

	# Define all the commands that the bot will receive
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("cane", quote))

	# Start the bot
	updater.start_polling()
	print("================================")
	print("========= Bot Running ==========")
	print("================================")

	updater.idle()


if __name__ == "__main__":
	main()
