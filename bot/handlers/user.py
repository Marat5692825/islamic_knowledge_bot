from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards.user import main_menu_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    text = (
        "Ассаляму алейкум!\n\n"
        "Добро пожаловать в Islamic Knowledge Bot.\n"
        "Выберите раздел в меню ниже."
    )
    await message.answer(text, reply_markup=main_menu_kb())


@router.message(Command("help"))
@router.message(F.text == "ℹ️ О боте / Помощь")
async def cmd_help(message: Message) -> None:
    text = (
        "Помощь:\n"
        "• /start — главное меню\n"
        "• /help — помощь\n\n"
        "Навигация будет внутри разделов: ⬅️ Назад, 🏠 Домой."
    )
    await message.answer(text, reply_markup=main_menu_kb())
