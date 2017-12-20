# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from Serializers import VideoSerializer
from models import Video, Tag


class VideoListView(generics.ListAPIView):
    #queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def get_queryset(self):
        queryset = Video.objects.all()
        tagNames = self.request.GET.getlist('tag')

        if len(tagNames) > 0:
            tags = Tag.objects.filter(tag__in = tagNames)
            queryset = queryset.filter(tags__in=tags)
        return queryset
