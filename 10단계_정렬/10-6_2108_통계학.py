N = int(input())

arr = []
for i in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

# # 평균
# average = round(sum(arr) / N)
# # 중앙값
# mid_num = arr[((N + 1) // 2) - 1]
# # 최빈값

count = 1
arr2 = []
if len(arr) == len(set(arr)):
    print(arr[1])
else:
   

    arr2.sort(key = lambda x :([1],[0]))
    print(arr2)
# print(arr[1:])
# 범위
# range_num = max(arr) - min(arr)

# print(arr)
# print(average)
# print(mid_num)
# print(range_num)