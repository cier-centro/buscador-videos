# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tag(models.Model):
    tag= models.CharField(max_length=45)

class Subject(models.Model):
    subject= models.CharField(max_length=80)
    time = models.IntegerField()


class Video(models.Model):
    url = models.CharField(max_length=60)
    nick = models.CharField(max_length=45)
    tittle= models.CharField(max_length=45)
    date=models.DateField()
    timr =models.BigIntegerField()
    subject=models.ForeignKey(Subject, null=True, blank=False, on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag)




