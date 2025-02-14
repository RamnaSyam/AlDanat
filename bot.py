import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from keep_alive import keep_alive  # Keeps Replit running

TOKEN = os.getenv("BOT_TOKEN")  # Securely get token from Replit Secrets

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# --- Creating Buttons ---
# Main menu with buttons
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📚 Admission Details"),
    KeyboardButton("📝 Exam Schedule"),
    KeyboardButton("📅 School Events"),
    KeyboardButton("ℹ️ Contact Us")
)

# Inline buttons with links
inline_links = InlineKeyboardMarkup()
inline_links.add(
    InlineKeyboardButton("Admission Info", url="https://your-school-website.com/admissions"),
    InlineKeyboardButton("Exam Schedule", url="https://your-school-website.com/exams"),
    InlineKeyboardButton("School Events", url="https://your-school-website.com/events"),
    InlineKeyboardButton("Contact Us", url="https://your-school-website.com/contact")
)

# --- Handling Start Command ---
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the School Support Bot! 🎓\nPlease choose an option below:", reply_markup=main_menu)

# --- Handling Button Clicks ---
@dp.message_handler(lambda message: message.text in ["📚 Admission Details", "📝 Exam Schedule", "📅 School Events", "ℹ️ Contact Us"])
async def send_info(message: types.Message):
    await message.reply("Click the relevant link below for details:", reply_markup=inline_links)

# Keep bot alive
keep_alive()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
