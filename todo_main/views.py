
from todos.models import Task
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user_task = Task.objects.filter(user = request.user)
    task = user_task.filter(is_completed = False).order_by('-updated_at')
    complete = user_task.filter(is_completed = True).order_by('-updated_at')
    return render(request,'home.html',{'task':task,'complete':complete})    