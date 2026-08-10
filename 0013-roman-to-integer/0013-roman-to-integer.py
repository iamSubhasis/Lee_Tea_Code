class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        f = 0
        su = 0

        while f < len(s):
            if f + 1 < len(s) and d[s[f+1]] > d[s[f]]:
                su += d[s[f+1]] - d[s[f]]
                f += 2
            else:
                su += d[s[f]]
                f += 1

        return su