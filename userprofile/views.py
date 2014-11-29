# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django import forms
from annoying.decorators import ajax_request, render_to
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import UserForm, UpForm, ChangePictureForm
from userprofile.models import Image
from posted.models import Picture, Profile
from django.template import RequestContext
from django.db.models import Q
import re

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['user__username'])
        found_entries = Picture.objects.filter(entry_query)
    return render_to_response('home.html', {'query_string': query_string, 'found_entries': found_entries[:1]}, context_instance=RequestContext(request))


def normalize_query(query_string, findterms=re.compile(r'"([^"]+)"|(\S+)').findall, normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    query = None       
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def home(request):
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("home.html", {"user": request.user})

def dashboard(request):
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("dashboard.html", {"user": request.user})

def picture(request, id):
    picture = Picture.objects.get(id=id)
    return render(request, 'picture.html', {'picture': picture})

def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    pictures = Picture.objects.filter(user=profile.user, upvotes=1)
    return render(request, 'profile.html', {'profile': profile, 'pictures': pictures})

def register(request):
    fname = lname = ""
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            newuser = User.objects.create_user(name, form.cleaned_data['email'], pw)
            newuser.first_name = fname
            newuser.last_name = lname
            newuser.save()
            newprofile = Profile.objects.create(user = newuser)
            newprofile.save()
            user = authenticate(username=name, password=pw)
            auth_login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render_to_response('register.html', {'form':form})

def login(request):
    username = password = ''
    error = False
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
  
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
        else:
            error = True
    return render_to_response('login.html', {'error': error})

def submit(request, username):
    if request.method == 'POST':
        form = UpForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(user__username=username)
            images = Picture.objects.create(user = profile.user, paths = form.cleaned_data['image'], name = form.cleaned_data['title'], time = timezone.now())
            images.save()
            return HttpResponseRedirect('/')
    else:
        form = UpForm()
    return render(request, 'dashboard.html', {'form':form})

def changePic(request):
    if (Image.objects.filter(user=request.user).count() == 1):
        images = Image.objects.get(user=request.user)
        images.delete()
    if request.method == 'POST':
        form = ChangePictureForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = Image.objects.create(user = request.user, path = form.cleaned_data['image'])
            newimg.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = ChangePictureForm()
    return render(request, 'dashboard.html', {'form':form})
  
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
