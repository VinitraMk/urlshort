# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
import random, string, json
from shortener.models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings


def index(request):
    c={}
    return render(request,'shortener/index.html',c)

def redirectOriginal(request,shortId):
    url=get_object_or_404(Urls,pk=shortId)
    url.save()
    return HttpResponseRedirect(url.httpUrl)

def shortenUrl(request):
    url=request.POST.get("url",'')
    if not (url==''):
        shortId=getShortUrl()
        b=Urls(httpUrl=url,shortId=shortId)
        b.save()

        responseData={}
        responseData['url']=settings.SITE_URL+"/"+shortId
        return HttpResponse(json.dumps(responseData),content_type="application/json")
    return HttpResponse(json.dumps({"error":"error occured"}),content_type="application/json")

def getShortUrl():
    length=7
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        shortId=''.join(random.choice(char) for x in range(length))
        try:
            temp=Urls.objects.get(pk=shortId)
        except:
            return shortId


# Create your views here.
