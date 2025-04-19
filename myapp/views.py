# myapp/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status

# Get all tasks
@api_view(['GET'])
def get_tasks(request):
    tasks = Todo.objects.all()
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)

# Create a new task
@api_view(['POST'])
def create_task(request):
    print("POST received:", request.data)
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update a task by ID
@api_view(['PUT'])
def update_task(request, pk):
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete a task by ID
@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
