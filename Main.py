import tools.constants
from alpha_vantage.timeseries import TimeSeries

class Main():

    def __init__(self):
        self.index = {}
        self.index_lenght = 25
        self.token_key = tools.constants.key
        self.ts = TimeSeries(key=self.token_key)
        self.revalue()

    def revalue(self):
        f = open("data/feed.txt", "r")
        for sym in f.readlines():
            data, meta_data = self.ts.get_monthly(symbol=sym)
            print(data)
            data_list = []
            for intra in data:
                data_list.append(data[intra])
            gain = float(data_list[0]["4. close"]) / float(data_list[-1]["4. close"]) -1
            print(gain)
            if gain >= 0.15:
                print("hit: " + sym)
                self.index.update({sym: gain})
        print(self.index)
        f.close()

Main()


# Fonds 1: Niedriegen KGV (ca. unter 20)
# KGV = Kurs Aktie/Gewinn Aktie

# Fonds 2: Wachstum
# Monatsanstieg überdurchschnittlich (ca. 15%)
