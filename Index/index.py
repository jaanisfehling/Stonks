import tools.constants, sys, pyEX

index1 = []
index2 = []
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

    data = c.keyStats(sym)

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
        # Falls über 15% Monatszuwachs
        if gain >= 15:
            index1.append(sym)
        # Falls KGV unter 20
        if kgv < 10:
            index2.append(sym)
f.close()

print("\nIndex 1:\n")
for i in index1: print(i)
print("\nIndex 2:\n")
for i in index2: print(i)

f = open("../data/index1.txt", "w")
f.write(str(index1))
f = open("../data/index2.txt", "w")
f.write(str(index2))
f.close()
