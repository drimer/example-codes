from datetime import datetime

from django.test import TestCase

from blog.models import BlogPost


class BlogPostTest(TestCase):
    def test_obj_create(self):
        title = 'any title'
        body = 'any body'
        timestamp = datetime.now()
        post = BlogPost.objects.create(
            title=title,
            body=body,
            timestamp=timestamp,
		)

        self.assertEqual(post.title, title)
        self.assertEqual(post.body, body)

    def test_home(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
