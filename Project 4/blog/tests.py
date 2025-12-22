from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_post_creation(self):
        post = Post.objects.create(
            user=self.user,
            title="My Learning Journey",
            content="Today I learned Django!"
        )
        self.assertEqual(post.title, "My Learning Journey")
        self.assertEqual(post.total_likes(), 0)