from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        widgets = {
            'content': Textarea()
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']