class Solution:
    def countSubstrings(self, s: str) -> int:
        res = set()
        reslen = 0
        for i in range(len(s)):
            #odd length
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res.add(s[l:r-l+1])
                reslen += 1
                l -= 1
                r += 1
            #even length
            l,r = i, i+1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                res.add(s[l:r-l+1])
                reslen += 1
                l -= 1
                r += 1
        return reslen