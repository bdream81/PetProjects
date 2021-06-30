from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN = "1892186813:AAFWB7epkwTaFCGGOrTnon81W0DRaZPSdSg"

class MoiSostoyania(StatesGroup):
    main_menu = State()
    menu = State()
    shares  = State()
    vacancies = State()
    about_company = State()