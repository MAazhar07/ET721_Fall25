from django import forms

class Todolistform(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={
            'class' : 'form_control',
            'place_holder' : 'Enter to do...',
            'aria-label' : 'todo',
            'aria-describeby' : 'add-btn'
        }
    ))