num = int(input("Введите число: "))
if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и не больше 100 тысяч")


is_prime = True
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False

print("Число", num, "является", "простым" if is_prime else "составным")
