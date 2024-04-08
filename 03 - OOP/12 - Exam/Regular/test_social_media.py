from unittest import TestCase, main
from project.social_media import SocialMedia


# pylint: disable=protected-access
class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.sm = SocialMedia("elijiyqa", "Instagram", 47, "content")
        self.valid_platforms = ['Instagram', 'YouTube', 'Twitter']

        self.sm_with_posts = SocialMedia("elijiyqa", "Instagram", 47, "content")

        self.sm_with_posts.create_post("0")
        self.sm_with_posts.create_post("1")
        self.sm_with_posts.create_post("2")

    def test_init_correct_info(self) -> None:
        self.assertEqual("elijiyqa", self.sm._username)
        self.assertEqual("Instagram", self.sm._platform)
        self.assertEqual("Instagram", self.sm.platform)
        self.assertEqual(47, self.sm._followers)
        self.assertEqual("content", self.sm._content_type)
        self.assertEqual([], self.sm._posts)

    def test_valid_platforms(self) -> None:
        for platform in self.valid_platforms:
            SocialMedia("test", platform, 3, "3")
            self.sm.platform = platform

    def test_setting_wrong_platform(self) -> None:
        wrong_platform = "Injekoplqktor"

        with self.assertRaises(ValueError) as error:
            SocialMedia("test", wrong_platform, 3, "3")

        self.assertEqual(
            f"Platform should be one of {self.valid_platforms}",
            str(error.exception)
        )

        with self.assertRaises(ValueError) as error:
            self.sm.platform = wrong_platform

        self.assertEqual(
            f"Platform should be one of {self.valid_platforms}",
            str(error.exception)
        )

    def test_invalid_followers_count_raises_value_error(self) -> None:
        with self.assertRaises(ValueError) as error:
            self.sm.followers = -47

        self.assertEqual("Followers cannot be negative.", str(error.exception))
        self.assertEqual(47, self.sm.followers)

    def test_zero_followers_does_not_raise(self) -> None:
        self.sm.followers = 0
        self.assertEqual(0, self.sm.followers)

    def test_creating_post(self) -> None:
        post_content = "Test Post 1"

        result = self.sm.create_post(post_content)
        expected = (
            f"New {self.sm._content_type} post created by "
            f"{self.sm._username} on {self.sm._platform}."
        )

        self.assertEqual(expected, result)

        test_post = {'content': post_content, 'likes': 0, 'comments': []}

        self.assertListEqual([test_post], self.sm._posts)

        self.sm.create_post(post_content)
        self.assertListEqual([test_post, test_post], self.sm._posts)

    def test_like_post(self) -> None:
        valid_index = 1

        result = self.sm_with_posts.like_post(valid_index)
        expected = f"Post liked by {self.sm_with_posts._username}."

        self.assertEqual(expected, result)
        self.assertEqual(1, self.sm_with_posts._posts[valid_index]["likes"])

        for likes in range(2, 10 + 1):
            self.sm_with_posts.like_post(valid_index)
            self.assertEqual(likes, self.sm_with_posts._posts[1]["likes"])

        valid_index = 0

        result = self.sm_with_posts.like_post(valid_index)
        expected = f"Post liked by {self.sm_with_posts._username}."

        self.assertEqual(expected, result)
        self.assertEqual(1, self.sm_with_posts._posts[valid_index]["likes"])

    def test_reaching_max_likes(self) -> None:
        valid_index = 1
        self.sm_with_posts._posts[1]["likes"] = 10

        expected = "Post has reached the maximum number of likes."

        for _ in range(11):
            result = self.sm_with_posts.like_post(valid_index)
            self.assertEqual(expected, result)
            self.assertEqual(10, self.sm_with_posts._posts[1]["likes"])

    def test_like_invalid_index(self) -> None:
        invalid_index = -123

        expected = "Invalid post index."
        result = self.sm_with_posts.like_post(invalid_index)

        self.assertEqual(expected, result)

        invalid_index = len(self.sm_with_posts._posts)

        expected = "Invalid post index."
        result = self.sm_with_posts.like_post(invalid_index)

        self.assertEqual(expected, result)

    def test_comment_on_post(self) -> None:
        post_indexes = range(len(self.sm_with_posts._posts))

        for post_index in post_indexes:
            for comment in "QWERTY":
                self.sm_with_posts.comment_on_post(post_index, comment * 11)
                self.assertEqual(
                    {'user': self.sm_with_posts._username, 'comment': comment * 11},
                    self.sm_with_posts._posts[post_index]["comments"][-1]
                )

        expected = f"Comment added by {self.sm_with_posts._username} on the post."
        result = self.sm_with_posts.comment_on_post(0, "test comment test")

        self.assertEqual(expected, result)

    def test_comment_too_short(self) -> None:
        expected = "Comment should be more than 10 characters."

        for repeats in range(11):
            wrong_comment = "0" * repeats

            result = self.sm_with_posts.comment_on_post(0, wrong_comment)
            self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
