N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(1 << N):
    new_arr = []
    for j in range(N):
        if i & (1 << j):
            new_arr.append(arr[j])
            # print(arr[j], end = ",")
        # print(new_arr)
    
    arr2 = []
    if len(new_arr) == 3:
        arr2.append(new_arr)
        print(arr2)
        # maxV = 0    
        # a = sum(new_arr)
        # if maxV < a <= M:
        #     maxV = a
        #     print(maxV)
        # # S.append(a)
        # print(type(a), a, end = ' ')
    
    # maxV = 0
    # for i in S:
    #     if maxV < i <= M:
    #         maxV = i
    # print(maxV)

