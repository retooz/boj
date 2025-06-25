n = int(input())
s = input().strip()
cnt = 0
for i in range(n//2):
    if s[i] != s[n - i - 1]:
        cnt += 1
print(cnt)