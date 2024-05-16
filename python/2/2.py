def to_hex(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal

# Получение целого числа от пользователя
number = int(input("Введите целое число: "))

# Получение шестнадцатеричного представления числа
hexadecimal_representation = to_hex(number)

print("Шестнадцатеричное представление числа:", hexadecimal_representation)

# Проверка результата с использованием встроенной функции hex()
print("Проверка с использованием встроенной функции hex():", hex(number))
