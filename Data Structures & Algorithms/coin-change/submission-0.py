class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [amount + 1] * (amount + 1)
        ans[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    ans[a] = min(ans[a], 1 + ans[a - c])

        return ans[amount] if ans[amount] != amount + 1 else -1
        
