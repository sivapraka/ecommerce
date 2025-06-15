from abc import ABC, abstractmethod

from social.model import *
from social.services import *


class SocialMediaAdapter(ABC):
    @abstractmethod
    def post(self):
        pass
    @abstractmethod
    def get_posts(self):
        pass


class FacebookAdapter(SocialMediaAdapter):
    def __init__(self):
        self.facebook_api = FacebookApi()

    def post(self, id: int, tweet: str) -> None:
        self.facebook_api.post_facebook_status(id, tweet)

    def get_posts(self, user_id: int, id: int) -> List[SocialMediaPost]:
        posts: List[FacebookPost] = self.facebook_api.fetch_facebook_posts(user_id,id)
        result: List[SocialMediaPost] = []
        for posts in posts:
            result.append(SocialMediaPost(id=posts.id, text=posts.status, user_id=posts.user_id, timestamp=posts.timestamp))
        return result


class TwitterAdapter(SocialMediaAdapter):
    def __init__(self):
        self.twitter_api = TwitterApi()

    def post(self, id: int, tweet: str) -> None:
        self.twitter_api.tweet(id, tweet)

    def get_posts(self, user_id: int, id: int) -> List[SocialMediaPost]:
        tweets: List[TwitterTweet] = self.twitter_api.get_tweets(user_id,id)
        posts: List[SocialMediaPost] = []
        for tweet in tweets:
            posts.append(SocialMediaPost(id=tweet.id,text=tweet.tweet, user_id=tweet.user_id,timestamp=None))
        return posts
