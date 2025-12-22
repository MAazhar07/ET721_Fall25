from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NoteImage
from .forms import NoteImageForm

@login_required
def note_list(request):
    notes = NoteImage.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'upload_notes/note_list.html', {'notes': notes})

@login_required
def note_upload(request):
    if request.method == 'POST':
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteImageForm()
    return render(request, 'upload_notes/note_form.html', {'form': form})

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(NoteImage, id=note_id, user=request.user)
    return render(request, 'upload_notes/note_detail.html', {'note': note})