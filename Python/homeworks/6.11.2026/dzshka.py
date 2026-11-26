import random
import math
#1
'''lst1 = [random.randint(-10, 10) for _ in range(15)]
print("Список 1:", lst1)

sum_neg = sum(x for x in lst1 if x < 0)
sum_even = sum(x for x in lst1 if x % 2 == 0)
sum_odd = sum(x for x in lst1 if x % 2 != 0)

prod_index_3 = 1
for i in range(0, len(lst1), 3):
    prod_index_3 *= lst1[i]

min_idx = lst1.index(min(lst1))
max_idx = lst1.index(max(lst1))
start_idx = min(min_idx, max_idx) + 1
end_idx = max(min_idx, max_idx)
sublist_min_max = lst1[start_idx:end_idx]
prod_min_max = math.prod(sublist_min_max) if sublist_min_max else 0

pos_indices = [i for i, x in enumerate(lst1) if x > 0]
sum_between_pos = 0
if len(pos_indices) >= 2:
    start_pos = pos_indices[0] + 1
    end_pos = pos_indices[-1]
    sum_between_pos = sum(lst1[start_pos:end_pos])

print("Сумма отрицательных:", sum_neg)
print("Сумма четных:", sum_even)
print("Сумма нечетных:", sum_odd)
print("Произведение (индексы кратны 3):", prod_index_3)
print("Произведение между мин и макс:", prod_min_max)
print("Сумма между первым и последним положительными:", sum_between_pos)'''

#2
'''lst2 = [random.randint(-20, 20) for _ in range(15)]
print("Список 2:", lst2)

list_even = [x for x in lst2 if x % 2 == 0]
list_odd = [x for x in lst2 if x % 2 != 0]
list_neg = [x for x in lst2 if x < 0]
list_pos = [x for x in lst2 if x > 0]

print("Четные:", list_even)
print("Нечетные:", list_odd)
print("Отрицательные:", list_neg)
print("Положительные:", list_pos)'''