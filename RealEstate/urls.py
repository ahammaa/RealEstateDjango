# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls import patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += (
    url(r'^admin/', include(admin.site.urls)),  # NOQA
#    url(r'^property/', 'property.views.home',name='home'),
    url(r'^properties/','property.views.index',name='index'),
    url(r'^featuredproperties/','property.views.featuredproperties',name='featuredproperties'),
    url(r'^contact/','property.views.contactus',name='contact'),
    url(r'^offer/','property.views.offer',name='offer'),
    url(r'^request/','property.views.request',name='request'),
    url(r'^requests/','property.views.requests',name='requests'),
    url(r'^propertyDetails/','property.views.propertyDetails',name='propertyDetails'),
    url(r'^', include('cms.urls')),
    url(r'^property/',include('property.urls')),
)



# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
