# 1
a = int(input("Введите начало: "))
b = int(input("Введите конец: "))

s1 = c1 = s2 = c2 = s3 = c3 = 0

for i in range(a, b + 1):
  if i % 2 == 0:
    s1 += i
    c1 += 1
  else:
    s2 += i
    c2 += 1
  if i % 9 == 0:
    s3 += i
    c3 += 1

print(s1, s1 / c1 if c1 else 0)
print(s2, s2 / c2 if c2 else 0)
print(s3, s3 / c3 if c3 else 0)

# 2
l = int(input("Длина: "))
sym = input("Символ: ")
for i in range(l):
  print(sym)

# 3
while True:
  n = int(input("Число: "))
  if n == 7:
    print("Good bye!")
    break
  if n > 0:
    print("Number is positive")
  elif n < 0:
    print("Number is negative")
  else:
    print("Number is equal to zero")

# 4
s = 0
mx = mn = None
f = True
while True:
  n = int(input("Число: "))
  if n == 7:
    print("Good bye!")
    break
  s += n
  if f:
    mx = mn = n
    f = False
  else:
    if n > mx:
      mx = n
    if n < mn:
      mn = n

print(s, mx, mn)
