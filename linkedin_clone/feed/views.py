from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import  IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """Provides `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
