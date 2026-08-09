class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        n1 = len(n)

        if n1 == 1:
            return -1

        s = n1 - 2

        while s >= 0 and n[s] >= n[s + 1]:
            s -= 1

        if s < 0:
            return -1

        f = n1 - 1

        while n[f] <= n[s]:
            f -= 1

        n = n[:s] + n[f] + n[s + 1:f] + n[s] + n[f + 1:]

        n = n[:s + 1] + n[s + 1:][::-1]

        ans = int(n)

        return ans if ans <= 2**31 - 1 else -1