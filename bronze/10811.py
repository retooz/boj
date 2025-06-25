n, m = map(int, input().split())
buckets = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    for i in range((b - a + 1) // 2):
        buckets[a + i], buckets[b - i] = buckets[b - i], buckets[a + i]
print(*buckets[1:])