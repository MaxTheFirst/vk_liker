from dispatcher import dp
from aiogram import executor
import handlers

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
