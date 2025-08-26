from itertools import count

n = input()
ucount = 0
lcount  =0
for i in n:
    if i.isupper():
        ucount += 1
    else:
        lcount +=1
if lcount >= ucount:
    print(n.lower())
else:
    print(n.upper())

