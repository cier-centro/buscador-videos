# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    tag= models.CharField(max_length=45)
    def __unicode__(self):
        return self.tag

class Video(models.Model):
    url = models.CharField(max_length=60)
    title= models.CharField(max_length=45)
    date=models.DateField()
    lenght =models.BigIntegerField()
    tags=models.ManyToManyField(Tag)

class Subject(models.Model):
    subject= models.CharField(max_length=80)
    time = models.IntegerField()
    video = models.ForeignKey(Video, related_name='subjects', null=True, blank=False, on_delete=models.CASCADE)






