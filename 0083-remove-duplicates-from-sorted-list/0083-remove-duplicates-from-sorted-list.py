# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        p1 = head
        while p1 != None and p1.next != None:
            if p1.next.val == p1.val :
                p1.next = p1.next.next
            else:
                p1 = p1.next
        return head

        