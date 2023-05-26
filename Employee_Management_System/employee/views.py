from django.shortcuts import render,HttpResponseRedirect

from employee.forms import EmployeeAdd, EmployeeLogin
from .models import Login
from .models import Add

# Create your views here.
def base(request):
    return render(request, 'employee/base.html')

def home(request):
    return render(request, 'employee/home.html')

def login(request):
    if request.method=='POST':
        fm=EmployeeLogin(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            pw=fm.cleaned_data['password']
            em=fm.cleaned_data['email']

            reg=Login(name=nm,password=pw,email=em)
            reg.save()
            fm=EmployeeLogin()
    else:
        fm=EmployeeLogin()



    return render(request, 'employee/login.html',{'form':fm})


def option(request):
    return render(request, 'employee/option.html')

def add(request):
    if request.method=='POST':
        fm=EmployeeAdd(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['FirstName']
            mm=fm.cleaned_data['MiddelName']
            lm=fm.cleaned_data['LastName']
            pw=fm.cleaned_data['Password']
            em=fm.cleaned_data['Email']
            ph=fm.cleaned_data['Phone']
            ad=fm.cleaned_data['Address']

            heg=Add(FirstName=nm,MiddelName=mm,LastName=lm,Password=pw,Email=em,Phone=ph,Address=ad)
            heg.save()
            fm=EmployeeAdd()
    else:
        fm=EmployeeAdd()



    return render(request, 'employee/add.html',{'form':fm})

def show_Page(request):
    stud=Add.objects.all()
    return render(request, 'employee/show.html',{'stu':stud})

def delete_info(request,id):
    if request.method=='POST':
        pi=Add.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_info(request,id):
    if request.method=='POST':
        pi=Add.objects.get(pk=id)
        fm=EmployeeAdd(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Add.objects.get(pk=id)
        fm=EmployeeAdd(instance=pi)
    return render(request, 'employee/update.html',{'form':fm})

       
