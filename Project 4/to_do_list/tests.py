from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            title="Test Task",
            description="Do homework",
            category="academic",
            due_date="2025-12-31"
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.completed, False)