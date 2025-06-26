cost = 0
for _ in range(int(input())):
    t, d = input().split()
    d = int(d)
    h, m = map(int, t.split(':'))
    if 7 <= h < 19 :
        if h == 18 and m + d >= 60:
            cost += (m + d - 60) * 5
            cost += (60 - m) * 10
        else :
            cost += d *10
    else :
        if h == 6 and m + d >= 60:
            cost += (m + d - 60) * 10
            cost += (60 - m) * 5
        else :
            cost += d * 5
print(cost)