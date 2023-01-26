N = int(input())

count = 0

if 0 < N <= 100:

    # 입력 받은 숫자의 배열을 int 형태로 리스트에 담는다
    nums = list(map(int, input().split()))
    
    # 리스트에 담긴 숫자 num을 차례대로 반복
    for num in nums:
        if 0 < num <= 1000:
            prime_num = []

            # 1부터 num까지 범위를 차례대로 반복
            for i in range(1, num + 1):

                # num을 나눴을 때 나누어 떨어지면 소수 리스트에 담는다
                if num % i == 0:
                    prime_num.append(i)

            # 나눠 떨어지는 수(약수)가 2개(소수 정의)이면 counting
            if len(prime_num) == 2:
                count += 1

    print(count)
# -------------------------------------------------------------
def prime_number(num):
    arr = []

    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)
    if len(arr) == 2:
        return num

N = int(input())
nums = list(map(int, input().split()))
prime_num_list = []

for i in nums:

    result = prime_number(i)

    if result:
        prime_num_list.append(result)
        
print(len(prime_num_list))