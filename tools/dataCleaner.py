import re

f = open("../data/s&p500.txt", "r")
new = ""
for line in f.readlines():
    if line != "r Derivate	-\n":
        new += line


f.close()

f = open("../data/s&p500.txt", "w")
f.truncate()
f.writelines(new)
f.close()
