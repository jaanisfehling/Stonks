import re

f = open("msciworld.txt", "r")
new = ""
for line in f.readlines():
    line = line[:-10]
    line = line.rstrip()
    line += "\n"
    new += line
f.close()

f = open("msciworld.txt", "w")
f.truncate()
f.writelines(new)
f.close()