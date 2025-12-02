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
        form.save()


    return redirect('index')