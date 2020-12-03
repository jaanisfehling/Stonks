import tools.constants, tools.DateHelper, time
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

            # Daten von min. einem Monat früher
            old_date = tools.DateHelper.oneMonthEarlier(list(data.keys())[0])
            # Falls Tag in Daten nicht existiert
            if old_date not in data.keys():
                old_date = tools.DateHelper.oneDayEarlier(old_date)

            print(data)
            print(list(data.keys())[0])
            print(data[old_date], "\n")

            # Monatszuwachs berechnen (in %)
            gain = (float(list(data.values())[0]["4. close"]) / float(data[old_date]["4. close"]) -1) *100
            print(sym + " " + str(gain) + "%")

            if gain >= 15:
                self.index.update({sym: gain})

        print(self.index)
        f.close()

Main()
