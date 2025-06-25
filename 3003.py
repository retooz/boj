chess = [i for i in map(int, input().split())]
chess_standard = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(chess_standard[i] - chess[i], end=' ')
