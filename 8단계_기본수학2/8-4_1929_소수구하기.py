M, N = map(int, input().split())

for num in range(M, N + 1):
    arr = []

    for i in range(2, num):
        if num % i == 0:
            arr.append(num)
            break

    if len(arr) == 0:
            print(num)

            # 제발