from django.shortcuts import render,redirect
from .models import employee
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import leaveform
from .models import applyleave



# Create your views here.
@login_required(login_url='login')
def show(request):
    form = leaveform()
    data_fatch = applyleave.objects.all()
    user = User.objects.filter(username=request.user)

    if request.method == 'POST':
        form = leaveform(request.POST)
        form.save()
        return redirect(show)

    return render(request,'employee_home.html',{'rows':form,'datavalue':data_fatch})



@login_required(login_url='login')
def profile(request):
    
    return render(request,'empprofile.html')

def passwordemp(request):
    if request.method=="POST":
        user = User.objects.get(username=request.user)
        Old_password = user.password
        current_password = request.POST['curpass']
        if user.check_password(current_password):
            if(request.POST['newpass'] == request.POST['cnfpass']):
                user.set_password('password')
                redirect(show)
            else:
                return render(request,'emppass.html',{'error':'Password Dont match'})

        else:
            return render(request,'emppass.html',{'error':'Password Dont match .......'})

    else:
        return render(request,'emppass.html')
##======================================
def emp_all_leave(request):
    data_fatch = applyleave.objects.all()
    return render(request,'emp_all_leave.html',{'datavalue':data_fatchp})
    