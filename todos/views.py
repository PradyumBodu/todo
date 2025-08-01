from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task)
            return redirect('home')  # or wherever you want to go after submission
    return HttpResponse('Form not submitted correctly')