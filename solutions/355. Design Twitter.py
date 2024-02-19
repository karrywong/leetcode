from collections import defaultdict
class Twitter:
    def __init__(self):
        # follow_lookup = {} #key= userID, value = set of followee's IDs
        self.follow_lookup=defaultdict(set)
        # tweet_lookup = {} # key=userID, value = array of tweets, Tuple (timestamp, tweetID) (most recent to least)
        self.tweet_lookup=defaultdict(list)
        # timestamp, postTweet -> update tweetlookup
        self.t = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None: #O(1), M = max(# tweets per user)
        self.tweet_lookup[userId].append((-1*self.t, tweetId))
        self.t += 1
        
    def getNewsFeed(self, userId: int) -> List[int]: #O(N*log10), N= total number of tweets of user + followers'
        # getNewsFeed, loop over follow_lookup, merge k (userID + followee) list of tweets
        lst_tweets: List[Tuple[int, int]] = self.tweet_lookup[userId][:]
        for follower in self.follow_lookup[userId]:
            lst_tweets.extend(self.tweet_lookup[follower][:])
        return [tp[1] for tp in heapq.nsmallest(10, lst_tweets)]
​
    def follow(self, followerId: int, followeeId: int) -> None: #O(1)
        self.follow_lookup[followerId].add(followeeId)
​
    def unfollow(self, followerId: int, followeeId: int) -> None: #O(1)
        self.follow_lookup[followerId].discard(followeeId) 
​
# Testing
# self.follow_lookup = {1:2}
# self.tweet_lookup = {1:[(0,5)], 2:[(-1,6)]}
# getNewsFeed = [(0,5),(-1,6)]
# self.t = 2
                           
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
