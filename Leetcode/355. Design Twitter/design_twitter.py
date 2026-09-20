from heapq import heappop, heappush


class Twitter:

    def __init__(self):
        self.user_feed = {}
        self.post_counter = 1
        self.user_follower = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_feed:
            self.user_feed[userId] = []
        self.user_feed[userId].append([self.post_counter, tweetId])
        self.post_counter += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        followers = self.user_follower[userId] if userId in self.user_follower else {userId}
        heap = []
        result =[]
        for follower in followers:
            if follower in self.user_feed and self.user_feed[follower]:
                length = len(self.user_feed[follower])
                counter, tweetId = self.user_feed[follower][-1]
                heappush(heap, (-counter,follower, length-1))
        while heap:
            if len(result)==10:
                return result
            _,follower, index = heappop(heap)
            result.append(self.user_feed[follower][index][1])
            if index - 1 >=0:
                c_id, _ = self.user_feed[follower][index-1]
                heappush(heap, (-c_id, follower, index-1))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follower:
            self.user_follower[followerId] = {followerId}
        self.user_follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_follower:
            return
        self.user_follower[followerId].discard(followeeId)