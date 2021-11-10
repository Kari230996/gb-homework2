# 2.5

price_list = [34.64, 268.4, 76, 35.98, 545.64, 43, 7.54, 43.64, 21,9 ] # список для цен на товары
new_price_list = [] # новый список для цен по убыванию
top_expensive = [] # новый список для 5 самых дорогих цен по возрастанию

text = [] # список для вывода текста

for i in range(len(price_list)): #
    # prices = float(input('Введите цену каждого товара в руб. и коп.: ')) # вводим числа, если хотим создать вручную
    # price_list.append(prices) # добавим числа в списку
    new_price_list.append(price_list[i])
    top_expensive.append(price_list[i])

    price_rub = round(price_list[i] // 1) # выводим числа перед запятой
    price_penny = round(price_list[i] % 1 * 100) # выводим числа после запятой

    text.append([price_rub, price_penny]) # добавим оба числа в отдельный список в списке

print()

print(sorted(price_list), '\n') # по возрастанию
print(sorted(new_price_list, reverse=True), '\n') # по убыванию
print(sorted(sorted(top_expensive, reverse=True)[:5]), '\n') # 5 самых дорогих цен по возрастанию

for i in text:
    print(f'{i[0]} руб {str(i[1]).zfill(2)} коп') # выводим тексты











