import re

f = open("../data/s&p500.txt", "r")
new = ""
for line in f.readlines():
    line = line.split(" ")[0]
    new += line + "\n"


f.close()

f = open("../data/s&p500.txt", "w")
f.truncate()
f.writelines(new)
f.close()
