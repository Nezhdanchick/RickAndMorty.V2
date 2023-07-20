from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


common_router = Router()


@common_router.message(Command('start'))
async def handle_start(message: Message):
    await message.answer(
        "Привет. Введи id персонажа, по которому хочешь узнать информацию.")

