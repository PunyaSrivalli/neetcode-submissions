class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        if len(d.keys()) != len(d2.keys()):
            return False
        for i in d.keys():
            if i not in d2 or d[i] != d2[i]:
                return False
        return True
            