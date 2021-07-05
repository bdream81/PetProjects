import os
import random
import time

questions_main = {
"Язык программирования": "питон",
"Один из принципов ООП": "инкапсуляция",
"Электронная схема, управляющая внешним устройством": "контроллер",
"Разъемы подключения внешних устройств": "интерфейс"
}


print("Добро пожаловать в игру Hangman!")
def timer():
    for endtime in range(0, 2):
        time.sleep(1)
timer()
print()
print("Правила: Я читаю Вам описание слова, а Вы пытаетесь отгадать по описанию")
timer()
print()
print("Игра начнется через...")

def timer():
    for endtime in range(0, 3):
        print(3 - endtime)
        time.sleep(1)  
timer()
print("Поехали!")

question_main = random.choice(list(questions_main.keys()))
 

answer_main = questions_main[question_main]
star_answer = []
for i in range(len(answer_main)):
    star_answer.append("*")

print()
print("Вопрос:", question_main)
print()
print(*star_answer)
print()

def poryadok(gamer, gamers):
    if len(gamers) <= gamer:
         return False
    else:
         return True

gamers = ['Akjol', 'Sanjar', 'Kyial', 'Oljas', 'Aidana', 'Islam']
gameOwer = False
gamer = 0

while not gameOwer:
    print("Букву пытается отгадать - " , gamers[gamer])
    print()
    while True:
        user = input("Угадать букву -1 / Сказать слово сразу - 2: ")
        
        if user == '1': 
            is_valid = False
            while '*' in star_answer:
                
                bukva = input('Введите букву').upper()
                if len(bukva)==1 and bukva.isalpha():
                    for i in range(len(answer_main)):
                        if bukva==answer_main[i]:
                            star_answer[i] = bukva
                            is_valid = True
                    print(*star_answer)
                    if not '*' in star_answer:
                        print('ВЫ ВЫИГРАЛИ')
                        break
                    if not is_valid:
                        print('Ход переходит к другому')
                        if poryadok(gamer+1, gamers):
                            gamer = gamer+1
                        else:
                            gamer = 0
            else:
                print("Игра переходит к следующему игроку")           
        if user == '2':
            slovo1 = input("Скажите слово: ").upper()
            if slovo1 == answer_main:
                print("Угадали! Поздравляю, Вы победитель!")
                break
            else:
                print("Неправильно... К сожалению, Вы выбываете из игры")
                break
        
        if user != 1 or user != 2:
            print("У Вас только две опции: 1 и 2!")
        
        
    
    gamer += 1
