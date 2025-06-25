s = input().strip().upper()
cnt = [0] * 26
for c in s:
    cnt[ord(c) - ord('A')] += 1
max_count = max(cnt)
if cnt.count(max_count) > 1:
    print("?")
else:
    print(chr(cnt.index(max_count) + ord('A')))