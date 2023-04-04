from datetime import timezone

from django import forms
from .models import User, Vote,Poll,Choice


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

class PollForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Poll
        fields = ['title', 'description','pub_date','end_date']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['poll','choices']
