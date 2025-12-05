from django.test import TestCase
from django.urls import reverse, resolve
from dolist.views import index, addTodoitem, completedTodo
from dolist.models import Todolist

class TestUrls(TestCase):
    
    def test_index_url(self):
        # test that the index URL resolves to the correct view
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_add_url(self):
        # test that the add URL resolves to the correct view

        url = reverse('add')
        self.assertEqual(resolve(url).func, addTodoitem)

    def test_completed_url(self):
        # test that the completed URL resolves to the correct view

        # example, todo_id = 1
        url = reverse("completed", args=[1])

        # ensure that URL is correctly mapped to the completedTodo view
        self.assertEqual(resolve(url).func, completedTodo)

    def test_urls_status_code(self):
        # test that urls return the correct status codes
        
        # test the index url
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
        # test add url (should be accessible via POST)
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 405)
        
        # test the completed url with valid todo_id (should redirect)
        # example, assuming 1 is a valid todo_id