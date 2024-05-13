a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Треугольника с такими сторонами не существует")
elif a != b and b != c and a != c:
    print("Треугольник разносторонний")
elif a == b == c:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")

num = int(input("Введите число: "))


