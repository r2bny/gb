from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

for attempt in range(1, attempts + 1):
    guess = int(input("Попытка №{}: Введите вашу догадку: ".format(attempt)))

    if guess < secret_number:
        print("Загаданное число больше")
    elif guess > secret_number:
        print("Загаданное число меньше")
    else:
        print("Поздравляем! Вы угадали число:", secret_number)

print("К сожалению, вы не угадали. Загаданное число было:", secret_number)
