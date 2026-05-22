from django.apps import AppConfig


class FeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'feedback'
student@410c4c0e479a:/projects/corpweb/feedback$ cat models.py 
from django.db import models

class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    date = models.DateField()
    feedback = models.CharField(max_length=1000, blank=True, default='')

class Meta:
    ordering = ['created']