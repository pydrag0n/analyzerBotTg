from matplotlib import pyplot 
import json

import datetime


with open("datas.json", 'r', encoding='utf-8') as f:
    datas_list = json.loads(f.read())
    
views_list = []
date_list = []
for datas in datas_list:
    views_list.append(datas['views'])
    date_list.append(datas['date'])
 
date_obj = []
for dt_str in date_list:
    dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    date_obj.append(dt.month)

print(type(views_list[1]))
pyplot.bar(date_obj[::-1], views_list[::-1], 0.2)

pyplot.xlabel("Время")
pyplot.ylabel("Просмотры")
pyplot.title("Chanell name |Views")
pyplot.savefig("chnellname.png")