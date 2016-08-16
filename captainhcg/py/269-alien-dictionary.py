import collections
class Solution(object):
    def alienOrder(self, words):
        all_chars = set()
        for word in words:
            for ch in word:
                all_chars.add(ch)
        pre = collections.defaultdict(set)
        post = collections.defaultdict(set)
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    pre[c1].add(c2)
                    post[c2].add(c1)
                    break
        queue = collections.deque(all_chars - set(post.keys()))
        arr = []
        while queue:
            head = queue.popleft()
            arr.append(head)
            while pre[head]:
                next_ch = pre[head].pop()
                post[next_ch].remove(head)
                if not post[next_ch]:
                    del post[next_ch]
                    queue.append(next_ch)
        return "".join(arr) if len(arr) == len(all_chars) else ""
