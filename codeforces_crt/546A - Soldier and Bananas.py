price, money, quant = map(int,input().split())
dollar = 0
for i in range(1,quant+1):
    dollar += i * price
if dollar <= money:
    print("0")
else:
    print(dollar - money)