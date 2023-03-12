N = int(input())
step = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(1, N + 1):

    # 계단이 1개일 때 하나만 밟음
    if i == 1:
        dp[i] = step[i]

    # 계단이 2개일 떄 최댓값은 두개 밟음
    elif i == 2:
        dp[i] = step[i - 1] + step[i]

    # 3개 이상일 때 최댓값은
    # 도착점 전 계단을 밟으면, 연속 3개는 안되므로 3개 전 계단까지의 최댓값과 본인 자신의 값
    # 도착점 전 계단을 밟지 않았으면, 2개 전 계단까지의 최댓값과 본인 자신의 합
    else:
        dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

print(dp[-1])
