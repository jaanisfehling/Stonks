index1 = []
index2 = []
index_lenght = 1
f = open("../data/fetched.txt", "r")
fetched = eval(f.readline())
f.close()

# Nach Monatszuwachs sortieren
fetched.sort(key=lambda x: x[1], reverse=True)
index1 = [fetched[i][0] for i in range(index_lenght)]

# Nach KGV sortieren
fetched.sort(key=lambda x: x[2])
i = 0
j = 0
while j < index_lenght:
    if fetched[i][2] > 0:
        index2.append(fetched[i][0])
        j += 1
    i += 1

print("\nIndex 1:\n")
for i in index1: print(i)
print("\nIndex 2:\n")
for i in index2: print(i)

f = open("../data/index1.txt", "w")
f.write(str(index1))
f.close()
f = open("../data/index2.txt", "w")
f.write(str(index2))
f.close()
