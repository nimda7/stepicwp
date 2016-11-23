from django import forms
from qa.models import Question, Answer

from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
#        text = self.cleaned_data['text']
#        if not text.is_valid():
#            raise forms.ValidationError('question text is wrong', code=12)
        return self.cleaned_data

    def save(self):
        post = Question(**self.cleaned_data)
        post.save()
        return post
    

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

