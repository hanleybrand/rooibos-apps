from django.conf.urls.defaults import *
from views import redirect_to_video

urlpatterns = patterns('',
     url(r'^(?P<id>[-\w]+)/$', redirect_to_video, name='ovc-redirect'),
    )
