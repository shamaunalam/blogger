from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd   = request.POST['password']

        user = authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('index')
    else:
        if request.user.is_anonymous:
            return render(request,'index.html')
        else:
            return redirect('home')


@login_required(login_url='index')
def home(request):
    return render(request,'home.html')

@login_required(login_url='index')
def article(request):
    return render(request,'article.html')


def signout(request):

    logout(request)

    return redirect('index')

def register(request):

    if request.method=='POST':

        uname = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']

        user = User.objects.create(username=uname,email=email)
        user.set_password(pwd)
        user.save()
        return redirect('index')