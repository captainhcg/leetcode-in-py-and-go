import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        edges = collections.defaultdict(set)
        in_degrees = collections.defaultdict(set)
        chars = set([i for word in words for i in word])
        for i in xrange(1, n):
            prev_word = words[i - 1]
            word = words[i]
            for idx in xrange(min(len(prev_word), len(word))):
                if prev_word[idx] == word[idx]:
                    if idx + 1 < len(prev_word) and idx + 1 == len(word):
                        return ''
                    continue
                else:
                    edges[prev_word[idx]].add(word[idx])
                    in_degrees[word[idx]].add(prev_word[idx])
                    break
               
        res = []
        queue = []
        for ch in chars:
            if ch not in in_degrees:
                queue.append(ch)
            
        while queue:
            curr = queue.pop(0)
            res.append(curr)
            if curr in edges:
                for n in edges[curr]:
                    in_degrees[n].discard(curr)
                    if len(in_degrees[n]) == 0:
                        queue.append(n)
                        del in_degrees[n]
        
        if in_degrees:
            return ''
                
        return ''.join(res)
