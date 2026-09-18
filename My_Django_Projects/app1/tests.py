from django.test import TestCase
from django.urls import reverse


class BlogViewTests(TestCase):
    def test_blogs_page_displays_welcome_message(self):
        response = self.client.get(reverse("blogs"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to my blog")
