from django.conf.urls import * 
from shortener.views import *
urlpatterns=[
        url(r'^$',index,name='home'),
        url(r'^(?P<shortId>[-\w]{7})$',redirectOriginal,name='redirectOriginal'),
        url(r'^makeshort/$',shortenUrl,name='shortenUrl'),
       ] 
