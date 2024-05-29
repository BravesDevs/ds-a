from collections import defaultdict


class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.userConnections = defaultdict(list)

    def postTweet(self, userId, tweetId):
        self.userTweets[userId].append(tweetId)

    def getNewsFeed(self, userId):
        tweets = []
        tweets.extend(self.userTweets[userId])
        for i in self.userConnections[userId]:
            tweets.extend(self.userTweets[i])
        # Sort tweets in descending order based on tweetId
        tweets.sort(reverse=True)
        return tweets[:10]  # Return the first 10 tweets

    def follow(self, followerId, followeeId):
        if followeeId not in self.userConnections[followerId]:
            self.userConnections[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.userConnections[followerId]:
            self.userConnections[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))
