from django.urls import path
from . import views

urlpatterns = [
    # load page of the app will be sent to the index.html
    path('', views.index, name='index'),
    path('add', views.addTodoitem, name='add'),
    
    # add a path of the completed items in our list to our database
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    
    # delete tasks that are marked as completed
    path('deletecompleted', views.deletecompleted, name='deletecompleted'),
    
    # delete all tasks
    path('deleteall', views.deleteAll, name='deleteall'),
]