n = int(input())
s = input()
a = 0
for i in range(len(s)):
    a += ((ord(s[i]) - ord('a') + 1) * 31 ** i)
print(a % 1234567891)