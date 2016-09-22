# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        hashmap = {}
        curr = head
        while curr:
            copy = RandomListNode(curr.label)
            hashmap[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
            
        return hashmap[head]
