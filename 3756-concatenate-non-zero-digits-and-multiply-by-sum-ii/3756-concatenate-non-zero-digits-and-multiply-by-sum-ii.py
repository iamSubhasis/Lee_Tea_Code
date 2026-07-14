class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        prefixSum = [0] * (n + 1)
        prefixCnt = [0] * (n + 1)
        prefixVal = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')

            prefixSum[i + 1] = prefixSum[i] + d
            prefixCnt[i + 1] = prefixCnt[i]

            if d == 0:
                prefixVal[i + 1] = prefixVal[i]
            else:
                prefixCnt[i + 1] += 1
                prefixVal[i + 1] = (prefixVal[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            digit_sum = prefixSum[r + 1] - prefixSum[l]

            k = prefixCnt[r + 1] - prefixCnt[l]

            x = (
                prefixVal[r + 1]
                - prefixVal[l] * pow10[k]
            ) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans