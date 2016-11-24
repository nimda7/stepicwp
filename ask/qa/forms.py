from django import forms
from qa.models import Question, Answer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        post = Question(**self.cleaned_data)
        post.save()
        return post


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean(self):
        self._user = self.cleaned_data['username']
        self._pass = self.cleaned_data['password']
        self._email = self.cleaned_data['email']
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(self._user, self._email, self._pass)
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean(self):
        return self.cleaned_data

