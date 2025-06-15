from dataclasses import dataclass
from typing import Optional


@dataclass
class SocialMediaPost:
  id: str
  text: str
  user_id: int
  timestamp: int


@dataclass
class FacebookPost:
    id: str
    status: str
    user_id: int
    timestamp: int


@dataclass
class TwitterTweet:
    id: str= Optional[None]
    tweet: str= Optional[None]
    user_id: int =Optional[None]
    text: str = Optional[None]
    timestamp: int=Optional[None]
