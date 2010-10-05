from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rooibos.data.models import Collection, standardfield, FieldValue, Record
from rooibos.viewers import FULL_SUPPORT
from rooibos.viewers.viewers.videoplayer import VideoPlayer

@login_required
def redirect_to_video(request, id):
    id_fields = [standardfield('identifier')]
    id_fields.extend(id_fields[0].get_equivalent_fields())
    records = Record.by_fieldvalue(id_fields, id).filter(collection__name='online-video-collection')
    if not records:
        raise Http404()
    return HttpResponseRedirect(VideoPlayer().url_for_obj(records[0]))
