from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rooibos.data.models import Collection, standardfield, FieldValue, Record
from rooibos.viewers import FULL_SUPPORT
from rooibos.viewers.viewers.videoplayer import VideoPlayer

@login_required
def redirect_to_video(request, id):
    collection = get_object_or_404(Collection, name='online-video-collection')
    records = Record.by_fieldvalue(standardfield('identifier'), id)
    if not records:
        raise Http404()
    return HttpResponseRedirect(VideoPlayer().url_for_obj(records[0]))
