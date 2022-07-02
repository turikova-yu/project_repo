i = input("Хотите сыграть в интересную игру? Y/N ")
while i == 'Y' or i =='y':
    import random

    print("***Игра 'Угадай число'***")
    print()
    print("Выберите уровень сложности: ")
    print()
    print("0 - Легкий")
    print("1 - Средний")
    print("0 - Сложный")
    difficult = int(input("Введите уровень сложности: "))

    comp_number = -1
    hearts = -1

    if difficult == 0:
        comp_number = random.randint(1, 10)
        hearts = 3
    if difficult == 1:
        comp_number = random.randint(1, 100)
        hearts = 5
    if difficult == 2:
        comp_number = random.randint(1, 1000)
        hearts = 8
    print()
    print('=========================')
    print()
    while hearts > 0:
        player_number = int(input("Введите число: "))
        hearts -= 1
        if comp_number == player_number:
            print(f"Ура! Вы угадали число за {3 - hearts} попыток")
            break
        elif  comp_number > player_number:
            print("Моё число больше")
        elif  comp_number < player_number:
            print("Моё число меньше")
    else:
        print(f"Увы, но Вы проиграли! Число было {comp_number}")

    i = input("Хотите начать игру заново? Y/N  ")
    if i == 'N' or i =='n':
        print()
        print("Спасибо за игру")
        break
    elif i == 'Y' or i =='y':
        print()
        print("Хорошее решение!")
    else:
        print("Спасибо за игру")
    