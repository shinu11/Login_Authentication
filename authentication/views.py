
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

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

    if request.method == 'POST':
        username=request.POST['username']
        p1=request.POST['p1']

        user=authenticate(request,username=username,password=p1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'index.html',{'fname': fname})
        else:
            messages.error(request,"Bad credentials") 
            return redirect('home')

    return render(request,'signin.html')

def signout(request):
    return render(request,'signout.html')