# import os
# import random
# import time

# questions_main = {
# "Язык программирования": "питон",
# "Один из принципов ООП": "инкапсуляция",
# "Электронная схема, управляющая внешним устройством": "контроллер",
# "Разъемы подключения внешних устройств": "интерфейс"
# }


# print("Добро пожаловать в игру Hangman!")
# def timer():
#     for endtime in range(0, 2):
#         time.sleep(1)
# timer()
# print()
# print("Правила: Я читаю Вам описание слова, а Вы пытаетесь отгадать по описанию")
# timer()
# print()
# print("Игра начнется через...")

# def timer():
#     for endtime in range(0, 3):
#         print(3 - endtime)
#         time.sleep(1)  
# timer()
# print("Поехали!")

# question_main = random.choice(list(questions_main.keys()))
 

# answer_main = questions_main[question_main]
# star_answer = []
# for i in range(len(answer_main)):
#     star_answer.append("*")

# print()
# print("Вопрос:", question_main)
# print()
# print(*star_answer)
# print()

# def poryadok(gamer, gamers):
#     if len(gamers) <= gamer:
#          return False
#     else:
#          return True

# gamers = ['Akjol', 'Sanjar', 'Kyial', 'Oljas', 'Aidana', 'Islam']
# gameOwer = False
# gamer = 0

# while not gameOwer:
#     print("Букву пытается отгадать - " , gamers[gamer])
#     print()
#     while True:
#         user = input("Угадать букву -1 / Сказать слово сразу - 2: ")
        
#         if user == '1': 
#             is_valid = False
#             while '*' in star_answer:
                
#                 bukva = input('Введите букву').upper()
#                 if len(bukva)==1 and bukva.isalpha():
#                     for i in range(len(answer_main)):
#                         if bukva==answer_main[i]:
#                             star_answer[i] = bukva
#                             is_valid = True
#                     print(*star_answer)
#                     if not '*' in star_answer:
#                         print('ВЫ ВЫИГРАЛИ')
#                         break
#                     if not is_valid:
#                         print('Ход переходит к другому')
#                         if poryadok(gamer+1, gamers):
#                             gamer = gamer+1
#                         else:
#                             gamer = 0
#             else:
#                 print("Игра переходит к следующему игроку")           
#         if user == '2':
#             slovo1 = input("Скажите слово: ").upper()
#             if slovo1 == answer_main:
#                 print("Угадали! Поздравляю, Вы победитель!")
#                 break
#             else:
#                 print("Неправильно... К сожалению, Вы выбываете из игры")
#                 break
        
#         if user != 1 or user != 2:
#             print("У Вас только две опции: 1 и 2!")
        
        
    
#     gamer += 1





import os
import random
import time

