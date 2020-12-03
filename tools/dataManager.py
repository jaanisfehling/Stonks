import re

f = open("../data/test.txt", "r")
new = ""
for line in f.readlines():
    line = line.split("\t")[0]
    new += line + "\n"


f.close()

f = open("../data/test.txt", "w")
f.truncate()
f.writelines(new)
f.close()
