from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Item, Feedback
from .forms import FeedbackForm

# Create your views here.

# Function to collect all items in the list
def item_list(request):
    items = Item.objects.all()
    return render(request, 'feedback/item_list.html', {'items':items})

# Function to calculate the average rating of an item
def item_detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    feedbacks = item.feedback_set.all()
    avg = item.average_rating()  # average_rating method from models.py

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.item = item
            fb.save()

            #redirect to avoid double POST
            return redirect(reverse('feedback:item_detail', args=[item.pk]))
    else:
        form = FeedbackForm
    
    return render(request, 'feedback/item_detail.html', {
        'item' : item,
        'feedbacks' : feedbacks,
        'average' : avg,
        'form' : form,
    })