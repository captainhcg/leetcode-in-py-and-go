class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.nd = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cnt = 1
        nd = self.nd
        v = nd.val
        while nd:
            if random.randint(1, cnt) == 1:
                v = nd.val
            nd = nd.next
            cnt += 1
        return v