class Pole_Chudes:
    gamers = ['Akjol', 'Sanjar', 'Kyial', 'Oljas', 'Aidana', 'Islam']
    gamers_amount = len(gamers)

    questions_answers = {
        "Неизменяемый 'список'": "КОРТЕЖ", 
        "Высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода": "ПИТОН",
        "Описывает местоположение и обращение к элементу списка, заключенному в квадратные скобки": "ИНДЕКС",
        "Функция range создает .... чисел ": "ДИАПАЗОН",
        "clear()- ... элементов списка ": "УДАЛЕНИЕ",
        "Данные, хранящиеся в прямоугольной таблице": "МАТРИЦА",
        }

    questions = random.choice(list(questions_answers.keys()))
    answers = list(questions_answers.get(questions))
    

    template = [] # шаблон
    for _ in range(len(answers)):
        template.append('*')

    def timer():
        print()
        for endtime in range(0, 3):
            print(f"{endtime} . . .")
            time.sleep(1)
    

    def all_in(self, current_user, word): # current -текущий
        if word == self.answers:
            print("Угадали! Поздравляю!")
            print("Победитель этой игры : {current_user}")
            return exit()
        else:
            user_index = self.gamers.index(current_user)
            self.gamers[user_index] = "" 
            print(f'Вы не угадали... {current_user} к сожалению, Вы выбываете из игры')
            return 0

    def main(self): # main - основной
        print("Добро пожаловать в игру Pole_Chudes\n")
        time.sleep(3)
        print("Правила: Я читаю вам описание слова, а вы пытаетесь его отгадать по описанию\n")
        
        time.sleep(3)
        print("Игра начнётся через...")
        time.sleep(1)

        # self.timer()
        user_count = 0
    
        while any(self.gamers):
            os.system("clear") #

            current_user = self.gamers[user_count % self.gamers_amount] # amount - количество
            if not current_user:#
                continue
            
            print()
            print()
            print(self.questions)
            print()
            print("".join(self.template))
            print()

            try:
                print(f"Букву пытается отгадать - {current_user}\n")
                choice = int(input("Угадать букву - 1 | Сказать слово сразу - 2:   "))
            except:
                print("Вы можете вводить только цифры!")
                # time.sleep(2)
                continue
            if choice == 1:
                letter = input("Вводите букву: ").upper()

                while not letter.isalpha or len(letter) > 1: #
                    print("Вводите только буквы!".upper())
                    # time.sleep(2)
                    os.system("clear")
                    letter = input("Вводите букву: ").upper()

                while letter in self.answers:
                    # self.timer() #
                    print("Отлично! Есть такая буква!")
                    # time.sleep(1.5)

                    for l in self.answers:
                        if l == letter:
                            indx = self.answers.index(letter)
                            self.answers[indx] = ""
                            self.template[indx] = letter
                        
                    if "".join(self.template) == self.answers:
                        print("Угадали! Поздравляю!")
                        print("Победитель этой игры : {current_user}")
                        exit()
                    
                    print()
                    print(self.questions)
                    print()
                    print("".join(self.template))
                    print()

                    # time.sleep(2)

                    while True:
                        try:
                            choice = int(input("Продолжить называть по букве - 1 | Сказать слово сразу - 2:   "))

                            if 0 < choice < 3:
                                break
                            else:
                                print("\nУ вас только 2 опции: 1 или 2!")
                                # time.sleep(2)
                                continue
                        except:
                            print("\nВы можете вводить только цифры!")
                            # time.sleep(2)
                            continue

                    if choice == 1:
                        print(f"\n{current_user} снова ваш ход!")
                        letter = input("Вводите букву:   ").upper()

                        while not letter.isalpha() or len(letter) > 1:
                            print("\nВводить можно только буквы!".upper())
                            letter = input("Вводите букву:   ").upper()
                    else:
                        word = input("Назовите слово полностью:   ").upper()
                        # self.timer()
                        self.all_in(current_user, word)
                        break

                # self.timer()
                print("Простите, такой буквы нет. . .")

            elif choice == 2:
                word = input("Назовите слово полностью:   ").upper()
                # self.timer()
                self.all_in(current_user, word)

            else:
                print("У вас только 2 опции: 1 или 2!")
                # time.sleep(1)
                continue   
                
            user_count += 1

        print("Все участники выбыли из игры. . .")

pole_chudes = Pole_Chudes()

pole_chudes.main() 


# import os
# import time
# import random


# class HangmanGame:
#     GAMERS = ["Акжол", "Санжар", "Кыял", "Олжас", "Айдана", "Ислам"]
#     GAMERS_AMOUNT = len(GAMERS)

#     WORDS = {
#         "ИНТЕРПРЕТАТОР": "Программа которая исполняет Python код?",
#         "ПАРАДИГМА": "Как называется стиль программирования?",
#         "ОБЪЕКТ": "Что мы получаем после инициализации класса?",
#     }

#     HANGMAN_WORD = random.choice(tuple(WORDS.keys()))
#     HANGMAN_WORD_DEFINITION = WORDS.get(HANGMAN_WORD)
#     HANGMAN_WORD_LIST = list(HANGMAN_WORD)

#     TEMPLATE = ["_ " for _ in range(len(HANGMAN_WORD))]

#     def timer(self):
#         print()
#         for i in range(3, 0, -1):
#             print(f"{i} . . .")
#             time.sleep(1.5)

