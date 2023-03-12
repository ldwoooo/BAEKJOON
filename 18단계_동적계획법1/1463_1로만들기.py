N = int(input())

dp = [0] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    # 6으로 나누어 떨어지면(2와 3으로 나누어 떨어지면)
    # 2로 나눈 몫의 dp 값, 3으로 나눈 몫의 dp 값, 1을 뺸 값의 dp 값의 최솟값 + 1
    if i % 6 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3], dp[i - 1]) + 1

    # 2로 나누어 떨어지면 2로 나눈 몫의 dp 값, 1을 뺸 값의 dp 값의 최솟값 + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1

    # 3으로 나누어 떨어지면 2로 나눈 몫의 dp 값, 1을 뺸 값의 dp 값의 최솟값 + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1

    # 나누어 떨어지지 않으면 1을 뺀 값 + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[-1])
