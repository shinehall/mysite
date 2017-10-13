from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login

# Create your views here.
def user_login_get(request):
    return render(request, 'user/login.html', {})


def user_login_post(request):
    print('get request!')
    username = request.POST['username']
    password = request.POST['password']
    print('get username : %s , get password : %s' % (username, password))
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('get login request')
    else:
        return HttpResponse('no such user exist!')