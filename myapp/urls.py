# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.get_tasks),
    path('api/tasks/create/', views.create_task),
]
