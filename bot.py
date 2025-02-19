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
main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📚 School Policies_سياسات المدرسة")],
    [KeyboardButton(text="📝 Assessments_الامتحانات")],
    [KeyboardButton(text="📅 School Timings_مواعيد المدرسة,")],
    [KeyboardButton(text="ℹ️ Al Danat News_أخبار الدانات")],
    [KeyboardButton(text="📚 Link for Medical Excusesرابط للأعذار الطبية")],
    [KeyboardButton(text="📚 Important contact details_تفاصيل الاتصال الهامة")],
    [KeyboardButton(text="📝 Announcements and circulars_الإعلانات والتعاميم")],
    [KeyboardButton(text="📝 Canteen Menu_قائمة المقصف المدرسي")],
],
                                resize_keyboard=True)

# Inline buttons with links
inline_links = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="School Policies_سياسات المدرسة",
                             url="https://bit.ly/4i45KUG")
    ],
    [
        InlineKeyboardButton(text="Assessments_الامتحانات",
                             url="https://bit.ly/3D5vAJa")
    ],
    [
        InlineKeyboardButton(text="School Timings_مواعيد المدرسة",
                             url="https://bit.ly/3X6nqXO")
    ],
    [
        InlineKeyboardButton(text="  Al Danat News_أخبار _أخبار",
                             url="https://bit.ly/3QkZZGC")
    ],
    [
        InlineKeyboardButton(
            text="Link for Medical Excuses الطبية للأعذار رابط ",
            url="https://forms.office.com/r/77cppezTHq")
    ],
    [
        InlineKeyboardButton(
            text="Important contact details_تفاصيل الاتصال الهامة ",
            url="https://bit.ly/41nVFNb")
    ],
    [
        InlineKeyboardButton(
            text="Announcements and circulars والتعاميم _الإعلانات", url="")
    ],
    [
        InlineKeyboardButton(text="Canteen Menu_قائمة المقصف المدرسي ",
                             url="https://bit.ly/3X845Wj")
    ]
])


# --- Handling Start Command ---
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "Welcome to Al Danat School Parent's Support Bot! 🎓\nPlease choose an option below:",
        reply_markup=main_menu)


# --- Handling Button Clicks ---
@dp.message(
    F.text.in_([
        "📚 School Policies", "📝 Exam Schedule", "📅 School Timings",
        "ℹ️ Weekly plans", "📚 Link for Medical Excuses",
        "📚 Technical support contacts"
    ]))
async def send_info(message: types.Message):
    await message.answer("Click the relevant link below for details:",
                         reply_markup=inline_links)


# Keep bot alive
keep_alive()


# --- Main Function ---
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
