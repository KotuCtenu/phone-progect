def how_you_old():
    age = int(input('Введите возраст'))
    if age >= 0 and age <= 12:
        print('Доступ запрещён!')
    else:
        print('Добро пожаловать!')

how_you_old()
              