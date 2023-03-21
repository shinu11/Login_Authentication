
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,'index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname =    request.POST['fname']
        lname =    request.POST['lname']
        email =    request.POST['email']
        p1    =    request.POST['p1']
        p2    =    request.POST['p2']

        myuser=User.objects.create_user(username,email,p1)
        myuser.first_name=fname
        myuser.last_name=lname
        
        myuser.save()

        messages.success(request,"Your account has been succefully created")
        return redirect('signin')


    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')

def signout(request):
    return render(request,'signout.html')