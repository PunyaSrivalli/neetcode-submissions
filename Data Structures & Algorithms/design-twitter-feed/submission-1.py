from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.q = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        self.q.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        f = self.followers[userId]
        for u, t in reversed(self.q):
            if u in f or u == userId:
                feed.append(t)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
