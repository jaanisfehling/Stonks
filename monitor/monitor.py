import pyEX, matplotlib, tools.constants

publishable = tools.constants.iex_publishable
secret = tools.constants.iex_secret
c = pyEX.Client(api_token=secret, version="sandbox")
f = open("../data/index1.txt", "r")
index = eval(f.readline())
dates = []
values = []

# Summe der Marktkapitalisierung aller Aktien im Index
total_marketcap = 0
for sym in index:
    stats = c.keyStats(sym)
    marketcap = stats["marketcap"]
    total_marketcap += marketcap

for sym in index:
    stats = c.keyStats(sym)
    marketcap = stats["marketcap"]
    weight = marketcap / total_marketcap
    index[sym] = weight

for sym in index.keys():
    data = c.chart(sym)
    for intra in data:
        weight = index[sym] * data["close"]
        dates.append(intra["date"])

mpl_dates = matplotlib.dates.date2num(dates)
matplotlib.pyplot.plot_date(mpl_dates, values)
