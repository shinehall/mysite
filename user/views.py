from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login_get(request):
    return render(request, 'user/login.html', {})


def user_login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    print('get username : %s , get password : %s' % (username, password))
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'user/profile.html', {'user': user})
    else:
        return render(request, 'user/profile.html', {'error_message': 'no such user exist!'})


@login_required
def user_profile(request):
    return render(request, 'user/profile.html', {'user': request.user})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:user_login_get'))
