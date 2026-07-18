class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d0 = {}

        for i in s:
            d[i] = d.get(i, 0) + 1

        for i in t:
            d0[i] = d0.get(i, 0) + 1

        return d == d0