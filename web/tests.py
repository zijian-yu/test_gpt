from django.test import TestCase
from django.urls import reverse

from .models import Post


class WebViewsTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_visible_on_home_page(self):
        post = Post.objects.create(title='第一篇文章', content='Hello Django')
        response = self.client.get(reverse('home'))
        self.assertContains(response, post.title)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
