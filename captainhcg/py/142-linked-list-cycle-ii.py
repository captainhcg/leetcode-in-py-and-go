class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow, fast = head, head
        while True:
            for _ in xrange(2):
                fast = fast.next
                if not fast:
                    return None
            slow = slow.next
            if slow is fast:
                break
            
        fast = head
        while slow is not fast:
            fast, slow = fast.next, slow.next

        return slow
