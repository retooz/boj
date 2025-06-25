s = input().strip()
n = 1
for i in range(len(s)):
    if s[i] != s[-i-1]:
        n = 0
        break
print(n)