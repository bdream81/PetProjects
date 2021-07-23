from logging import Manager
import configs

from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
import psycopg2

from text_buttons import TextButtons
from inline_buttons import InlineButtons

conn = psycopg2.connect(
    dbname='my_pizzy', 
    user='postgres', 
    password=123, 
    host='localhost'
)

cursor = conn.cursor()


storage = MemoryStorage()

bot = Bot(configs.TOKEN)
dp = Dispatcher(bot=bot, storage=storage)

tbtns = TextButtons()
ibtns = InlineButtons()
sts = configs.MoiSostoyania()


@dp.message_handler(commands=["start"])
async def listen(message: Message):
    await message.answer(text="Добро пожаловать в телеграм-бот 'Империи Пиццы' 🍕🍕🍕")
    await sts.main_menu.set()
    return await message.answer(text="Выберите категорию:", reply_markup=ibtns.main_btns())
    
@dp.callback_query_handler(state=sts.main_menu)
async def mainmenu(call:CallbackQuery): 
    if call.data == "menu":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())
    
    elif call.data == "shares":
        postgreSQL_select_Query = "SELECT * FROM aksii"
        await sts.shares.set()
        cursor.execute(postgreSQL_select_Query)
        aksii = cursor.fetchall()

        for row in aksii:
            file = open(row[2], "rb") 
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text=row[1], reply_markup=ibtns.shares_btn(row[0]))
        await call.message.answer(text="Вернуться в начало", reply_markup=ibtns.back_btn())

    elif call.data == "vacancies":
        await sts.vacancies.set()
        return await call.message.edit_text(text = "Все вакансии:", reply_markup=ibtns.vacancy_btns())  



    elif call.data == "about_company":
        postgreSQL_select_Query = "SELECT * FROM o_nas"
        await sts.about_company.set()
        cursor.execute(postgreSQL_select_Query)
        o_nas = cursor.fetchall()

        for row in o_nas:
            await call.message.answer(text = row[1])
        await call.message.edit_text(text = "О компании", reply_markup=ibtns.company_btns())
        await call.message.answer(text="Вернуться в начало", reply_markup=ibtns.back_btn())


@dp.callback_query_handler(state=sts.menu)
async def kategoria_menu(call:CallbackQuery):
    if call.data == "breakfasts":
        postgreSQL_select_Query = "SELECT * FROM zavtrak"

        cursor.execute(postgreSQL_select_Query)
        zavtrak = cursor.fetchall()
        await sts.zavtrak.set()
        for row in zavtrak:
            file = open(row[2], "rb")
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text = row[1], reply_markup=ibtns.comman_btn(row[3])) 
        await call.message.answer(text="Вернуться назад в раздел 'Меню'", reply_markup=ibtns.back_btn()) 
                 

    elif call.data == "pizza":
        postgreSQL_select_Query = "SELECT * FROM pizza40"
        cursor.execute(postgreSQL_select_Query)
        pizza40 = cursor.fetchall()
        await sts.pizza40.set()
        for row in pizza40:
            file = open(row[2], "rb") 
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text = row[1], reply_markup=ibtns.comman_btn(row[3])) 
        await call.message.answer(text="Вернуться назад в раздел 'Меню'", reply_markup=ibtns.back_btn())

    elif call.data == "rolls":
        postgreSQL_select_Query = "SELECT * FROM rolly"
        cursor.execute(postgreSQL_select_Query)
        rolly = cursor.fetchall()
        await sts.rolly.set()
        for row in rolly:
            file = open(row[2], "rb") 
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text = row[1], reply_markup=ibtns.comman_btn(row[3])) 
        await call.message.answer(text="Вернуться назад в раздел 'Меню'", reply_markup=ibtns.back_btn())

    elif call.data == "salads":
        postgreSQL_select_Query = "SELECT * FROM salaty"
        cursor.execute(postgreSQL_select_Query)
        salaty = cursor.fetchall()
        await sts.salaty.set()
        for row in salaty:
            file = open(row[2], "rb") 
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text = row[1], reply_markup=ibtns.comman_btn(row[3])) 
        await call.message.answer(text="Вернуться назад в раздел 'Меню'", reply_markup=ibtns.back_btn())

    elif call.data == "snacks":
        postgreSQL_select_Query = "SELECT * FROM zakuski"
        cursor.execute(postgreSQL_select_Query)
        zakuski = cursor.fetchall()
        await sts.zakuski.set()
        for row in zakuski:
            file = open(row[2], "rb") 
            photo = file.read()
            file.close()
            await bot.send_photo(chat_id=call.message.chat.id, photo=photo)
            await call.message.answer(text = row[1], reply_markup=ibtns.comman_btn(row[3])) 
        await call.message.answer(text="Вернуться назад в раздел 'Меню'", reply_markup=ibtns.back_btn())

    elif call.data == "back_main_menu":
        await sts.main_menu.set()
        return await call.message.edit_text(text = "Выберите категорию:", reply_markup=ibtns.main_btns())

@dp.callback_query_handler(state=sts.zavtrak)
async def menuzavtrak(call: CallbackQuery):
    if call.data=="back":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())

@dp.callback_query_handler(state=sts.pizza40)
async def menupizza(call: CallbackQuery):
    if call.data=="back":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())

@dp.callback_query_handler(state=sts.rolly)
async def menurolly(call: CallbackQuery):
    if call.data=="back":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())

