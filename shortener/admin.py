# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin
from shortener.models import Urls

class UrlsAdmin(admin.ModelAdmin):
    listDisplay=('shortId','httpUrl','timeStamp')
    order=('-timeStamp',)

admin.site.register(Urls,UrlsAdmin)


# Register your models here.
