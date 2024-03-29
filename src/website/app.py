from flask import Flask, render_template, request
import graph
import bot.tg_bot as tg_bot
app = Flask(__name__)
@app.route("/", methods=['POST', "GET"])
def index():
    
    admin = 'pydrag0n'
    graph_root = "graphics\\"
    datas_root = "datas\\"
    # channel_link = "naebnet"

    if request.method == 'POST':
        channel_link = request.form['channel_link']
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
        
        
    return render_template("index.html")

app.run()