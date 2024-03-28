from matplotlib import pyplot
import json
import datetime

# Чтение данных из файла JSON
with open("datas.json", 'r', encoding='utf-8') as f:
    datas_list = json.loads(f.read())

views_list = []
date_list = []
date_obj = []

# Извлечение данных о просмотрах и дате из данных JSON
for datas in datas_list:
    views_list.append(datas['views'])
    date_list.append(datas['date'])

# Преобразование строковых дат в объекты datetime
for dt_str in date_list:
    dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    date_obj.append(dt)

# Построение графика
fig, ax = pyplot.subplots()
ax.plot(date_obj[::-1], views_list[::-1])  # Используется [::-1], чтобы инвертировать порядок данных
ax.xaxis_date()  # Интерпретация значений x-оси как дат
fig.autofmt_xdate()  # Поворот меток времени по оси x

# Добавление названий осей и заголовка графика
pyplot.xlabel("Время")
pyplot.ylabel("Просмотры")
pyplot.title("Название канала | Просмотры")

# Сохранение графика в файл
pyplot.savefig("channelname.png")