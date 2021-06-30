from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineButtons:
    def __init__(self) -> None:
        pass

    def pizza_btns(self):
        markup = InlineKeyboardMarkup()

        menu = InlineKeyboardButton(text="Меню", callback_data="menu")
        shares = InlineKeyboardButton(text="Акции", callback_data="shares")
        vacancies = InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
        about_company = InlineKeyboardButton(text="О нас", callback_data="about_company")


        markup.add(menu, shares)
        markup.add(vacancies, about_company )
       
        return markup

    def menu_btns(self):
        markup = InlineKeyboardMarkup()

        breakfasts = InlineKeyboardButton(text='Завтраки', callback_data='breakfasts') # call_data инф о кнопке
        pizza = InlineKeyboardButton(text='Пиццы', callback_data='pizza')
        rolls = InlineKeyboardButton(text='Роллы', callback_data='rolls')
        salads = InlineKeyboardButton(text='Салаты', callback_data='salads')
        snacks = InlineKeyboardButton(text='Закуски', callback_data='snacks')
        
        markup.add(breakfasts, pizza)
        markup.add(rolls, salads)
        return markup       

    def shares_btn(self, id_):
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton(text='Подробнее', callback_data=id_)
        markup.add(btn)
        return markup

    def vacancy_btns(self):
        markup = InlineKeyboardMarkup()
        povar = InlineKeyboardButton(text='Повар', callback_data='povar')
        waiter = InlineKeyboardButton(text='Официант', callback_data='waiter')        
        markup.add(povar, waiter)
        return markup         

    def comman_btn(self, name): # печатает любую кнопку
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton(text=name, callback_data=str(name))        
        markup.add(btn)  
        return markup     

    def back_btn(self):
        markup = InlineKeyboardMarkup()
        back = InlineKeyboardButton(text='Вернуться назад', callback_data="back")
        markup.add(back)
        return markup