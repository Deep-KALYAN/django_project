from django.test import TestCase
from .models import BlogPost, Comment

# Create your tests here.


class BlogPostTestCase(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(title="Test Post", content="Test Content")

    def test_create_blog_post(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_edit_blog_post(self):
        self.post.title = "Updated Title"
        self.post.save()
        self.assertEqual(self.post.title, "Updated Title")

    def test_delete_blog_post(self):
        self.post.delete()
        self.assertEqual(BlogPost.objects.count(), 0)