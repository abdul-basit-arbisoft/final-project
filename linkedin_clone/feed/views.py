from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import CanEditDeleteAnyPost, CanEditDeleteOwnPost

class PostViewSet(viewsets.ModelViewSet):
    """Provides `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """Override the permission classes for update and destroy actions."""
        if self.action in ['update', 'partial_update', 'destroy']:
            print("User : ", self.request.user.user_type)
            return [CanEditDeleteAnyPost() if self.request.user.user_type == 'admin' else CanEditDeleteOwnPost()]
