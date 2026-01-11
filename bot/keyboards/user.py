from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Книги"), KeyboardButton(text="📖 Суры")],
            [KeyboardButton(text="🎵 Нашиды"), KeyboardButton(text="🕌 Обучение намазу")],
            [KeyboardButton(text="ℹ️ О боте / Помощь")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите раздел…",
    )
