import re

f = open("../data/msciworld.txt", "r")
new = ""
for line in f.readlines():
    # nur die ersten 6 zeichen sind relevant
    line = line[-13:]
    new += line


f.close()

f = open("../data/msciworld.txt", "w")
f.truncate()
f.writelines(new)
f.close()
