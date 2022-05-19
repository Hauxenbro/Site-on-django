from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Article

class AddArt(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
            'title':forms.TextInput,
            'content':forms.Textarea,
            'category':forms.Select,
        }


class RegUserForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

class EmailForm(forms.Form):
    subject = forms.EmailField(label='Ваш e-mail:', widget=forms.EmailInput())
    content = forms.CharField(label='Текст:', widget=forms.Textarea())
    captcha = CaptchaField()
