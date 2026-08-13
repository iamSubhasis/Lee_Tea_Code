class Solution:
    def reverseBetween(self, h: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = h
        
        prev = dummy
        
        # move prev to node before l
        for _ in range(l - 1):
            prev = prev.next
        
        curr = prev.next
        
        # reverse r-l nodes
        for _ in range(r - l):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next