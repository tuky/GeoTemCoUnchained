import json
import importlib
from copy import copy
from datetime import datetime, date

import six

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

GEOTEMCO = getattr(settings, 'GEOTEMCO', {})


@staff_member_required
def geotemco(request):
    data_sources = [
        {
            'title': v['verbose'],
            'url': reverse('geotemco_data_loader', kwargs={'name': k}),
        } for k, v in GEOTEMCO.get('data', {}).items()
    ]
    context = {
        'data_sources': json.dumps(data_sources),
        'title': GEOTEMCO.get('title', 'GeoTemCo'),
    }
    return render(request, 'geotemco/geotemco.html', context=context)


def import_attribute(path):
    pkg, attr = path.rsplit('.', 1)
    ret = getattr(importlib.import_module(pkg), attr)
    return ret


@staff_member_required
def data(request, name):
    data_options = GEOTEMCO.get('data', {}).get(name, {})
    if not data_options:
        raise Http404
    qs_path = data_options.get('queryset')
    if not qs_path:
        raise Http404
    queryset = import_attribute(qs_path)
    mapping = data_options.get('mapping')
    if not mapping:
        raise Http404
    db_data = queryset.values(*mapping.values())
    limit = data_options.get('query_limit')
    if limit:
        db_data = db_data[:limit]
    result = [
        {
            k: r.get(v) or u'' for k, v in mapping.items()
        } for r in db_data
    ]
    for r in result:
        if not r["lon"] or not r["lat"]:
            r["lon"] = -69.395142
            r["lat"] = 26.38695  # bermuda triangle
        for k, v in r.items():
            if isinstance(v, (datetime, date)):
                r[k] = v.isoformat()
            elif not isinstance(v, six.string_types):
                r[k] = six.text_type(v)

        r["tableContent"] = copy(r)
        del r["tableContent"]["lon"]
        del r["tableContent"]["lat"]
    return HttpResponse(
        content=json.dumps(result, indent=1), content_type='application/json')
