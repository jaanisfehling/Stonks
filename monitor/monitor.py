import pyEX, matplotlib, tools.constants

publishable = tools.constants.iex_publishable
secret = tools.constants.iex_secret
c = pyEX.Client(api_token=secret, version="sandbox")
f = open("./data/index1.txt", "r")

index = eval(f.readline())
graph = {}
for sym in index.keys():
    data = c.chart(sym)
    for i in data():
        if graph == {}:

