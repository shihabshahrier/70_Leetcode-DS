class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float("inf") for i in range(amount + 1)]
        memo[0] = 0
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    c = memo[i - coins[j]]
                    if (c != float("inf") and c + 1 < memo[i]):
                        memo[i] = c + 1
        if memo[amount] == float("inf"):
            return -1
        return memo[amount]

            