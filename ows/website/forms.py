from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import worlds


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=32, help_text='Required', label="Email Address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")        

from django.contrib.auth.forms import PasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'your class',
        'placeholder': 'your placeholder',
        'type': 'email',
        'name': 'email'
        }))

class worldsForm(forms.ModelForm):
    class Meta:
        model = worlds.Worlds
        fields = [
            "name",
            "slug",
            "description",
        ]