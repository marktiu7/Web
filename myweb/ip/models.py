from __future__ import unicode_literals

from django.db import models

# Create your models here.


class iptable(models.Model):
    ip = models.GenericIPAddressField()
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=100)

    def __unicode__(self):
        return self.ip
