class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        n = collections.defaultdict(list)
        wordList.append(beginWord)
        res = 1
        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i+1:]
                n[pattern].append(word)
        print(n)
        visit = set()
        q = deque([beginWord])

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    pattern = w[:i] + "*" + w[i+1:]
                    for j in n[pattern]:
                        
                        if j in visit:
                            continue
                        
                        visit.add(j)
                        q.append(j)
            res += 1


        return 0

        