def solution(money):
    dp = [[0] * 1_000_000 for _ in range(2)]
    # 0 = 0번 선택, 1 = 1번 선택
    dp[0][0], dp[0][1] = money[0], money[0]
    dp[1][0], dp[1][1] = 0, money[1]
    for i in range(2, len(money)):
        for k in range(2):
            dp[k][i] = max(dp[k][i-1], money[i] + dp[k][i-2])
    return max(dp[0][len(money)-2], dp[1][len(money)-1])