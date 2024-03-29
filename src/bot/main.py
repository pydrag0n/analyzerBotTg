import graph
import tg_bot

admin = 'pydrag0n' #  юзернейм пользователя, которому будут приходить сообщения о запуске бота.
channel_link = "naebnet" # ссылка на канал без https://t.me/  
LIMIT = 5000 # количество постов которое надо спарсить
graph_root = "graphic\\" # корневая папка для графиков
datas_root = "data\\" # корневая папка для json файлов


data_file_name = f"{datas_root}{channel_link}.json"
graph_file_name = f"{graph_root}{channel_link}.png"

tg_bot.start(admin=admin,
             channel_link=channel_link,
             limit=LIMIT,
             save_file=data_file_name
             )

graph.draw(data_file_name=data_file_name, 
           save_file_name=graph_file_name, 
           graph_title="@"+channel_link
           )