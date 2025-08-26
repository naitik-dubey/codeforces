t = int(input())

for _ in range(t):
    size, k = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    i = 0
    while i <= size - k:
        if all(arr[i + l] == 0 for l in range(k)):
            count += 1
            i += k + 1
        else:
            i += 1
    print(count)
