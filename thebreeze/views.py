from __future__ import with_statement
from django.shortcuts import render_to_response
from django.template import RequestContext
from rooibos.data.models import Collection, FieldValue, standardfield
from rooibos.pdfviewer.viewers import pdfviewer
import random


def main(request):
    collection = Collection.objects.get(name='the-breeze')

    coverage = standardfield('coverage')
    date = standardfield('date')

    volumes = sorted(map(int, FieldValue.objects.filter(
        record__collection=collection,
        field=coverage,
        label='Volume',
        ).values_list('value', flat=True).distinct()))

    try:
        volume = int(request.GET.get('v'))
    except (ValueError, TypeError):
        volume = None
    if not volume in volumes:
        volume = volumes[0]


    record_ids = FieldValue.objects.filter(
        record__collection=collection,
        field=coverage,
        label='Volume',
        value=str(volume),
        ).values_list('record', flat=True)


    issues = sorted(FieldValue.objects.filter(
        record__in=record_ids,
        field=coverage,
        label='Issue',
        ).values_list('record', 'value'))

    dates = sorted(FieldValue.objects.filter(
        record__in=record_ids,
        field=date,
        ).values_list('record', 'value'))


    combined = sorted((int(i[1]), d[1], i[0]) for i, d in zip(issues, dates))


    try:
        record_id = int(request.GET.get('r'))
    except (ValueError, TypeError):
        record_id = None
    if not record_id in (r for i, d, r in combined):
        record_id = combined[0][2]

    for i, d, r in combined:
        if record_id == r:
            issue = i
            break

    viewer = pdfviewer(None, request, record_id)


    return render_to_response('thebreeze.html',
                              {'collection': collection,
                               'breezelogo': 'breeze_logo_%s.png' %
                                    random.choice('00 01 02 03 04'.split()),
                               'volume': volume,
                               'volumes': volumes,
                               'issue': issue,
                               'issues': combined,
                               'record': record_id,
                               'viewer': viewer,
                               'embedcode': viewer.embed_code(request, None),
                               },
                              context_instance=RequestContext(request))
