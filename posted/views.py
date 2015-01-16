# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from userprofile.models import Image
from posted.models import Picture, Profile, Vote, Comment
from django.http import HttpResponseRedirect, HttpResponse
import simplejson as json


@login_required
def picture(request):

    if (Image.objects.filter(user=request.user).count() != 0):
        images = Image.objects.get(user=request.user)
        imagers = [images.for_json()]
        return {"status": "OK", "imaged": imagers}
    else:
        return {"status": "NotOK"}


@login_required
def getProfile(request):
    id = request.POST.get("id")
    profile = Profile.objects.get(id=id)

    profiles = Profile.objects.get(user=profile.user)
    profilers = [profiles.for_json()]
    return {"status": "OK", "profiled": profilers}


@login_required
def load(request):

    if (Picture.objects.filter(user=request.user).count() != 0):
        pictures = Picture.objects.filter(user=request.user, upvotes=1).order_by("-id")
        picturers = [pl.for_json() for pl in pictures]
        return {"status": "YAYA", "pictured": picturers}
    else:
        return {"status": "NotYAYA"}


@login_required
def firstLook(request):

    if (Picture.objects.filter(user=request.user).count() != 0):
        pictures = Picture.objects.filter(user=request.user, upvotes=0).order_by("-id")
        picturers = [pl.for_json() for pl in pictures]
        return {"status": "YEE", "pictured": picturers}
    else:
        return {"status": "NotYEE"}


@login_required
def everyone(request):
    id = request.POST.get("id")
    picture = Picture.objects.get(id=id)

    comments = Comment.objects.filter(picture=picture)
    commenters = [pl.for_json() for pl in comments]
    return {"status": "OHYEA", "commented": commenters}


@login_required
def everyonePics(request):

    pictures = Picture.objects.filter(upvotes = 1).order_by("-id")
    picturers = [pl.for_json() for pl in pictures]
    return {"status": "OHK", "pictured": picturers}

 
@login_required
def accept(request):
    id = request.POST.get("id")
    picture = Picture.objects.get(id=id)

    upvoting = Vote.objects.filter(user=picture.user, upvoted=True, picture=picture)

    if (upvoting.count() == 0 and picture.user == request.user):

        created = Vote.objects.create(user=picture.user, upvoted=True, picture=picture)
        picture.upvotes += 1
        picture.save()
   
    return {"status": "WOO", "message": u"Accepted picture"}

 
@login_required
def reject(request):
    id = request.POST.get("id")
    picture = Picture.objects.get(id=id)

    if (picture.user == request.user):

        picture.delete()
   
    return {"status": "WOOP", "message": u"Rejected picture"}


@login_required
def delete(request):

    if (Image.objects.filter(user=request.user).count() != 0):
        images = Image.objects.get(user=request.user)
        images.delete()
        return {"status": "Deleted"}
    else:
        return {"status": "Not deleted"}
