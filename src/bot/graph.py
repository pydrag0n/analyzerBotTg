from matplotlib import pyplot
import json
import datetime

# file_name,  название json файла
class DataPlotter:
    def __init__(self, file_name: str, channel_name: str="channelname"):
        self.file_name = file_name
        self.channel_name = channel_name
        self.views_list = []
        self.date_list = []
        self.date_obj = []

    def load_data(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
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
        pyplot.title("Channel Name | Views")
        pyplot.savefig(f"{self.channel_name}.png")

def main():
    file_name = "datas.json"
    plotter = DataPlotter(file_name)
    plotter.load_data()
    plotter.plot_graph()

main()