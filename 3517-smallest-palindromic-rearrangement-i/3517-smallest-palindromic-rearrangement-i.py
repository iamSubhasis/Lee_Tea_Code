class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        for i in range(26):
            ch = chr(i + ord('a'))

            if count[i] % 2 == 1:
                middle = ch

            left.append(ch * (count[i] // 2))

        left = "".join(left)

        return left + middle + left[::-1]