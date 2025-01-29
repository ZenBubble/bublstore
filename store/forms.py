from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'item']
        widgets = {
            'content': Textarea()
        }