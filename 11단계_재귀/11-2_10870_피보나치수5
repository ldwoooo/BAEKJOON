def fibonacci(x):
    # 기본 값 0과 1 정의
    f0 = 0
    f1 = 1
    
    if x == 0:
        return f0
    elif x == 1:
        return f1
    # 2이상일 경우 x-1의 값 + x-2의 값
    else:
        return fibonacci(x-1) + fibonacci(x-2)

print(fibonacci(int(input())))

#-----------------------------------------------------------------
n = int(input())
dp = [0,1]

for i in range(1,n):
    dp.append(dp[i]+dp[i-1])
print(dp[n])
# ----------------------------------------------------------------
def fibo(n):
    if n<=1: 
        return n
    else: 
        return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))
# ----------------------------------------------------------------
N = int(input())

a = 0
b = 1

while N > 0:
    tmp = a
    a = b
    b = b + tmp
    N -= 1
print(a)