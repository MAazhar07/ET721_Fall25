from django.test import TestCase
from django.urls import reverse
from dolist.models import Todolist
from dolist.forms import TodolistForm
from dolist.views import addTodoitem, completedTodo, deletecompleted, deleteAll

class TodoViewsTestCase(TestCase):
    def setUp(self):
        # create initial data for testing
        self.task1 = Todolist.objects.create(text="Task 1", completed=False)
        self.task2 = Todolist.objects.create(text="Task 2", completed=False)
        self.task3 = Todolist.objects.create(text="Task 3", completed=True)

    def test_index_view(self):
        # test the index view render the correct context and template
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_todo_item_view_valid_data(self):
        # test adding a valid to-do item
        response = self.client.post(reverse('addTodoitem'), {'text': 'Task 4'})

        # should redirect to 'index'
        self.assertEqual(response.status_code, 302)

        # verify the new task was added to the list
        self.assertEqual(Todolist.objects.count(), 4)
        self.assertTrue(Todolist.objects.filter(text='Task 4').exists())

    def test_completed_todo_view_valid_id(self):
        # test adding a valid to-do item
        response = self.client.post(reverse(addTodoitem), {'text': 'New Task', 'text': 'New task 2'})

        # should redirect to 'index'
        self.assertEqual(response.status_code, 302)

        # verify a set was added
        self.assertTrue(Todolist.objects.count(), 5)

    def test_add_todo_item_invalid(self):
        # test adding an invalid to-do item (empty text)
        response = self.client.post(reverse(addTodoitem), {'text': ''})

        # should redirect to 'index'
        self.assertEqual(response.status_code, 302)

        # no new task should be added
        self.assertEqual(Todolist.objects.count(), 3)

    def test_completed_todo_valid(self):
        # test marking a valid to-do item as completed
        response = self.client.post(reverse(completedTodo, args=[self.task1.id]))

        # should redirect to 'index'
        self.assertEqual(response.status_code, 302)

        # check if task1 is marked as completed (True)
        self.task1.refresh_from_db()
        self.assertTrue(self.task1.completed)
    