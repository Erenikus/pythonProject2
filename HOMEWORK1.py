# Задача:
# Выполните следующие действия в PyCharm:
# В переменную example запишите любую строку.
# Выведите на экран(в консоль) первый символ этой строки.
# Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
# Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
# Выведите на экран(в консоль) это слово наоборот.
# Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
#varian1
example='Tопинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])
#varian2
print(example[0]+'\n'+example[-1]+'\n'+example[5:]+'\n'+example[::-1]+'\n'+example[1::2])
