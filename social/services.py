from datetime import datetime
from typing import List
from .model import FacebookPost, TwitterTweet


# External Facebook API
class FacebookApi:
    def __init__(self):
        self.posts: List[FacebookPost] = []
    def fetch_facebook_posts(
        self, user_id: int, id_: int) -> List["FacebookPost"]:
        # Implementation to fetch Facebook posts
        # Return sorted post by id
        return sorted([post for post in self.posts if post.user_id == user_id and post.id == id_],key=lambda post: post.id)

    def post_facebook_status(self, user_id: int, status: str) -> None:
        # Implementation to post a status on Facebook
        id_ = str(len(self.posts) + 1)  # Generate simple id
        timestamp = int(datetime.timestamp(datetime.now()))
        new_tweet = FacebookPost(id=id_, status=status, user_id=user_id, timestamp=timestamp)
        self.posts.append(new_tweet)


class TwitterApi:
    def __init__(self):
        self.tweets: List[TwitterTweet] = []

    def get_tweets(self, user_id: int,id:int) -> List[TwitterTweet]:
        # Return sorted tweets by id
        return sorted(
            [tweet for tweet in self.tweets if tweet.user_id == user_id and tweet.id == id],
            key=lambda tweet: tweet.id
        )

    def tweet(self, user_id: int, tweet: str) -> None:
        tweet_id = str(len(self.tweets) + 1)  # Generate simple id
        timestamp = int(datetime.timestamp(datetime.now()))
        new_tweet = TwitterTweet(id=tweet_id, tweet=tweet,text=tweet, user_id=user_id,timestamp=timestamp)
        self.tweets.append(new_tweet)