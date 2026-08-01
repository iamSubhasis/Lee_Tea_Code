class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        l = 1
        fast = slow.next
        while fast != slow:
            fast = fast.next
            l += 1
        slow = head
        fast = head

        for _ in range(l):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow