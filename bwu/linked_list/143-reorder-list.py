class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        middle = self.findMiddle(head)
        new_head = self.reverse(middle.next)
        middle.next = None
        self.merge(head, new_head)
        return
        
        
    def findMiddle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        
    def reverse(self, head):
        tail = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = tail
            tail = curr
            curr = tmp
        return tail
    
    def merge(self, head1, head2):
        while head2:
            tmp = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = tmp
