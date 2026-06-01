n = int(input("Введите размер массива N: "))

arr = []
for i in range(n):
    num = float(input(f"Введите элемент {i+1}: "))
    arr.append(num)

ind_max = arr.index(max(arr))
ind_min = arr.index(min(arr))

left = min(ind_max, ind_min)
right = max(ind_max, ind_min)

sum_neg = 0
for i in range(left + 1, right):
    if arr[i] < 0:
        sum_neg += arr[i]

print("\nМассив:", arr)
print(f"Индекс макс. элемента ({arr[ind_max]}): {ind_max}")
print(f"Индекс мин. элемента ({arr[ind_min]}): {ind_min}")
print(f"Границы поиска: от индекса {left} до {right}")
print(f"Сумма отрицательных элементов между ними: {sum_neg}")
