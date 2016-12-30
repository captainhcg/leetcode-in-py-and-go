class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return ListNode(0)
        s1 = []
        s2 = []
        
        node = l1
        while node:
            s1.append(node.val)
            node = node.next
            
        node = l2
        while node:
            s2.append(node.val)
            node = node.next
            
        lastNode = None
        carry = 0
        while s1 or s2:
            v = 0
            if s1 and s2:
                v = s1.pop() + s2.pop() + carry
            else:
                v = (s1 or s2).pop() + carry
            carry, v = divmod(v, 10)
            newNode = ListNode(v)
            newNode.next = lastNode
            lastNode = newNode
        if carry:
            newNode = ListNode(carry)
            newNode.next = lastNode
            lastNode = newNode
        return lastNode
