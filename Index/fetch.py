import tools.constants, sys, pyEX

fetched = []
publishable = tools.constants.iex_publishable
secret = tools.constants.iex_secret
c = pyEX.Client(api_token=secret, version="sandbox")

# Prozentanzeige
f = open("../data/test.txt", "r")
total = len(f.readlines())
f.close()
f = open("../data/test.txt", "r")
counter = 0

# Alle Aktien iterieren
for sym in f.readlines():
    counter += 1
    # \n entfernen
    sym = sym.rstrip()

    # Falls Fehler in Daten auftreten bzw. Daten nicht vorhanden sind
    try:
        # Daten fetchen
        gain = c.keyStats(sym, "month1ChangePercent")
        kgv = c.keyStats(sym, "peRatio")

        # Prozentanzeige
        sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | " + str(round(gain, 2)) + "% | " + str(kgv))

    # Keine Daten verfügbar
    except pyEX.common.PyEXception:
        sys.stdout.write("\r" + str(round((counter/total)*100, 2)) + "% | " + sym + " | No Data available.")

    else:
        # Daten in Liste speichern
        fetched.append([sym, gain, kgv])

f.close()
f = open("../data/fetched.txt", "w")
f.write(str(fetched))
f.close()
