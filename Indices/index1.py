import tools.constants, time, sys
import pyEX

class index1():

    def __init__(self):
        self.index = []
        self.index_lenght = 25
        self.publishable = tools.constants.iex_publishable
        self.secret = tools.constants.iex_secret
        self.c = pyEX.Client(api_token=self.secret, version="sandbox")
        self.revalue()

    def revalue(self):
        # Prozentanzeige
        f = open("../data/test.txt", "r")
        total = len(f.readlines())
        f.close()
        f = open("../data/test.txt", "r")
        counter = 0

        for sym in f.readlines():
            counter += 1
            sym = sym.rstrip()

            data = self.c.chart(sym)

            try:
                # Monatszuwachs berechnen (in %)
                gain = (data[-1]["close"] / data[0]["close"] -1)*100

                # Prozentanzeige
                sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | " + str(data[0]["date"]) + ": " + str(data[0]["close"]) + " | " + str(data[-1]["date"]) + ": " + str(data[-1]["close"]) + " | " + str(round(gain, 2)) + "%")

            # Keine Daten verfügbar
            except KeyError:
                sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | No Data available.")

            else:
                # Falls über 15% Monatszuwachs
                if gain >= 15:
                    self.index.append(sym)
        f.close()

        print("\nIndex 1:\n")
        for i in self.index: print(i)
        f = open("../data/index1.txt", "w")
        f.write(str(self.index))
        f.close()

index1()
