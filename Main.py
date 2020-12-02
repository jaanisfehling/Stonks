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

        f = open("data/test.txt", "r")
        for sym in f.readlines():
            try:
                # Gibt 2 Datenpunkte aus: Heute und letzter Tag des letzen Monats
                # meat_data ist irrelevant, z.B Zeitzone etc.
                data, meta_data = self.ts.get_daily(symbol=sym, outputsize="compact")

            # API erlaubt nur 5 Anfragen pro Minute
            except ValueError:
                time.sleep(60)

            # Dicitonary in Liste umwandeln
            data_list = []
            for intra in data: data_list.append(data[intra])

            print(data)
            print(data_list[0])
            print(data_list[29], "\n")

            # Monatszuwachs berechnen (in %)
            gain = (float(data_list[0]["4. close"]) / float(data_list[29]["4. close"]) -1) *100
            print(sym + " " + str(gain) + "%")

            if gain >= 15:
                self.index.update({sym: gain})

        print(self.index)
        f.close()

Main()
