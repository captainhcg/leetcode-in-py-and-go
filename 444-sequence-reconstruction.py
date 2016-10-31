class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        from collections import deque
        nodes = dict()
        max_num = 0
        for seq in seqs:
            if not seq:
                continue

            pre = None
            for num in seq:
                if num < 1:
                    return False
                max_num = max(max_num, num)
                if num not in nodes:
                    nodes[num] = {"in": set(), "out": set()}
                if pre is not None:
                    nodes[pre]["out"].add(num)
                    nodes[num]["in"].add(pre)
                pre = num

        q = deque()
        for v, nd in nodes.iteritems():
            if not nd["in"]:
                q.append(v)

        arr = []
        while q:
            if len(q) != 1:
                return False
            v = q.popleft()
            arr.append(v)
            for next_to in nodes[v]["out"]:
                nodes[next_to]["in"].remove(v)
                if not nodes[next_to]["in"]:
                    q.append(next_to)

        return len(arr) == max_num and arr == org
