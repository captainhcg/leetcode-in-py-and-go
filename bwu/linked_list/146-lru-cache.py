class DoublyLinkedListNode(object):
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoublyLinkedListNode()
        self.tail = DoublyLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def kick(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.toTail(node)
        
    def toTail(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
    
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hashmap:
            self.kick(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1
        

    def popOldest(self):
        del self.hashmap[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.hashmap:
            node = DoublyLinkedListNode(key, value)
            
            if self.capacity == 0:
                self.popOldest()
                self.capacity += 1
                
            self.toTail(node)
            self.hashmap[key] = node
            self.capacity -= 1
        else:
            node = self.hashmap[key]
            node.val = value
            self.kick(node)
        
