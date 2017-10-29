from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Post


class MyLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['password'].label = ''
        self.fields['username'].widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Username',
            }
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )
        labels = {
            'title': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Title',
                }),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control editable',
                    'placeholder': 'Content',
                }),
        }