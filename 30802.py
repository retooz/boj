n = int(input())
size = [i for i in map(int, input().split())]
t, p = map(int, input().split())
cnt = 0
for i in size:
    if i % t == 0:
        cnt += i // t
    else:
        cnt += i // t + 1
print(cnt)
print(n // p, end=' ')
print(n % p)