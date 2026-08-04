class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        h = []
        for i in points:
            x,y = i[0],i[1]
            dis = (x)**2+(y)**2
            heapq.heappush(h,[dis,x,y])
        res = []   
        #print(h)
        while k > 0:
            dis,x,y = heapq.heappop(h)
            res.append([x,y])
            k -= 1
        return res
        