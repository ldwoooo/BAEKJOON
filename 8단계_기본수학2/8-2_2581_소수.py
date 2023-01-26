def prime_number(num):
    # '''
    # 소수 판단 함수
    # 입력된 숫자를 2부터 본인 자신까지 나눴을 때 나눠 떨어지는 숫자(약수)를 arr 리스트에 정리한다.
    # 만약 리스트에 본인 자신인, 하나의 숫자만 들어가면(소수의 정의) 해당 숫자를 반환한다.
    # '''
    arr = []

    for i in range(2, num + 1):
        if num % i == 0:
            arr.append(i)
    if len(arr) == 1:
        return num

M = int(input())
N = int(input())
prime_num_list = []

for i in range(M, N + 1):

    # prime_number 함수를 통해 판별된 소수를 result 변수에 할당
    result = prime_number(i)

    # 만약 None 값이 아닌 숫자가 할당된다면 prime_num_list 에 배열
    if result:
        prime_num_list.append(result)

# prime_num_list에 배열 된 것이 없다면 -1 출력
if len(prime_num_list) == 0:
    print('-1')

else:
    print(sum(prime_num_list))
    print(min(prime_num_list))