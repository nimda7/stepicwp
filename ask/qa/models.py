from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        self.oder_by('added_at')

    def popular(self):
        return self.order_by('likes')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default = 1)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question', kwargs = {'id': self.id})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

