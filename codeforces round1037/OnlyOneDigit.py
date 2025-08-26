n = int(input())
while n != 0:
    n -= 1
    num = input().strip()
    min = num[0]
    for i in num:
        if i <= min:
            min = i
    print(min)