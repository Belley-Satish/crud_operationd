from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
def registration(request):
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            mobile=form.cleaned_data.get('mobile')
            myobj=User.objects.create_user(username=username,email=email)
            myobj.mobile=mobile
            myobj.set_password(password)
            myobj.save()
            # messages.success(request,'you have succsfully registered your account')
            return redirect(login_user)
        # else:
        #     #  messages.error(request,'Please register yourself again!!')
        #      return redirect(registration)
        return render(request,'authenticate/registration.html',{'form':form})
@login_required(login_url='login_user')
def home(request):
    form=to_do_list.objects.filter(user=request.user)
    return render(request,'authenticate/home.html',{'form':form})
@csrf_exempt
def login_user(request):    
    form=loginform(request.POST)  
    if form.is_valid:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'your account is succesfully logged in!')
            return redirect(home)
        # else:
        #     messages.error(request,'invalid creditentials,Please login yourself again')
        #     return redirect(login_user)
    return render(request,'authenticate/login.html',{'form':form})
def logout_user(request):
     messages.success(request,'your account is succesfully logout')
     logout(request)
     return redirect(login_user)
@login_required(login_url='login_user')
def search(request):
     logged_in_user=request.user
     search_input=request.POST.get("search")
     form=to_do_list.objects.filter(Tittle__icontains=search_input , user=request.user) | to_do_list.objects.filter(to_do_list__icontains=search_input, user=request.user) | to_do_list.objects.filter(completed__icontains=search_input, user=request.user) 
     return render(request,'authenticate/home.html',{'form':form})

@login_required(login_url='login_user')
def create(request):
     logged_in_user=request.user
     form=to_do_list_form(request.POST or None )
     if form.is_valid():
          form.save()
          return redirect(home)
     return render(request,'authenticate/create.html',{'form':form})
@csrf_exempt
@login_required(login_url='login_user')
def update(request,id):
    data1=to_do_list.objects.filter(id=id).first()
    #  task=request.POST.get("Task")
    #  description=request.POST.get("Description")
    #  progress=request.POST.get("Progress")
    #  print(request.GET)
    #  print(id,task,description,progress)
    #  myobj=to_do_list.objects.filter(id=id).update(Tittle=task,to_do_list=description)
    #  myobj.save()
    #  print(task,description,progress)
    form=to_do_list_form(request.POST or None, instance=data1) 
    if form.is_valid():
         form.save()
         return redirect(home)
    return render(request,'authenticate/update1.html',{'form':form})
@csrf_exempt
def update1(request,id):
     form='satish'
     return render(request,'authenticate/update.html',{'form':form})

@login_required(login_url='login_user')
def delete(request,id):
    obj=to_do_list.objects.get(id=id)
    obj.delete()
    return redirect(home)
@login_required(login_url='login_user')
def completed(request):
    form=to_do_list.objects.filter(user=request.user).filter(completed='Completed')
    return render(request,'authenticate/home.html',{'form':form})

@login_required(login_url='login_user')
def InComplete(request):
    form=to_do_list.objects.filter(user=request.user).filter(completed='NotCompleted')
    return render(request,'authenticate/home.html',{'form':form})

@login_required(login_url='login_user')
def InProgress(request):
    form=to_do_list.objects.filter(user=request.user).filter(completed='InProgress')
    return render(request,'authenticate/home.html',{'form':form})
