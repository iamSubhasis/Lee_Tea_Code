class Solution:
    MOD = 10**9 + 7

    def myPow(self, x, n):
        if n == 0:
            return 1

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return (half * half) % self.MOD
        else:
            return (half * half * x) % self.MOD

    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        odd = n // 2

        return (self.myPow(5, even) * self.myPow(4, odd)) % self.MOD