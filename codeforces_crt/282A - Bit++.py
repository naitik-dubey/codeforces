n = int(input())
count = 0
'''
for _ in range(n):
    bit = input();
    if bit == "X++" or bit == "++X":
        count += 1
    elif bit == "X--" or bit == "--X":
        count -= 1
print(count)'''
for _ in range(n):
    bit = input()
    if bit in('X++','++X'):
        count += 1
    elif bit in('X--','--X'):
        count -= 1
print(count);