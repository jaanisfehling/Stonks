import re

f = open("../data/msciworld.txt", "r")
new = ""
for line in f.readlines():
    # nur die ersten 6 zeichen sind relevant
    if line != "r Derivate	-\n":
        new += line


f.close()

f = open("../data/msciworld.txt", "w")
f.truncate()
f.writelines(new)
f.close()
