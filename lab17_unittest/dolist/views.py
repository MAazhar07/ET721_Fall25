from django.shortcuts import render, redirect
from . models import Todolist
from .forms import Todolistform
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    form = Todolistform()
    context = {'todo_tasks' : todo_tasks, 'form':form}
    return render(request, 'index.html', context)

@require_POST
def addTodoitem(request):
    form = Todolistform(request.POST)
    
    # capture data from the form when the Add to list button is pressed
    if form.is_valid():
        text = form.cleaned_data['text']
        Todolist.objects.create(text=text)


    return redirect('index')

# function to select an item as completed
def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

# function to delete all items that are marked as 'completed'
def deletecompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

# function to delete all tasks in our list
def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')