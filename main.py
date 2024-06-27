print("0. Hello World!!!")
#Задача «Длина слова».
print("количество знаков'wht fk mz fk':")
print(len('wht fk mz fk'))
#######
#Практическое задание по уроку "Базовые структуры данных"
#Задача «Суммы и разности».
def diff(a, b):#введение фунkции "difference" для значений first, second
    return a - b# что должна возвращать э та фунция
print("1. разница между числами 222 и 56 состaвляет:")
first = 222
second = 56
result1 = diff(first, second)#хз как это работает но вроде логично
print(result1)#print он и в африке print
#
#Задача «Суммы и разности».
def summa(a, b):#введение фунkции "summa" для значений first, second
    return a + b# что должна возвращать эта фунkция
print("2. сумма чисeл 222 и 56 состaвляет:")
first = 222
second = 56
result2 = summa(first, second)#хз как это работает но вроде логично
print(result2)#print он и в африке print
#
#Задача «Среднее арифметическое» пример 2.
def mean(first, second, third):#введение фунkции "mean" для значений first, second, third
    return (first+second+third)/3# что должна возвращать эта фунkция
print("3. средняя арифметическая чисел 1, 15, 159 состaвляет:")
first = 1
second = 15
third = 159
result3 = mean(first, second, third)#хз как это работает но вроде логично
print(result3)
#
#Задача «Простые строчки». first_string и second_string
print("4. простые строчки")
def simplestr(first_string, second_string):#введение фунkции "simplestr" для значений first_string, second_string
    return first_string + ", " + second_string  # возврат двух строк, разделенных запятой
first_string = "monday"
second_string = "tuesday"
result4 = simplestr(first_string, second_string)  # исправлено использование переменных
print(result4)
#
#Задача «Сложная формула».
def f(a,b,c):#введение фунkции "mean" для значений first, second, third
    return ((a*b)+(a*c))# что должна возвращать эта фунkция
print("5. вычисление =(a*b)+(a*c) где  a=1, b=15, c=159 состaвляет:")
a = 1
b = 15
c = 159
result5 = f(a, b, c)#хз как это работает но вроде логично
print(result5)#print он и в африке print
print("ДАЛЕЕ НЕ ПО ЗАДАНИЯМ!")
#как пример «Среднее арифметическое»:
print("средняя арифметическая чисел 1, 2, 3 состaвляет:")
from statistics import mean
average = mean([1, 2, 3])
print(average)
#####
#Прочее
print("поиск отличий в текстовой строке st1 относительно st2:")#искал вычисление разницы между числами нашел это
st2 = {'F', 'F', 'F', 'D', 'F'}
st1 = {'F', 'A', 'F', 'F', 'F'}
restxt = st1.difference(st2)
print(restxt)#искал вычисление разницы между числами нашел это. беру на заметку.