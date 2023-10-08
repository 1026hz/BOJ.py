N = int(input())

while (N != 0):
    name = []
    height = []

    for _ in range(N):
        n, h = map(str, input().split())

        name.append(n)
        height.append(h)

    max = sorted(height)[-1]

    for i in range(N):
        if height[i] == max:
            print(name[i], end=" ")

    print("")

    N = int(input())
