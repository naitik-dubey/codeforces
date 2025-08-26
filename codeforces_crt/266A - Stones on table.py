n = int(input())
s = input().strip()
count = 0
first = s[0]
for i in range(1,n):
    if first == s[i]:
        count += 1
    first = s[i]
print(count)

