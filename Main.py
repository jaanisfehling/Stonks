import constants

class Main(self):

    def __init__(self):
        self.index = {}
        self.index_lenght = 25
        self.token_publishable = constants.publishable
        self.token_secret = constants.secret

    def revalue(self):
        f = open("data/feed.txt", "r")
        for line in f.readlines():
            if kgv < 20:
                self.index.update({line, 1})



# KGV = Kurs Aktie/Gewinn Aktie
# Fonds 1: Niedriegen KGV (ca. unter 20)

# Fonds 2: Wachstum
# Monatsanstieg überdurchschnittlich (ca. 15%)
