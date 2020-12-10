import tools.constants, sys, pyEX

filtered = []
index1 = []
index2 = []
index_lenght = 10
publishable = tools.constants.iex_publishable
secret = tools.constants.iex_secret
c = pyEX.Client(api_token=secret, version="sandbox")

# Prozentanzeige
f = open("../data/test.txt", "r")
total = len(f.readlines())
f.close()
f = open("../data/test.txt", "r")
counter = 0

for sym in f.readlines():
    counter += 1
    sym = sym.rstrip()

    # Daten fetchen
    data = c.keyStats(sym)

    # Falls Fehler in Daten auftreten bzw. Daten nicht vorhanden sind
    try:
        # Monatszuwachs (in %)
        gain = data["month1ChangePercent"]*100
        # KGV
        kgv = data["peRatio"]

        # Prozentanzeige
        sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | " + str(round(gain, 2)) + "% | " + str(kgv))

    # Keine Daten verfügbar
    except KeyError:
        sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | No Data available.")

    else:
        # Daten in Liste speichern
        filtered.append([sym, gain, kgv])

f.close()

# Nach Monatszuwachs sortieren
filtered.sort(key=lambda x: x[1], reverse=True)
index1 = [filtered[i][0] for i in range(index_lenght)]

# Nach KGV sortieren
filtered.sort(key=lambda x: x[2])
i = 0
while i < index_lenght:
    if filtered[i][2] != 0:
        index2.append(filtered[i][0])
        i += 1

print("\nIndex 1:\n")
for i in index1: print(i)
print("\nIndex 2:\n")
for i in index2: print(i)

f = open("../data/index1.txt", "w")
f.write(str(index1))
f = open("../data/index2.txt", "w")
f.write(str(index2))
f.close()
