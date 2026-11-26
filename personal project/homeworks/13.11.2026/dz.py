#1
login = input("Логин: ")
password = input("Пароль: ")
if login == "admin" and password == "1234":
  print("Вход выполнен")
else:
  print("Ошибка входа")

#2
s = 0
k = 0
n = int(input("Сколько чисел: "))
for i in range(n):
  x = int(input("Число: "))
  if x > 0:
    s += x
    k += 1
print(s / k if k else 0)

#3
n = int(input("Сколько чисел: "))
mx = None
for i in range(n):
  x = int(input("Число: "))
  if mx is None or x > mx:
    mx = x
print(mx)
