def lastStoneWeightII(stones: list[int]) -> int:
    total = sum(stones)
    target = total // 2
    
    # dp[s] = True if sum s is reachable with some subset of stones
    dp = [False] * (target + 1)
    dp[0] = True
    
    for stone in stones:
        for s in range(target, stone - 1, -1):
            dp[s] = dp[s] or dp[s - stone]
    
    # Find the largest reachable sum <= total // 2
    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s  # |group1 - group2| minimized
