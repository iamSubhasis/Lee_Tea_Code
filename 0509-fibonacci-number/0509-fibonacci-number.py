
class Solution:
    
    def fib(self, n: int) -> int:
        if n <=1:
            return n 
        return self.fib(n-1) + self.fib(n-2)
#problem ..runs in O(n2) .. need to add a sequence to lower the tc . 

        