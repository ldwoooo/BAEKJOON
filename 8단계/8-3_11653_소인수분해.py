num = int(input())

divisor = 2
prime_factor = []

while True:
    # 입력 받은 숫자가 1이 되면 즉, 소인수분해가 완료되면 반복문 멈춘다
    if num == 1:
        break

    # 숫자가 나누어 떨어지면 prime_factor(소인수리스트)에 넣고 몫의 값을 num에 할당
    elif num % divisor == 0:
        prime_factor.append(divisor)
        num = num // divisor

    # 나누어 떨어지지 않으면 나누는 값 +1
    else:
        divisor += 1

# 소인수 분해가 끝나고 소인수 값 반복 출력
for i in prime_factor:
    print(i)