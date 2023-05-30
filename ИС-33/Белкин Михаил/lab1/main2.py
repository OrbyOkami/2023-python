import datetime
from queue import Queue
user = ("Белкин Михаил Александрович", 3, 11, 2004)
predmet = {
"химия": 4,
"физика": 5,
"математика" : 4,
"обж": 2,
"русский": 4,
"география": 5,
"обществознание": 3,
"технология": 5,
"музыка": 5,
"литература": 4,
"информатика": 5,
"физкультура": 5,
"английский": 4,
"история": 4
}
parents = ["Ольга", "Александр", "Татьяна", "Николай", "Екатерина", "Михаил", "Ольга", "Александр"]
kiwiNAME = "Бубочка"

# 1. вывести среднюю оценку в аттестате
print("1. Средняя оценка: ")
print((predmet['химия'] + predmet['физика'] + predmet['математика'] + predmet['обж'] + predmet['русский'] + predmet['география'] + predmet['обществознание'] + predmet['технология'] + predmet['музыка'] + predmet['литература'] + predmet['информатика'] + predmet['физкультура'] + predmet['английский'] + predmet['история']) / 14, '\n')

# 2. вывести уникальные имена среди своих родственников (включая свое)
print("2. Уникальные имена: ")
names = list(set(parents))
print(names, '\n')

# 3. общая длина всех названий предметов
print("3. Общая длина всех названий предметов: ")
n = "химия" + "физика" + "математика" + "обж" + "русский" + "география" + "обществознание" + "технология" + "музыка" + "литература" + "информатика" + "физкультура" + "английский" + "история"
print(len(n), '\n')

# 4. уникальные буквы в названиях предметов
print("4. Уникальные буквы в названиях предметов: ")
n = "химия" + "физика" + "математика" + "обж" + "русский" + "география" + "обществознание" + "технология" + "музыка" + "литература" + "информатика" + "физкультура" + "английский" + "история"
p = list(set(n))
print(p, '\n')

# 5. имя вашей домашней пушистой кивы в бинарном виде
print("5. Имя вашей домашней пушистой кивы в бинарном виде: ")
bin_result = ''.join(format(ord(x), '08b') for x in kiwiNAME)
print(bin_result, '\n')

# 6. отсортированный по алфавиту (в обратном порядке) список родственников;
print("6. Отсортированный по алфавиту (в обратном порядке) список родственников: ")
print(sorted(parents, reverse=True))
print('\n')

# 7. количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)
print("7. количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной) ")
data = datetime.date(user[3], user[2], user[1])
today = datetime.date.today() # получаем текущую дату
delta = today - data
days = delta.days
print(f"Количество дней с даты рождения {user[0]}: {days}", '\n')

# 8. FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все)
print("8. FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки), после введения - вывести все ")
q = Queue()
print("Введите элементы очереди по одному, для остановки введите 'стоп'")
while True:
    index = input("Индекс элемента очереди: ")
    if index.lower() == 'стоп':
        break
        q.put(index)
    while not q.empty():
        print(q.get())
    print('\n')

# 9. по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя
print("9. по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя ")
zadan9 = (3 + 11**2 + 2004) % 21 + 1;
print("элемент в списке",zadan9,"\n")
parents = ["Ольга", "Александр", "Татьяна", "Николай", "Екатерина", "Михаил", "Ольга", "Александр"]
parents[7] = "Tizoc"
print(parents, '\n')

# 10. создать связный список, как словарь, где ключ - имя родственника)
print("10. Cоздать связный список, как словарь, где ключ - имя родственника ")
family = [
{'name': 'Ольга', 'year': 1995},
{'name': 'Александр', 'year': 1983},
{'name': 'Татьяна', 'year': 1976},
{'name': 'Екатерина', 'year': 2007},
{'name': 'Михаил', 'year': 1987}
]
linked_list = {}
for i in range(len(sorted_family)):
    if i == len(sorted_family) - 1:
        linked_list[sorted_family[i]['name']] = None  # последний элемент списка не имеет соседа
    else:
        linked_list[sorted_family[i]['name']] = sorted_family[i+1]['name']

print(linked_list, '\n')

# 11. написать функцию-генератор
print("11. Написать функцию-генератор ")
number = len("Белкин Михаил Александрович") * len ("Ольга Александр Татьяна Николай Екатерина Ольга Александр") % 4
print("Номер варианта ", number, '\n')
def leonardo():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b + 1
        yield b

gen = leonardo()

# Генерация и вывод первых 10 чисел Леонардо
for i in range(10):
    print(next(gen), '\n')

# сортируем список по годам рождения
sorted_family = sorted(family, key=lambda x: x['year'])
