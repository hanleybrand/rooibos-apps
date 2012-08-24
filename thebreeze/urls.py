from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from views import main, upload


urlpatterns = patterns('',
     url(r'^$', main, name='thebreeze-main'),
     url(r'^upload/$', upload, name='thebreeze-upload'),
     url(r'^css/$', direct_to_template, {'template': 'thebreeze.css', 'mimetype': 'text/css'}, name='thebreeze-css'),
     url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.THEBREEZE_STATIC_FILES}, name='thebreeze-static'),
    )
