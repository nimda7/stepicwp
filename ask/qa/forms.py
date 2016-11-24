from django import forms
from qa.models import Question, Answer

from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        post = Question(**self.cleaned_data)
        post.save()
        return post


class AnswerForm(forms.Form):

    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.CharField(widget=forms.HiddenInput())
    author = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        return self.cleaned_data

    def save(self):
#        assert False, self.cleaned_data
        self.cleaned_data ['author_id'] = '1'
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
