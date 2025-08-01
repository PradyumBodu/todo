from django.urls import path
from . import views

urlpatterns = [
    path('adddata/',views.todo,name='adddata'),

]