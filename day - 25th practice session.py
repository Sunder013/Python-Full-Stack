#doormat
N, M = map(int, input().split())
for i in ange(1, N, 2):
    print(".|." * i).center(M, "-")
print("WELCOME").center(M, "-")
for i in range(N - 2, 0, -2):
    print(".|." * i).center(M, "-")
