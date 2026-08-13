class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def backtrack(openn,closen):
            if openn == closen == n:
                res.append("".join(sol))
                return
            if openn<n:
                sol.append("(")
                backtrack(openn+1,closen)
                sol.pop()
            if closen<openn:
                sol.append(")")
                backtrack(openn,closen+1)
                sol.pop()
        backtrack(0,0)
        return res
        