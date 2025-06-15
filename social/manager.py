from typing import List
from .model import FacebookPost, TwitterTweet
from .services import FacebookApi, TwitterApi


class SocialMediaManager:
    def __init__(self):
        self.facebook_api = FacebookApi()
        self.twitter_api = TwitterApi()

    def get_messages(self, user_id: int, timestamp: int, platform: str):
        if platform == "facebook":
            posts: List[FacebookPost] = self.facebook_api.fetch_facebook_posts(
                user_id, timestamp
            )
        elif platform == "twitter":
            tweets: List[TwitterTweet] = get_tweets(user_id)
        else:
            raise ValueError("Invalid platform specified")
