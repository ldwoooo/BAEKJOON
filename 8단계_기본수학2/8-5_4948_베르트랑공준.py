arr2 = []

while True:
    nums = int(input())

    if nums == 0:
        break

    elif nums == 1:
        arr2.append(nums)

    else:
        count = 0

        for num in range(nums + 1, nums * 2):
            arr = []
            
            for i in range(2, num):
                if num % i == 0:
                    arr.append(num)
                    break

            if len(arr) == 0:
                count += 1
        arr2.append(count)

for j in arr2:
    print(j)