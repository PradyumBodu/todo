from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task,user=request.user)
            return redirect('home')  # or wherever you want to go after submission
        else:
            return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    task.is_completed = True
    task.save()
    return redirect('home')


def remove_done(request,pk):
    task = get_object_or_404(Task,id=pk,user=request.user)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete(request,pk):
    task = get_object_or_404(Task,id=pk)
    task.delete()
    return redirect('home')


def edit(request,pk):
    get_task = get_object_or_404(Task,id = pk)

    if request.method == 'POST':
        get_task.task = request.POST.get('task')
        get_task.save()
        return redirect('home')

    return render(request,'edit.html',{'get_task':get_task})

from .forms import RagisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout

def ragister(request):
    
    if request.method == 'POST':
        form = RagisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form = RagisterForm()
    return render(request,'ragister.html',{'form':form})

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'invalid cridintioal'})
    return render(request,'login.html')

            

def logout(request):
    auth_logout(request)
    return redirect('login')