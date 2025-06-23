a = [-1 for _ in range(26)]
s = input().strip()
for i, c in enumerate(s):
    if a[ord(c) - ord('a')] == -1:
        a[ord(c) - ord('a')] = i
print(*a)