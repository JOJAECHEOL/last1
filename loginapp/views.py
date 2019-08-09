from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import auth
from .models import Member
from django.db.models import Q
from backapp.models import Goods

    # Create your views here.
    
def about(request):
    return render(request, 'about.html')

def main(request):
    return render(request, 'main.html')

def signup(request):
    member = Member()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            member.title = request.POST['username']
            member.pw = request.POST['password1']
            member.choose = request.POST['choose']
            member.save()
            return redirect('login')
    return render(request, 'signup.html')
    
    
def login(request):
    goods = Goods.objects
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            mem = Member.objects.get(title__exact=username, pw__exact=password)
        except Member.DoesNotExist as e:
            error = 'username or password is incorrcet'
            mem = None
        if mem is not None:
            return render(request, 'main.html', {'mem': mem, 'goodss':goods})

        else:
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        return redirect('')
    return render(request, 'main.html')

def good(request):
    return render(request, 'good.html')