@dp.callback_query_handler(state=sts.salaty)
async def menusalaty(call: CallbackQuery):
    if call.data=="back":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())

@dp.callback_query_handler(state=sts.zakuski)
async def menuzakuski(call: CallbackQuery):
    if call.data=="back":
        await sts.menu.set()
        return await call.message.edit_text(text = "Выберите что хотели посмотреть:", reply_markup=ibtns.menu_btns())



@dp.callback_query_handler(state=sts.shares)
async def kategoryshares(call: CallbackQuery):
    if call.data=="back":
        await sts.main_menu.set()
        return await call.message.edit_text(text = "Выберите категорию:", reply_markup=ibtns.main_btns())
    else:
        get_shares_definition_cmd = f"SELECT * FROM aksii WHERE id = {call.data};"

        cursor.execute(get_shares_definition_cmd)
        share_definition = cursor.fetchone()
        
        return await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=share_definition[3], reply_markup=None)    

@dp.callback_query_handler(state=sts.vacancies)
async def kategoria_vacancies(call:CallbackQuery):
    if call.data == "povar":
        postgreSQL_select_Query = "SELECT * FROM vacancy where id = 2;"

        cursor.execute(postgreSQL_select_Query)
        vacancy = cursor.fetchone()
        await sts.povar.set()
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text = vacancy[2], reply_markup=None)
        await call.message.answer(text="Вернуться назад", reply_markup=ibtns.back_btn())

    elif call.data == "waiter":
        postgreSQL_select_Query = "SELECT * FROM vacancy where id = 1;"

        cursor.execute(postgreSQL_select_Query)
        vacancy = cursor.fetchone()
        await sts.waiter.set()
        await bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text = vacancy[2], reply_markup=None)
        await call.message.answer(text="Вернуться назад", reply_markup=ibtns.back_btn())
    
    elif call.data == "back_main_menu":
        await sts.main_menu.set()
        return await call.message.edit_text(text = "Выберите категорию:", reply_markup=ibtns.main_btns())

@dp.callback_query_handler(state=sts.povar)
async def vacancypovar(call: CallbackQuery):
    if call.data=="back":
        await sts.vacancies.set()
        return await call.message.edit_text(text = "Выберите что Вас интересует:", reply_markup=ibtns.vacancy_btns())

@dp.callback_query_handler(state=sts.waiter)
async def vacancywaiter(call: CallbackQuery):
    if call.data=="back":
        await sts.vacancies.set()
        return await call.message.edit_text(text = "Выберите что Вас интересует:", reply_markup=ibtns.vacancy_btns())
            
@dp.callback_query_handler(state=sts.about_company)
async def aboutcompany(call: CallbackQuery):
    if call.data=="back":
        await sts.main_menu.set()
        return await call.message.edit_text(text = "Выберите категорию:", reply_markup=ibtns.main_btns())


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)


















    
    
    



















# @dp.message_handler(commands=["start"])
# async def start(message: Message):
#     return await message.answer(
#         text="Здравствуйте, мы рады Вас видеть!", reply_markup=tbtns.main_menu()
#     )


# @dp.message_handler(content_types=["text"])
# async def operate_main_menu(message: Message):
#     if message.text.lower() == "меню":
#         return await message.answer(text="Здесь будет меню...")
#     elif message.text.lower() == "заказать":
#         return await message.answer(text="Здесь заказываться еда...")
#     else:
#         return await message.answer(text="Простите, я Вас не совсем понял)")


# @dp.message_handler(content_types=["photo"])
# async def accept_image(message: Message):
#     return await message.answer(text="Я успешно получил картинку ✅")


# @dp.message_handler(commands=["shareloc"])
# async def ask_user_to_share_location(message: Message):
#     print(message)
#     return await message.answer(
#         text="Пожалуйста поделитесь геолокцией, чтобы знать куда доставить пиццу)",
#         reply_markup=tbtns.get_location(),
#     )

# @dp.message_handler(content_types=["location"])
# async def coordinates(message: Message):  
#     if message.location:
#         # print("Долгота", message.location.latitude)
#         # print("Широта", message.location.longitude)
#         return await message.answer(text="Ну и отлично, мы знаем вашу локацию")
# if __name__ == "__main__":
#     executor.start_polling(dispatcher=dp)

# # @dp.message_handlers(commands=['sharecontact'])
# # async def ask_user_to_share_contact(message: Message):
# #     print(message)
# #     return await message.answer(
# #         text="Ostav'te svoi kontaktnyi nomer",
# #         reply_markup=phone_btn.get_phone_number(),
# #     )

# @dp.message_handler(commands=["sharephone"])
# async def ask_user_to_share_phone(message: Message):
#     return await message.answer(
#         text="Пожалуйста поделитесь номером телефона, чтобы знать кому звонить",
#         reply_markup=tbtns.get_phone_number(),
#     )


# @dp.message_handler(content_types=["contact"])
# async def contact_information(message: Message):
#     if message.contact:
#         return await message.answer(text="Ну и отлично! Мы знаем куда звонить!")


   


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)






# elif call.data == "shares":
    #     await call.message.answer(text="Здесь будет акции")
    # elif call.data == "vacancies":
    #     await call.message.answer(text="Здесь будет вакансии")
    # elif call.data == "about_company":
    #     await call.message.answer(text="Здесь будет о компании")

