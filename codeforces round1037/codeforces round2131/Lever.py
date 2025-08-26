t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    excess = sum(max(0, a[i] - b[i]) for i in range(n))
    print(excess + 1)