# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import Video, Tag, Subject

class SubjectInline(admin.TabularInline):
    model = Subject

class VideoAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)

