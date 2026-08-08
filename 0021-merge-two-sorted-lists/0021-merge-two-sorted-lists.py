# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        c1=list1
        c2=list2
        c3= dummy

        if c1 == None:
            return c2
        elif c2 == None:
            return c1

        while c1 != None and c2 != None:
            if c1.val < c2.val :
                c3.next = c1
                c1=c1.next
            else :
                c3.next = c2
                c2=c2.next
            c3=c3.next

        if c1 == None:
            c3.next = c2
        else:
            c3.next = c1
        return dummy.next





        