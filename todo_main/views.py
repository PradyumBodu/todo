
from todos.models import Task
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    task = Task.objects.filter(is_completed = False).order_by('-updated_at')
    return render(request,'home.html',{'task':task})