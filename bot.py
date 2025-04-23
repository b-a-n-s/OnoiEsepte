from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command 
import asyncio
import os
API_TOKEN = os.getenv("7718390615:AAERDda35Ktx4gwKUbnCImv3RNwFlz0WWj4")



bot = Bot(token=API_TOKEN)
dp = Dispatcher()

ort_total = 0
math_callbacks = [f'm{i}' for i in range(1, 61)]
kyr_callbacks = [f'k{i}' for i in range(1, 31)] 
oku_callbacks = [f'o{i}' for i in range(1, 31)]
gram_callbacks = [f'g{i}' for i in range(1, 31)]  # Changed to 'k' prefix

# Math section inline keyboard (60 questions)
def q60():
    maz = []
    row_size = 4  
    row = [] 
    for i in range(1, 61):
        button = InlineKeyboardButton(text=str(i), callback_data=f'm{i}')
        row.append(button)
        if len(row) == row_size:
            maz.append(row)
            row = [] 
    if row:
        maz.append(row)
    return maz
def math_inline():
    maz = q60()
    return InlineKeyboardMarkup(inline_keyboard=maz)

# Kyrgyzstan section inline keyboard (30 questions)
def q30():
    kyr = []
    row_size = 4  
    row = [] 
    for i in range(1, 31):
        button = InlineKeyboardButton(text=str(i), callback_data=f'k{i}')  # Changed to 'k' prefix
        row.append(button)
        if len(row) == row_size:
            kyr.append(row)
            row = [] 
    if row:
        kyr.append(row)
    return kyr
def kyr_inline():
    kyr = q30()
    return InlineKeyboardMarkup(inline_keyboard=kyr)

def qoku():
    oku = []
    row_size = 4  
    row = [] 
    for i in range(1, 31):
        button = InlineKeyboardButton(text=str(i), callback_data=f'o{i}')  # Changed to 'k' prefix
        row.append(button)
        if len(row) == row_size:
            oku.append(row)
            row = [] 
    if row:
        oku.append(row)
    return oku
def oku_inline():
    oku = qoku()
    return InlineKeyboardMarkup(inline_keyboard=oku)

def qgram():
    gram = []
    row_size = 4  
    row = [] 
    for i in range(1, 31):
        button = InlineKeyboardButton(text=str(i), callback_data=f'g{i}')
        row.append(button)
        if len(row) == row_size:
            gram.append(row)
            row = [] 
    if row:
        gram.append(row)
    return gram
def gram_inline(): 
    gram = qgram()
    return InlineKeyboardMarkup(inline_keyboard=gram)

@dp.message(Command('start'))
async def start_command(message: types.Message):
    global ort_total
    ort_total = 0
    await message.answer('🧮 *Математика бөлүмү* \n\nЭсептегиле: канча суроого туура жооп бердиңиз? 😊', 
                         reply_markup=math_inline(), parse_mode='Markdown')

@dp.callback_query(lambda c: c.data.startswith('m'))
async def math_callback(callback: types.CallbackQuery):
    global ort_total
    correct_answers = int(callback.data[1:])
    points = correct_answers * 1.12
    ort_total += points
    
    await callback.message.answer(
        f"✅ *Математика*: {correct_answers} туура → *{points} балл* 🎉\n\n"
        f"🌟 Керемет! Эми *Окшоштуктар* бөлүмүнө өтөлү:",
        reply_markup=kyr_inline(),
        parse_mode='Markdown'
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith('k'))
async def kyr_callback(callback: types.CallbackQuery):
    global ort_total
    correct_answers = int(callback.data[1:])
    points = correct_answers * 2.1
    ort_total += points
    
    await callback.message.answer(
        f"✅ *Окшоштуктар*: {correct_answers} туура → *{points} балл* 🎊\n\n"
        f"✨ Супер! Эми *Окуп түшүнүү* бөлүмүн баштайлы:",
        reply_markup=oku_inline(),
        parse_mode='Markdown'
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith('o'))
async def oku_callback(callback: types.CallbackQuery):
    global ort_total
    correct_answers = int(callback.data[1:])
    points = correct_answers * 1.96
    ort_total += points
    
    await callback.message.answer(
        f"✅ *Окуп түшүнүү*: {correct_answers} туура → *{points} балл* 💫\n\n"
        f"📚 Акыркы бөлүм - *Грамматика*:",
        reply_markup=gram_inline(),
        parse_mode='Markdown'
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data.startswith('g'))
async def gram_callback(callback: types.CallbackQuery):
    global ort_total
    correct_answer = int(callback.data[1:])
    points = correct_answer*1.9
    ort_total += points
    
    # Create a celebratory message based on score
    if ort_total >= 180:
        result_emoji = "🏆🔥"
        comment = "Сиздин жыйынтыгыңыз эң жогору деңгээлде! Так улантыңыз!"
    elif ort_total >= 120:
        result_emoji = "🎯✨"
        comment = "Жакшы натыйжа! Дагы аракет кылып, жогорулай бериңииз!"
    else:
        result_emoji = "📝💪"
        comment = "Башталыш үчүн жакшы! Андан ары да күчөйө бериңиз!"
    
    await callback.message.answer(
        f"✅ *Грамматика*: {correct_answer} туура → *{points} балл* 📝\n\n"
        f"{result_emoji} *Сиздин жалпы жыйынтыгыңыз: {round(ort_total, 2)} балл!*\n"
        f"{comment}",
        parse_mode='Markdown'
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())