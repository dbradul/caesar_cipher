import string

s = open("alice.txt").read().lower()

stat = {}
for c in s:
    if c in string.ascii_lowercase:
        if c in stat:
            stat[c] += 1
        else:
            stat[c] = 1

for char in sorted(stat, key=stat.get, reverse=True):
    #print("{1}->{0}".format(char, stat[char]))
    print(char + "->" + str(stat[char]))
