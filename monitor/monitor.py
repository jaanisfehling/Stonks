import pyEX, tools.constants
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

publishable = tools.constants.iex_publishable
secret = tools.constants.iex_secret
c = pyEX.Client(api_token=secret, version="sandbox")
f = open("../data/index1.txt", "r")
index = eval(f.readline())
data = c.chart(index[0])
dates = [0] * len(data)
values = [0.0] * len(data)

# Alle Aktien im Index
for sym in index:
    data = c.chart(sym)

    # Für alle Tagesabschlussdaten
    for i in range(len(data)):
        dates[i] = data[i]["date"]
        values[i] += float(data[i]["close"])

# Alle Werte durch Anzahl der Aktien rechnen
for i in range(len(values)):
    values[i] = values[i] / len(index)

# Graphen darstellen
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
plt.plot(dates, values)
plt.gcf().autofmt_xdate()
plt.show()
