class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
            
        queue = [0]
        visited = set([0])
        nc = 0
        
        while queue:
            nc += 1
            length = len(queue)
            for _ in xrange(length):
                v = queue.pop(0)
                for coin in coins:
                    new_v = v + coin
                    if new_v == amount:
                        return nc
                    elif new_v > amount:
                        continue
                    elif new_v not in visited:
                        visited.add(new_v)
                        queue.append(new_v)
                        
        return -1
