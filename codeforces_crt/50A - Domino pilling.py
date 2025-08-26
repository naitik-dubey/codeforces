'''
You have board size of M x N and each dominos cover exactly 2 square.
You can place dominos vertically or horizontally

you must cover square completely and not overlap and keep dominoes inside the loop
'''
m, n = map(int, input().split())
print((m*n)//2)

