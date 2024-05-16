from fractions import Fraction

def operations_with_fractions(fraction1, fraction2):
    try:
        # Разбиваем строки на числитель и знаменатель
        num1, denom1 = map(int, fraction1.split('/'))
        num2, denom2 = map(int, fraction2.split('/'))

        # Создаем объекты Fraction для дробей
        frac1 = Fraction(num1, denom1)
        frac2 = Fraction(num2, denom2)

        # Вычисляем сумму и произведение дробей
        sum_result = frac1 + frac2
        product_result = frac1 * frac2

        return sum_result, product_result

    except ValueError:
        print("Ошибка: Неправильный формат ввода. Используйте формат 'a/b' для дробей.")

# Получение ввода от пользователя
fraction1 = input("Введите первую дробь в формате 'a/b': ")
fraction2 = input("Введите вторую дробь в формате 'a/b': ")

# Выполнение операций с дробями
sum_result, product_result = operations_with_fractions(fraction1, fraction2)

if sum_result is not None and product_result is not None:
    print("Сумма дробей:", sum_result)
    print("Произведение дробей:", product_result)
