import tools.constants, time
from alpha_vantage.timeseries import TimeSeries

class Main():

    def __init__(self):
        self.index = {}
        self.index_lenght = 25
        self.token_key = tools.constants.key
        self.ts = TimeSeries(key=self.token_key)
        self.revalue()

    def revalue(self):

        f = open("data/msciworld.txt", "r")

        for sym in f.readlines():
            try:
                # Gibt 2 Datenpunkte aus: Heute und letzter Tag des letzen Monats
                # meat_data ist irrelevant, z.B Zeitzone etc.
                data, meta_data = self.ts.get_monthly(symbol=sym)
            # API erlaubt nur 5 Anfragen pro Minute
            except ValueError:
                time.sleep(60)
            print(data)

            # Dicitonary in Liste umwandeln
            data_list = []
            for intra in data: data_list.append(data[intra])

            # Monatszuwachs berechnen
            gain = float(data_list[0]["4. close"]) / float(data_list[-1]["4. close"]) -1
            print(gain)

            if gain >= 0.15:
                print("hit: " + sym)
                self.index.update({sym: gain})

        print(self.index)
        f.close()

Main()
