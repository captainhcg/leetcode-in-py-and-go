class Node(object):
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.pre = None
        self.next = None

class AllOne(object):

    def __init__(self):
        self.buckets_head = Node(-1)
        self.buckets_tail = Node(-2)
        self.buckets_head.next = self.buckets_tail
        self.buckets_tail.pre = self.buckets_head
        self.keyMap = dict()
        
    def addKeyValue(self, key, value, node, left_or_right):
        if node.val != value:
            new_node = Node(value)
            if left_or_right:
                new_node.pre = node
                new_node.next = node.next
            else:
                new_node.next = node
                new_node.pre = node.pre
            new_node.pre.next, new_node.next.pre = new_node, new_node
            node = new_node
        node.keys.add(key)
        self.keyMap[key] = node

    def removeKeyValue(self, key):
        node = self.keyMap.pop(key)
        val = node.val
        node.keys.remove(key)
        if not node.keys:
            node.pre.next, node.next.pre = node.next, node.pre
        return val, node
        
    def inc(self, key):
        if key not in self.keyMap:
            self.addKeyValue(key, 1, self.buckets_head.next, False)
        else:
            value, node = self.removeKeyValue(key)
            self.addKeyValue(key, value + 1, node.next, False)

    def dec(self, key):
        if key in self.keyMap:
            value, node = self.removeKeyValue(key)
            if value > 1:
                self.addKeyValue(key, value - 1, node.pre, True)

    def getMaxKey(self):
        if not self.keyMap:
            return ""
        for v in self.buckets_tail.pre.keys:
            return v

    def getMinKey(self):
        if not self.keyMap:
            return ""
        for v in self.buckets_head.next.keys:
            return v
