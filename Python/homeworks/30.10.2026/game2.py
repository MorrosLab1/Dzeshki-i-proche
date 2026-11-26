'''import random

# 1
size = int(input("Введите размер стороны квадрата: "))
for i in range(size):
    print("*" * size)'''

# 2
'''width = int(input("Введите ширину: "))
height = int(input("Введите высоту: "))
for i in range(height):
    print("*" * width)'''

# 3
'''size2 = int(input("Введите размер стороны квадрата: "))
for i in range(size2):
    if i == 0 or i == size2 - 1:
        print("*" * size2)
    else:
        print("*" + " " * (size2 - 2) + "*")'''

# 4
'''w = int(input("Введите ширину: "))
h = int(input("Введите высоту: "))
for i in range(h):
    if i == 0 or i == h - 1:
        print("*" * w)
    else:
        print("*" + " " * (w - 2) + "*")'''

# 1
'''num_str = input("Введите число: ")
while True:
    print("1. Кол-во цифр, 2. Сумма и среднее, 3. Нули, 4. Выход")
    choice = input("Выбор: ")
    
    if choice == '1':
        print("Количество:", len(num_str))
    elif choice == '2':
        summ = 0
        for d in num_str:
            summ += int(d)
        print("Сумма:", summ, "Среднее:", summ / len(num_str))
    elif choice == '3':
        zeros = 0
        for d in num_str:
            if d == '0':
                zeros += 1
        print("Нулей:", zeros)
    elif choice == '4':
        break'''

# 2
'''s = int(input("Введите размер клеточки: "))
for row in range(8):
    for i in range(s):
        for col in range(8):
            if (row + col) % 2 == 0:
                print("*" * s, end="")
            else:
                print("-" * s, end="")
        print()'''

# 3
'''print("1 - Легкий, 2 - Сложный")
lvl = input("Уровень: ")

count = 5 if lvl == '1' else 10
mx = 5 if lvl == '1' else 10
corr = 0

for i in range(count):
    a = random.randint(1, mx)
    b = random.randint(1, mx)
    ans = int(input(f"{a} * {b} = "))
    if ans == a * b:
        corr += 1

print(f"Правильно: {corr} из {count}")

# 4
rhomb_s = int(input("Высота половины ромба: "))
for i in range(rhomb_s):
    print(" " * (rhomb_s - i - 1) + "*" * (2 * i + 1))
for i in range(rhomb_s - 2, -1, -1):
    print(" " * (rhomb_s - i - 1) + "*" * (2 * i + 1))'''