class Solution:
    def isPalindrome(self, s: str) -> bool:
        al="abcdefghijklmnopqrstuvwxyz0123456789"
        rem_s=''
        for i in s:
            if i.lower() in al:
                rem_s=rem_s+i.lower()
        return rem_s == rem_s[-1::-1]

        