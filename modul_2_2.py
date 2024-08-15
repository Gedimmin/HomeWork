first = int(input("Введите число:"))
second = int(input("Введите число:"))
third = int(input("Введите число:"))
if first == second and third == first and second == third:
    print(3)
elif first == second or third == first or second == third:
    print(2)
else:
    print(0)
