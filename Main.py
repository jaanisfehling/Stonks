import tools.constants, tools.dateHelper, time, sys
import pyEX

class Main():

    def __init__(self):
        self.index = {}
        self.index_lenght = 25
        self.publishable = tools.constants.iex_publishable
        self.secret = tools.constants.iex_secret
        self.c = pyEX.Client(api_token=self.secret, version="sandbox")
        self.revalue()

    def revalue(self):
        # Prozentanzeige
        f = open("data/iex.txt", "r")
        total = len(f.readlines())
        f.close()
        f = open("data/iex.txt", "r")
        counter = 0

        for sym in f.readlines():
            counter += 1
            sym = sym.rstrip()

            data = self.c.chart(sym)

            # Monatszuwachs berechnen (in %)
            gain = (data[-1]["close"] / data[0]["close"] -1)*100

            # Prozentanzeige
            sys.stdout.write("\r" + str(round((counter/total)*100, 1)) + "% | " + sym + " | " + str(data[0]["date"]) + ": " + str(data[0]["close"]) + " | " + str(data[-1]["date"]) + ": " + str(data[-1]["close"]) + " | " + str(gain) + "%")

            # Falls über 15% Monatszuwachs
            if gain >= 15:
                self.index.update({sym: gain})

        f.close()
        print("Index:\n")
        for i in self.index: print(i)
        f = open("data/index.txt", "w")
        f.write(str(self.index))
        f.close()

Main()
