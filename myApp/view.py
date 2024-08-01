import json
import time

from django.core import serializers
from django.http import HttpResponse

from myApp.models import sabad


def sabadApi(request):
    data = serializers.serialize("json", sabad.objects.all())
    data=json.loads(data)
    list=[]
    for item in data:
        list.append(item['fields'])
    return HttpResponse(json.dumps(list),content_type='application/json')

def inc(request):
    obj=sabad()
    obj.name=request.GET['name']
    obj.count=1
    try:
        a=sabad.objects.get(name=obj.name)
        a.count=a.count+1
        a.save()
    except:
        obj.save()

    return HttpResponse(json.dumps({'msg':'ok'}),content_type='application/json')

