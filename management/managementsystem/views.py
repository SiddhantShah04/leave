from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from showdata.views import show
from .models import extendemp
from .forms import extendemp_form

# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    if request.method == "POST":
        #check if a user exists
        #with the user name and password
        uname = request.POST['username']
        pwd = request.POST['password']

        user  = auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect(show);
        else:
            return render(request,'index.html',{'error':"Invilid user name and password"})

    else:
        return render(request,'index.html')



def sin_up(request):
    form = extendemp_form()
    if request.method=="POST":
        #to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            #both password match 
            #now check if a previous user exit
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'employe.html',{'error':'User Already exits','rows':form})

            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password = request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['email'])
                new_user = extendemp(user=user)
                form = extendemp_form(request.POST,instance=user)
                form.save()
                #if you want to redirect to home of employee
                #auth.login(request,user)
                return redirect(index)

        else:
            return render(request,'employe.html',{'error':'Password Dont match','rows':form})
    else:
        return render(request,'employe.html',{'rows':form})


def logout(request):
    auth.logout(request)
    return redirect(index)