f = open('27.txt') # Открываем файл
d = 5
k = 0 # количество наборов
knc = 0 # количество нечетных элементов в наборе
summ = 0 # сумма чисел в наборе
pr = 1 # произведение четных элементов в наборе
n = int(f.readline()) # Считываем N - количество чисел
mas = [] # создаем массив  для чисел
for i in range(n):
    x = int(f.readline())
    mas.append(x)
f = [] # занесем 100 чисел в этот массив
for i in range(d):
    f.append(mas[i]) # заносим числа в массив
    if mas[i] % 2 == 0: # смотрим произведение, если четно иначе считаем количество нечетных чисел
        pr *= mas[i]
    else:
        knc += 1
    summ += mas[i] # считаем сумму 
print(f,knc,summ,pr)
if (knc <= 50) and (pr > 10000) and (pr % 120 == 0) and (summ > 1000): # проверяем подходит ли первый набор
    k += 1
for i in range(n - d):
    if f[0] % 2 == 0: #  убираем число первое в наборе
        pr //= f[0] # если число четно, то делим
    else:
        knc -= 1 # если число нечетно, то количество нечетных чисел уменьшаем
    summ -= f[0] # вычитаем из суммы
    del f[0] # удаляем первое число в наборе 
    x = mas[i + d]
    f.append(x)  # добавляем новое число в набор
    if x % 2 == 0: # делаем аналогичные действия в предыдущем форе
        pr *= x
    else:
        knc += 1
    summ += x
    if (knc <= 50) and (pr > 10000) and (pr % 120 == 0) and (summ > 1000): # проверяем подходит линабор
        k += 1
    print(f,knc,summ,pr)
if (knc <= 50) and (pr > 10000) and (pr % 120 == 0) and (summ > 1000): # проверяем подходит ли  набор
    k += 1
print(k) # ответ
