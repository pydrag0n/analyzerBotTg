import tg_bot
import graph

admin = 'pydrag0n'
graph_root = "graphics\\"
datas_root = "datas\\"
channel_link = "PyNikola7"
data_file_name = f"{datas_root}{channel_link}.json"
graph_file_name = f"{graph_root}{channel_link}.png"

tg_bot.start(admin=admin,
             channel_link=channel_link, 
             save_file=data_file_name
             )

graph.draw(data_file_name=data_file_name, 
           save_file_name=graph_file_name, 
           channel_name=channel_link
           )