from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea, PasswordInput, TextInput
from .models import Order, Review

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
        widgets = {
            'username': TextInput(attrs={'class': 'rounded-xl bg-accent w-2/3'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'rounded-xl bg-accent w-2/3'})
        self.fields['password2'].widget.attrs.update({'class': 'rounded-xl bg-accent w-2/3'})

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'rounded-xl bg-accent w-2/3'}),
            'password': PasswordInput(attrs={'class': 'rounded-xl bg-accent w-2/3'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['details']
        widgets = {
            'details': Textarea(attrs={'class': 'rounded-xl bg-accent h-full w-full align-text-top','style':'resize:none;','placeholder':'Enter in additional information about your order, such as what type of video, how to contact you, etc.'}),
        }