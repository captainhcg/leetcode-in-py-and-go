class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        arr = [{'i': idx, 'n': p[1]} for idx, p in enumerate(people)]
        ret = []
        for p in arr:
            ret.insert(p['n'], p)
        return [people[p['i']] for p in ret]
