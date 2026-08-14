class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 0
        mark = [0] * 26
        l = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('a')
            mark[idx] += 1

            while mark[idx] > 2:
                mark[ord(s[l]) - ord('a')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res