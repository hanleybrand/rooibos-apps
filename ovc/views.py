from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from rooibos.data.models import standardfield, Record
from rooibos.viewers.views import viewer_shell
from rooibos.migration.models import ObjectHistory
from rooibos.statistics.models import Activity



@login_required
def redirect_to_video(request, id):
    id_fields = [standardfield('identifier')]
    id_fields.extend(id_fields[0].get_equivalent_fields())
    records = Record.by_fieldvalue(id_fields, id).filter(
        collection__name='online-video-collection')
    if not records:
        raise Http404()
    Activity.objects.create(event='ovc-redirect',
                            request=request,
                            content_object=records[0],
                            data=dict(id=id))
    request.master_template = 'ovc_master.html'

    return viewer_shell(request, 'mediaplayer', records[0].id,
                        template='ovc_player.html')


@login_required
def redirect_to_video_id(request, id):
    try:
        record = ObjectHistory.objects.get(
            content_type=ContentType.objects.get_for_model(Record),
            original_id=id).content_object
    except ObjectHistory.DoesNotExist:
        raise Http404()
    Activity.objects.create(event='ovc-redirect-by-id',
                            request=request,
                            content_object=record,
                            data=dict(id=id))
    request.master_template = 'ovc_master.html'

    return viewer_shell(request, 'mediaplayer', record.id,
                        template='ovc_player.html')
