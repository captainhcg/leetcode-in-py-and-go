class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mapping = collections.defaultdict(dict)
        for (dvd, dv), val in zip(equations, values):
            mapping[dvd][dvd] = mapping[dv][dv] = 1.0
            mapping[dvd][dv] = val
            mapping[dv][dvd] = 1 / val
        for j in mapping:
            for i in mapping[j]:
                for k in mapping[j]:
                    mapping[i][k] = mapping[i][j] * mapping[j][k]
        return [mapping[dvd].get(dv, -1.0) for dvd, dv in queries]
