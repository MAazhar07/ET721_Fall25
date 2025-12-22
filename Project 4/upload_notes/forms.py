from django import forms
from .models import NoteImage

class NoteImageForm(forms.ModelForm):
    class Meta:
        model = NoteImage
        fields = ['title', 'subject', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Math Notes - Chapter 3'}),
        }