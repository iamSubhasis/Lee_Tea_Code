# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        rev = self.reverse(slow)
        while rev:
            if head.val != rev.val:
                return False
            else:
                head = head.next
                rev= rev.next
        return True
    
    def reverse(self,head: Optional[Listnode]):
        curr  = head 
        prev= None
        while curr :
            next_temp = curr.next
            curr.next= prev
            prev= curr
            curr= next_temp
        return prev


        