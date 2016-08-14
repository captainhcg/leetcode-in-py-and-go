import heapq
class Solution(object):
    def mergeKLists(self, lists):
        h = []
        [heapq.heappush(h, (l.val, l)) for l in lists if l]
        dummy = ListNode(-1)
        pre = dummy
        while h:
            (_, nd) = heapq.heappop(h)
            pre.next = nd
            pre = nd
            if nd.next:
                heapq.heappush(h, (nd.next.val, nd.next))
        return dummy.next
