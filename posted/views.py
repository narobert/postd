# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from userprofile.models import Image
from annoying.decorators import ajax_request
from django.http import HttpResponseRedirect, HttpResponse
import simplejson as json


@ajax_request
@login_required
def picture(request):

    if (Image.objects.filter(user=request.user).count() != 0):
        images = Image.objects.get(user=request.user)
        imagers = [images.for_json()]
        return {"status": "OK", "imaged": imagers}
    else:
        return {"status": "NotOK"}


@ajax_request
@login_required
def delete(request):

    if (Image.objects.filter(user=request.user).count() != 0):
        images = Image.objects.get(user=request.user)
        images.delete()
        return {"status": "Deleted"}
    else:
        return {"status": "Not deleted"}
