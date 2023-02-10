N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x: (x[0], x[1]), reverse = True)

for i in range(N - 1):
    if arr[i][0] >= arr[i + 1][0]
    


print(arr)