# Wrong Answer

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = sorted((x % k, x) for x in map(int, input().split()))
    T = sorted((x % k, x) for x in map(int, input().split()))
    print("YES" if S == T else "NO")