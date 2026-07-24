class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())

        rem_s = "".join(chars)
        return rem_s == rem_s[::-1]