# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        
        heapq.heapify(heap)
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return dummy.next
