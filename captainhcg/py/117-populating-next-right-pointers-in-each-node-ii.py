class Solution(object):
    def connect(self, root):
        cur, next_cur, next_pre = root, None, None
        while cur:
            if cur.left and cur.right:
                cur.left.next = cur.right
            
            if not next_pre:
                next_pre = cur.left or cur.right
                next_cur = cur.right or cur.left
            elif not next_cur.next:
                next_cur.next = cur.left or cur.right
                next_cur = cur.right or cur.left or next_cur
                
            if cur.next:
                cur = cur.next
            else:
                cur = next_pre
                next_pre = None
