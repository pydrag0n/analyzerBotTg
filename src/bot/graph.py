from matplotlib import pyplot
import json
import datetime

# file_name,  название json файла
class DataPlotter:
    def __init__(self, 
                 data_file_name:str,
                 save_file_name:str,
                 channel_name:str="channelname"
                 ):
        
        self.data_file_name = data_file_name
        self.channel_name = channel_name
        self.save_file_name = save_file_name
        self.views_list = []
        self.date_list = []
        self.date_obj = []

    def load_data(self):
        with open(self.data_file_name, 'r', encoding='utf-8') as f:
            datas_list = json.loads(f.read())

        for datas in datas_list:
            self.views_list.append(datas['views'])
            self.date_list.append(datas['date'])

        self.date_obj = [datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S") for dt_str in self.date_list]

    def plot_graph(self):
        fig, ax = pyplot.subplots()
        ax.plot(self.date_obj[::-1], self.views_list[::-1])
        ax.xaxis_date()
        fig.autofmt_xdate()
        pyplot.xlabel("Time")
        pyplot.ylabel("Views")
        pyplot.title(f"{self.channel_name} | Views")
        pyplot.savefig(f"{self.save_file_name}")

def draw(data_file_name: str,
         save_file_name:str,
         channel_name:str
         ):
    
    plotter = DataPlotter(data_file_name=data_file_name, 
                            save_file_name=save_file_name,
                            channel_name=channel_name
                            )
    
    plotter.load_data()
    plotter.plot_graph()