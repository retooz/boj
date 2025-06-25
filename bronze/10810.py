n, m = map(int, input().split())
a = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i-1, j):
        a[x] = k
for i in a:
    print(i, end=' ')