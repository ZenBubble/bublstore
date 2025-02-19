from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea, PasswordInput
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        widgets = {
            'title': Textarea(attrs={'class': 'rounded-xl bg-accent h-full w-full','style':'resize:none;'}),
            'content': Textarea(attrs={'class': 'rounded-xl bg-accent h-full w-full','style':'resize:none;'})
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': PasswordInput()
        }