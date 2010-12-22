from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from rooibos.data.models import Collection, standardfield, FieldValue, Record
from rooibos.viewers import FULL_SUPPORT
from rooibos.viewers.viewers.mediaplayer import MediaPlayer
from rooibos.migration.models import ObjectHistory
from rooibos.statistics.models import Activity



@login_required
def redirect_to_video(request, id):
    id_fields = [standardfield('identifier')]
    id_fields.extend(id_fields[0].get_equivalent_fields())
    records = Record.by_fieldvalue(id_fields, id).filter(collection__name='online-video-collection')
    if not records:
        raise Http404()
    Activity.objects.create(event='ovc-redirect',
                            request=request,
                            content_object=records[0],
                            data=dict(id=id))
    return HttpResponseRedirect(MediaPlayer().url_for_obj(records[0]))


@login_required
def redirect_to_video_id(request, id):
    try:
        record = ObjectHistory.objects.get(content_type=ContentType.objects.get_for_model(Record),original_id=id).content_object
    except ObjectHistory.DoesNotExist:
        raise Http404()
    Activity.objects.create(event='ovc-redirect-by-id',
                            request=request,
                            content_object=record,
                            data=dict(id=id))
    return HttpResponseRedirect(MediaPlayer().url_for_obj(record))
