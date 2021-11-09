# 2.5

price_list = [] # список для цен на товары
new_price_list = [] # новый список для цен по убыванию
top_expensive = [] # новый список для 5 самых дорогих цен по возрастанию

text = [] # список для вывода текста

for i in range(1, 21): #
    prices = float(input('Введите цену каждого товара в руб. и коп.: ')) # вводим числа
    price_list.append(prices) # добавим числа в списку
    new_price_list.append(prices)
    top_expensive.append(prices)

    price_rub = round(prices // 1) # выводим числа перед запятой
    price_penny = round(prices % 1 * 100) # выводим числа после запятой

    text.append([price_rub, price_penny]) # добавим оба числа в отдельный список в списке

print()

print(sorted(price_list), '\n') # по возрастанию
print(sorted(new_price_list, reverse=True), '\n') # по убыванию
print(sorted(sorted(top_expensive, reverse=True)[:5]), '\n') # 5 самых дорогих цен по возрастанию

for i in text:
    print(f'{i[0]} руб {str(i[1]).zfill(2)} коп') # выводим тексты











