from django.conf.urls.defaults import *
from views import redirect_to_video, redirect_to_video_id

urlpatterns = patterns('',
     url(r'^(?P<id>[-\w]+)/$', redirect_to_video, name='ovc-redirect'),
     url(r'^id/(?P<id>[\d]+)/$', redirect_to_video_id, name='ovc-redirect-id'),
    )
