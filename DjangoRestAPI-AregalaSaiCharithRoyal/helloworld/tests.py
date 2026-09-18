from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import BlogPost


class BlogPostApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="sai", password="safe-password-123")
        self.other_user = User.objects.create_user(username="other", password="safe-password-123")
        self.client.force_authenticate(self.user)

    def test_user_can_create_a_post(self):
        response = self.client.post("/api/posts/", {"title": "My first post", "content": "Hello"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["author"], "sai")

    def test_user_only_sees_own_posts(self):
        BlogPost.objects.create(title="Mine", content="Visible", author=self.user)
        BlogPost.objects.create(title="Theirs", content="Hidden", author=self.other_user)
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["title"], "Mine")

    def test_pagination_uses_five_posts_per_page(self):
        BlogPost.objects.bulk_create(
            [BlogPost(title=f"Post {number}", content="Test", author=self.user) for number in range(6)]
        )
        response = self.client.get("/api/posts/")
        self.assertEqual(response.data["count"], 6)
        self.assertEqual(len(response.data["results"]), 5)
