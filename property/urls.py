# -*- coding: utf-8 -*-
from django.conf.urls import *
#from rest_framework import routers
from property import views

#router = routers.DefaultRouter()
#router.register(r'property',views.PropertyViewSet)

urlpatterns = patterns('',
    url(r'^property$','property.views.index'),
    url(r'^properties/','property.views.index'),
#    url(r'^api/',include(router.urls)),
    )