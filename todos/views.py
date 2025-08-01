from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task)
            return redirect('home')  # or wherever you want to go after submission
    return HttpResponse('Form not submitted correctly')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,id=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def remove_done(request,pk):
    task = get_object_or_404(Task,id=pk)
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