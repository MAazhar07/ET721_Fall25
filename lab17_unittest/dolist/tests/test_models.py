from django.test import TestCase
from dolist.models import Todolist

class TodolistModelTestCase(TestCase):
    def setUp(self):
        # create initial test data
        self.task1 = Todolist.objects.create(text="Task 1", completed=False)
        self.task2 = Todolist.objects.create(text="Task 2", completed=True)

    def test_todolist_creation(self):
        # test that Todolist instances are created correctly
        self.assertEqual(self.task1.text, "Task 1")
        self.assertFalse(self.task1.completed)
        self.assertEqual(self.task2.text, "Task 2")
        self.assertTrue(self.task2.completed)

    def test_todolist_default_completed(self):
        # test that the default value of completed is False
        new_task = Todolist.objects.create(text="New Task")
        self.assertFalse(new_task.completed)

    def test_todolist_max_length(self):
        # test that the max_length of the text field is enforced
        max_length = Todolist._meta.get_field('text').max_length
        self.assertEqual(max_length, 100)