from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN = ""

class MoiSostoyania(StatesGroup):
    main_menu = State()
    menu = State()
    zavtrak = State()
    pizza40 = State()
    rolly = State()
    salaty= State()
    zakuski = State()
    shares  = State()
    vacancies = State()
    about_company = State()
    povar = State()
    waiter=State()
    