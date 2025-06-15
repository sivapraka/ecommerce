import inspect
import unittest
from unittest.mock import MagicMock

from social.adapter import *
from social.model import *
from social.services import *


class SocialMediaAdapterTest(unittest.TestCase):
    def test_methods(self):
        adapter_class = SocialMediaAdapter
        methods = inspect.getmembers(adapter_class, predicate=inspect.isfunction)

        self.assertTrue(
            len(methods) >= 2,
            "If the adapter class is implemented correctly, there should be at least 2 methods.",
        )

        get_posts_method = sum(1 for name, _ in methods if name.startswith("get_posts"))
        post_method = sum(1 for name, _ in methods if name.startswith("post"))

        self.assertEqual(
            1,
            get_posts_method,
            "If the adapter class is implemented correctly, there should be 1 method called get_posts for getting the list of posts which accepts 2 parameters of type Long and has a return type of List.",
        )
        self.assertEqual(
            1,
            post_method,
            "If the adapter class is implemented correctly, there should be 1 method called post for posting a message which accepts 2 parameters of type Long and String and has a return type of void.",
        )

    def test_common_post_class(self):
        fields = SocialMediaPost.__annotations__
        self.assertEqual(
            len(fields),
            4,
            "If the SocialMediaPost class is implemented correctly, it should have 4 fields.",
        )

        string_count = sum(1 for field_type in fields.values() if field_type == str)
        self.assertEqual(
            string_count,
            2,
            "If the SocialMediaPost class is implemented correctly, it should have 2 fields of type String.",
        )

        long_count = sum(1 for field_type in fields.values() if field_type == int)
        self.assertEqual(
            long_count,
            2,
            "If the SocialMediaPost class is implemented correctly, it should have 2 fields of type Long.",
        )


class TestTwitterAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_twitter_api = MagicMock(spec=TwitterApi)
        self.adapter = TwitterAdapter()
        self.adapter.twitter_api = self.mock_twitter_api

    def test_get_posts(self):
        expected_tweets = [
            TwitterTweet(id="1", tweet="Tweet 1", user_id=123),
            TwitterTweet(id="2", tweet="Tweet 2", user_id=456),
        ]
        self.mock_twitter_api.get_tweets.return_value = expected_tweets

        posts = self.adapter.get_posts(123, 0)

        self.assertEqual(
            len(posts),
            2,
            "If the adapter class is implemented correctly, it should return the correct number of posts.",
        )
        self.assertEqual(
            posts[0].id,
            "1",
            "If the adapter class is implemented correctly, it should return the correct post ID.",
        )
        self.assertEqual(
            posts[0].text,
            "Tweet 1",
            "If the adapter class is implemented correctly, it should return the correct post text.",
        )
        self.assertEqual(
            posts[0].user_id,
            123,
            "If the adapter class is implemented correctly, it should return the correct user ID.",
        )
        self.assertIsNone(
            posts[0].timestamp,
            "If the adapter class is implemented correctly, it should return None for timestamp.",
        )
        self.assertEqual(
            posts[1].id,
            "2",
            "If the adapter class is implemented correctly, it should return the correct post ID.",
        )
        self.assertEqual(
            posts[1].text,
            "Tweet 2",
            "If the adapter class is implemented correctly, it should return the correct post text.",
        )
        self.assertEqual(
            posts[1].user_id,
            456,
            "If the adapter class is implemented correctly, it should return the correct user ID.",
        )
        self.assertIsNone(
            posts[1].timestamp,
            "If the adapter class is implemented correctly, it should return None for timestamp.",
        )

    def test_post(self):
        self.adapter.post(123, "Hello Twitter!")
        self.mock_twitter_api.tweet.assert_called_once_with(
            123,
            "Hello Twitter!",
        )


class TestFacebookAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_facebook_api = MagicMock(spec=FacebookApi)
        self.adapter = FacebookAdapter()
        self.adapter.facebook_api = self.mock_facebook_api

    def test_get_posts(self):
        expected_posts = [
            FacebookPost(id="1", status="Post 1", user_id=123, timestamp=123456),
            FacebookPost(id="2", status="Post 2", user_id=456, timestamp=789012),
        ]
        self.mock_facebook_api.fetch_facebook_posts.return_value = expected_posts

        posts = self.adapter.get_posts(123, 0)

        self.assertEqual(
            len(posts),
            2,
            "If the adapter class is implemented correctly, it should return the correct number of posts.",
        )
        self.assertEqual(
            posts[0].id,
            "1",
            "If the adapter class is implemented correctly, it should return the correct post ID.",
        )
        self.assertEqual(
            posts[0].text,
            "Post 1",
            "If the adapter class is implemented correctly, it should return the correct post text.",
        )
        self.assertEqual(
            posts[0].user_id,
            123,
            "If the adapter class is implemented correctly, it should return the correct user ID.",
        )
        self.assertEqual(
            posts[0].timestamp,
            123456,
            "If the adapter class is implemented correctly, it should return the correct timestamp.",
        )
        self.assertEqual(
            posts[1].id,
            "2",
            "If the adapter class is implemented correctly, it should return the correct post ID.",
        )
        self.assertEqual(
            posts[1].text,
            "Post 2",
            "If the adapter class is implemented correctly, it should return the correct post text.",
        )
        self.assertEqual(
            posts[1].user_id,
            456,
            "If the adapter class is implemented correctly, it should return the correct user ID.",
        )
        self.assertEqual(
            posts[1].timestamp,
            789012,
            "If the adapter class is implemented correctly, it should return the correct timestamp.",
        )

    def test_post(self):
        self.adapter.post(123, "Hello Facebook!")
        self.mock_facebook_api.post_facebook_status.assert_called_once_with(
            123,
            "Hello Facebook!",
        )


if __name__ == "__main__":
    unittest.main()
