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
from userprofile.models import Image
from .forms import UserForm

def home(request):
    images = Image.objects.all()
    if not request.user.is_authenticated():
        return render_to_response("register.html")
    return render_to_response("dashboard.html", {"user": request.user, "images": images})

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
            newimg = Image.objects.create(user = newuser, path = form.cleaned_data['image'])
            newimg.save()
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
  
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')
