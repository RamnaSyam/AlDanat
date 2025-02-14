import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram import F
from keep_alive import keep_alive  # Keeps Replit running

# Securely get token from Replit Secrets
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in Replit Secrets!")

# Create Bot and Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- Creating Buttons ---
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Admission Details")],
        [KeyboardButton(text="📝 Exam Schedule")],
        [KeyboardButton(text="📅 School Events")],
        [KeyboardButton(text="ℹ️ Contact Us")]
    ],
    resize_keyboard=True
)

# Inline buttons with links
inline_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Admission Info", url="https://your-school-website.com/admissions")],
    [InlineKeyboardButton(text="Exam Schedule", url="https://your-school-website.com/exams")],
    [InlineKeyboardButton(text="School Events", url="https://your-school-website.com/events")],
    [InlineKeyboardButton(text="Contact Us", url="https://your-school-website.com/contact")]
])

# --- Handling Start Command ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Welcome to the School Support Bot! 🎓\nPlease choose an option below:", reply_markup=main_menu)

# --- Handling Button Clicks ---
@dp.message(F.text.in_(["📚 Admission Details", "📝 Exam Schedule", "📅 School Events", "ℹ️ Contact Us"]))
async def send_info(message: types.Message):
    await message.answer("Click the relevant link below for details:", reply_markup=inline_links)

# Keep bot alive
keep_alive()

# --- Main Function ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
