# 2_2 - 2_3

time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов'] # дан список

num = '015723456789'


for i in range(10):
    # string = input()
    # time.append(string)

    if time[1] in num and time[3] in num or time[-2][1::] in num:

        a = int(time[1])  # сделаем число из str в int
        a1 = str(f'"{a:02}"') # конвертируем обратно в str, добавляя кавычки и впереди ноль
        time[1] = a1 # заменим старый элемент в новый

        b = int(time[3])
        b1 = str(f'"{b:02}"')
        time[3] = b1

        if '+' in time[-2][0]:
            c = int(time[-2][1::])
            c1 = str(f'"+{c:02}"')
            time[-2] = c1

        elif '-' in time[-2][0]:
            c = int(time[-2][1::])
            c1 = str(f'"-{c:02}"')
            time[-2] = c1

print(*time)  # распакуем список и выводим результата







