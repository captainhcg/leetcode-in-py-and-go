class Solution(object):
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre_for_next = dummy_head

        def reverse_k(pre_for_next, k):
            _nd = pre_for_next.next
            for _ in xrange(k):
                if not _nd:
                    return None
                _nd = _nd.next

            tail = pre_for_next.next
            for _ in xrange(k - 1):
                to_switch = tail.next
                tail.next = to_switch.next
                to_switch.next = pre_for_next.next
                pre_for_next.next = to_switch
            return tail

        while pre_for_next:
            pre_for_next = reverse_k(pre_for_next, k)
        return dummy_head.next
