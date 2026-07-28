class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            d[n] = 1 + d.get(n,0)
        
        for n,c in d.items():
            freq[c].append(n)
        print(freq)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                print(res)
                if len(res) == k:
                    return res