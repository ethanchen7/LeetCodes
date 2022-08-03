class Twitter:

    def __init__(self):
        self.users = collections.defaultdict(set) # track the follows
        self.tweets = collections.defaultdict(list) # track each user's tweets
        self.time = 0
        # {1: {1, 2}, }
        # {1: [(-1, 5), (-2, 3), (-3, 101), (-4, 13), (-5, 10), (-6, 2), (-7, 94), (-8, 505), (-9, 333), (-10, 22), (-11, 11)], 2: [(-2, 6)]}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.users[userId] # return the set of people that user follows
        following.add(userId) # add own userId to the set to check for own tweets
        
        res = []
        tweets = []
        for f in following: # O(F) f = number of followers
            tweets += self.tweets[f]
        
        k = 10 # get top 10
        heapify(tweets) # O(N)
        while tweets and k > 0:
            time, tweetId = heappop(tweets) # O(log N)
            res.append(tweetId)
            k -= 1

        return res # Overall: O(N) N = tweets by all of users followers

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user_set = self.users[followerId]
        if followeeId in user_set:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)