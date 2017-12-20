# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from apps.video.models import Video,Tag,Subject

admin.site.register(Video)
admin.site.register(Tag)
admin.site.register(Subject)