arr = [input() for _ in range(5)]

ans = ''
for j in range(15):
    for i in range(5):
        if len(arr[i]) <= j:
            continue
        ans += arr[i][j]

print(ans)
