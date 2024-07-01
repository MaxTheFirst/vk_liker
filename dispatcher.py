import config
from vkclients import VkClients
from aiogram import Bot, Dispatcher

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)

clients = VkClients(config.PROXIES_FILE, config.TOKENS_FILE)
