from aiogram import Router, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
import rickandmorty
from rickandmorty.character_client import Characters

characters_router = Router()


#
#  = ramapi.Character.get(100)
#
# print(character['name'])

@characters_router.message(F.text)
async def get_characters(message: Message):
    if message.text.isdigit() and 1 <= int(message.text) <= 671:
        characters_api = Characters()
        character = characters_api.getSingle(message.text)
        picture = character["image"]
        await message.answer_photo(picture, caption=f'Name: {character["name"]}\nStatus: {character["status"]}\nSpecies: {character["species"]}\nGender: {character["gender"]}\nLocation: {character["location"]["name"]}\n Episode: {character["episode"]}')
