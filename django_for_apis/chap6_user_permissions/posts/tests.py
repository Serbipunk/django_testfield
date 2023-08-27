from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Blog title')
        self.assertEqual(actual_body, 'Body content...')
