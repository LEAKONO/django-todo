from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Todo
from .serializers import TodoSerializer

# ----------------------------
# ✅ Signup View (Standalone)
# ----------------------------
@api_view(['POST'])
def signup(request):
    """
    User signup endpoint for creating a new user.
    Expects a JSON body with 'username' and 'password'.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if both fields are provided
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the user
    user = User.objects.create(
        username=username,
        password=make_password(password)
    )
    return Response({'message': 'User created successfully', 'user': {'username': user.username}}, status=status.HTTP_201_CREATED)

# ----------------------------
# 🔄 TodoViewSet (CRUD Actions for Todos)
# ----------------------------
class TodoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Todo items.
    """
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns a queryset filtered by the logged-in user.
        """
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the logged-in user to the created todo item.
        """
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        """
        A custom action to mark a todo as completed.
        """
        todo = self.get_object()
        todo.completed = True
        todo.save()
        return Response({'status': 'Todo marked as completed'})
