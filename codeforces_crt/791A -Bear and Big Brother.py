a,b = map(int,input().split())
'''if a > b:
    print("0")
elif a == b:
    print("1")
else:'''
count = 0
while a <= b:
    count += 1
    a *= 3
    b *= 2
print(count)

