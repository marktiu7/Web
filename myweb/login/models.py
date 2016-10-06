from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Notice(models.Model):
    title=models.CharField(max_length=100)
    time = models.DateTimeField()
    comment=models.TextField()

    def __unicode__(self):
        return self.titie


class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def Meta:
        db_name='login'
        
    def __unicode__(self):
        return self.username