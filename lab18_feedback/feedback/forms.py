from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your feedback...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    # method to collect the rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating in None:
            raise forms.ValidationError("Rating is required")
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5")
        return rating

    # method to collect the comments
    def clean_comment(self):
        comment = self.cleaned_data.get('comment', '').strip()
        if not comment:
            raise forms.ValidationError("Comment cannot be empty!")
        return comment