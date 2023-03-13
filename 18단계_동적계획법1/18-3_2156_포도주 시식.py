# 계단 오르기와 같은 로직
n = int(input())
podo = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(1, n + 1):

    if i == 1:
        dp[1] = podo[1]

    elif i == 2:
        dp[2] = podo[1] + podo[2]

    # 계단 오르기와 다르게 마지막 포도주를 꼭 마실 필요가 없으므로 안마셔도 최대인지 판별
    else:
        dp[i] = max(dp[i - 2] + podo[i], dp[i - 3] + podo[i - 1] + podo[i], dp[i-1])

print(dp[-1])
