from django.urls import path
from . import views

urlpatterns = [
    path('adddata/',views.todo,name='adddata'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark'),
    path('remove_done/<int:pk>/',views.remove_done,name='remove_done'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('edit/<int:pk>/',views.edit,name='edit'),

]