#     def all_in(self, current_user, word):
#         if word == self.HANGMAN_WORD:
#             print("Ура! Вы угадали!")
#             print(f"Победитель этой игры: {current_user}")
#             return exit()

#         else:
#             user_ndx = self.GAMERS.index(current_user)
#             self.GAMERS[user_ndx] = ""
#             print(f"Простите {current_user} вы не угадали, Вы выбываете из игры. . .")
#             return 0

#     def main(self):
#         print("Добро пожаловать в игру Hangman!\n")
#         time.sleep(3)
#         print(
#             "Правила: Я читаю вам описание слова, а вы пытаетесь его отгадать по описанию\n"
#         )
#         time.sleep(3)
#         print("Игра начнётся через...")
#         time.sleep(1)

#         self.timer()
#         user_count = 0

#         while any(self.GAMERS):
#             os.system("clear")

#             current_user = self.GAMERS[user_count % self.GAMERS_AMOUNT]
#             if not current_user:
#                 continue

#             print()
#             print()
#             print(self.HANGMAN_WORD_DEFINITION)
#             print()
#             print("".join(self.TEMPLATE))
#             print()

#             try:
#                 print(f"Букву пытается отгадать - {current_user}\n")
#                 choice = int(input("Угадать букву - 1 | Сказать слово сразу - 2:   "))
#             except:
#                 print("Вы можете вводить только цифры!")
#                 time.sleep(2.5)
#                 continue

#             if choice == 1:
#                 letter = input("Ну же! Что же это за буква:   ").upper()

#                 while not letter.isalpha() or len(letter) > 1:
#                     print("\nВводить можно только буквы!".upper())
#                     time.sleep(2.5)
#                     os.system("clear")
#                     letter = input("Ну же! Что же это за буква:   ").upper()

#                 while letter in self.HANGMAN_WORD_LIST:
#                     self.timer()
#                     print("\nОтлично! Вы угадали!\n")
#                     time.sleep(1.5)

#                     for l in self.HANGMAN_WORD_LIST:
#                         if l == letter:
#                             ndx = self.HANGMAN_WORD_LIST.index(letter)
#                             self.HANGMAN_WORD_LIST[ndx] = ""
#                             self.TEMPLATE[ndx] = letter

#                     if "".join(self.TEMPLATE) == self.HANGMAN_WORD:
#                         print("Ура! Вы угадали!")
#                         print(f"Победитель этой игры: {current_user}")
#                         exit()

#                     print()
#                     print(self.HANGMAN_WORD_DEFINITION)
#                     print()
#                     print("".join(self.TEMPLATE))
#                     print()

#                     time.sleep(2)

#                     while True:
#                         try:
#                             choice = int(
#                                 input(
#                                     "Продолжить называть по букве - 1 | Сказать слово сразу - 2:   "
#                                 )
#                             )
#                             if 0 < choice < 3:
#                                 break
#                             else:
#                                 print("\nУ вас только 2 опции: 1 или 2!")
#                                 time.sleep(2.5)
#                                 continue
#                         except:
#                             print("\nВы можете вводить только цифры!")
#                             time.sleep(2.5)
#                             continue

#                     if choice == 1:
#                         print(f"\n{current_user} снова ваш ход!")
#                         letter = input("Ну же! Что же это за буква:   ").upper()

#                         while not letter.isalpha() or len(letter) > 1:
#                             print("\nВводить можно только буквы!".upper())
#                             letter = input("Ну же! Что же это за буква:   ").upper()
#                     else:
#                         word = input("Ну же! Назовите слово полностью:   ").upper()
#                         self.timer()
#                         self.all_in(current_user, word)
#                         break

#                 self.timer()
#                 print("Простите, такой буквы нет. . .")

#             elif choice == 2:
#                 word = input("Ну же! Назовите слово полностью:   ").upper()
#                 self.timer()
#                 self.all_in(current_user, word)

#             else:
#                 print("У вас только 2 опции: 1 или 2!")
#                 time.sleep(2.5)
#                 continue

#             user_count += 1

#         print("Все участники выбыли из игры. . .")


# hang_game = HangmanGame()

# hang_game.main()