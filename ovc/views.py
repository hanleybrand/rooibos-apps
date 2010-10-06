from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from rooibos.data.models import Collection, standardfield, FieldValue, Record
from rooibos.viewers import FULL_SUPPORT
from rooibos.viewers.viewers.videoplayer import VideoPlayer
from rooibos.migration.models import ObjectHistory



@login_required
def redirect_to_video(request, id):
    id_fields = [standardfield('identifier')]
    id_fields.extend(id_fields[0].get_equivalent_fields())
    records = Record.by_fieldvalue(id_fields, id).filter(collection__name='online-video-collection')
    if not records:
        raise Http404()
    return HttpResponseRedirect(VideoPlayer().url_for_obj(records[0]))


@login_required
def redirect_to_video_id(request, id):
    try:
        record = ObjectHistory.objects.get(content_type=ContentType.objects.get_for_model(Record),original_id=81675).content_object
    except ObjectHistory.DoesNotExist:
        raise Http404()
    return HttpResponseRedirect(VideoPlayer().url_for_obj(record))
