class Solution(object):
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict
        mat = defaultdict(dict)
        for (st, ed), v in zip(equations, values):
            mat[st][ed], mat[ed][st] = v, 1.0 / v

        def dfs(st, mid):
            eds = mat.get(mid) or []
            for ed in eds:
                if mat[st].get(ed) is not None:
                    continue
                mat[st][ed], mat[ed][st] = mat[st][mid] / mat[ed][mid], mat[ed][mid] / mat[st][mid]
                dfs(st, ed)

        for st in mat.keys():
            for ed in tuple(mat[st]):
                dfs(st, ed)

        return [mat[st].get(ed, -1.0) for (st, ed) in queries]
