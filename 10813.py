n, m = map(int, input().split())
buckets = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    buckets[a], buckets[b] = buckets[b], buckets[a]
print(*buckets[1:])