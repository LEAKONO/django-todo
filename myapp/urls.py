# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/tasks/', views.get_tasks),  # List all tasks
    path('api/tasks/create/', views.create_task),  # Create a new task
    path('api/tasks/<int:pk>/', views.update_task),  # Update a task by ID
    path('api/tasks/delete/<int:pk>/', views.delete_task),  # Delete a task by ID
]
