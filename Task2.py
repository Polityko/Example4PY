# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.


data = open('Icecream.txt', encoding= 'utf-8')
icecream = data.readlines()
data.close

assortiment = set(icecream[0].replace('\n', '').split(', '))
sklad = set(icecream[1].replace('\n', '').split(', '))
print(assortiment)
print(sklad)
print(assortiment.difference(sklad))