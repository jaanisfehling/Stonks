import tools.constants, time, sys
import pyEX

class index2():

    def __init__(self):
        self.index = {}
        self.index_lenght = 25
        self.publishable = tools.constants.iex_publishable
        self.secret = tools.constants.iex_secret
        self.c = pyEX.Client(api_token=self.secret, version="sandbox")
        self.revalue()

    def revalue(self):
        # Prozentanzeige
        f = open("./data/test.txt", "r")
        total = len(f.readlines())
        f.close()
        f = open("./data/test.txt", "r")
        counter = 0

        for sym in f.readlines():
            counter += 1
            sym = sym.rstrip()

            earnings = self.c.earnings(sym)
            price = self.c.price(sym)

            try:
                # KGV
                kgv = price / earnings["earnings"][0]["actualEPS"]

                # Prozentanzeige
                sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | " + str(kgv))

            # Keine Daten verfügbar
            except KeyError:
                sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | No Data available.")

            else:
                # Falls KGV unter 20
                if kgv < 20:
                    self.index.update({sym: 0})

        f.close()

        total_marketcap = 0
        for sym in self.index.keys():
            stats = self.c.keyStats(sym)
            marketcap = stats["marketcap"]
            total_marketcap += marketcap

        for sym in self.index.keys():
            stats = self.c.keyStats(sym)
            marketcap = stats["marketcap"]
            weight = marketcap / total_marketcap
            self.index[sym] = weight

        print("\nIndex 2:\n")
        for i in self.index: print(i)
        f = open("./data/index2.txt", "w")
        f.write(str(self.index))
        f.close()

index2()
