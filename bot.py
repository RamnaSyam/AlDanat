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
        [KeyboardButton(text="📚 School Policies")],
        [KeyboardButton(text="📝 Exam Schedule")],
        [KeyboardButton(text="📅 School Timings")],
        [KeyboardButton(text="ℹ️ Weekly plans")],
        [KeyboardButton(text="📚 Link for Medical Excuses")],
        [KeyboardButton(text="📚 Technical support contacts")],
    ],
    resize_keyboard=True
)

# Inline buttons with links
inline_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="School Policies", url="https://your-school-website.com/policies")],
    [InlineKeyboardButton(text="Exam Schedule", url="https://your-school-website.com/exams")],
    [InlineKeyboardButton(text="School Timings", url="https://your-school-website.com/timings")],
    [InlineKeyboardButton(text="Weekly Plans", url="https://your-school-website.com/weekly plan")],
     [InlineKeyboardButton(text="Link for Medical Excuses", url="https://your-school-website.com/medicalexcuses")]
    
    
])

# --- Handling Start Command ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Welcome to Al Danat School Parent's Support Bot! 🎓\nPlease choose an option below:", reply_markup=main_menu)

# --- Handling Button Clicks ---
@dp.message(F.text.in_(["📚 School Policies", "📝 Exam Schedule", "📅 School Timings", "ℹ️ Weekly plans", "📚 Link for Medical Excuses", "📚 Technical support contacts"]))
async def send_info(message: types.Message):
    await message.answer("Click the relevant link below for details:", reply_markup=inline_links)

# Keep bot alive
keep_alive()

# --- Main Function ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
