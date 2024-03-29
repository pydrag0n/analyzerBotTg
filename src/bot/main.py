import graph
import tg_bot

admin = 'pydrag0n' #  юзернейм пользователя, которому будут приходить сообщения о запуске бота.
graph_root = "graphics\\" # корневая папка для графиков
datas_root = "datas\\" # корневая папка для json файлов
channel_link = "channel_official" # ссылка на канал без https://t.me/  


data_file_name = f"{datas_root}{channel_link}.json"
graph_file_name = f"{graph_root}{channel_link}.png"

tg_bot.start(admin=admin,
             channel_link=channel_link, 
             save_file=data_file_name
             )

graph.draw(data_file_name=data_file_name, 
           save_file_name=graph_file_name, 
           graph_title="@"+channel_link
           )