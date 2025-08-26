n = int(input())
if n > 5:
    quo = n//5
    if n % 5 ==0:
        print(quo)
    else:
        print(quo+1)
else:
    print("1")
