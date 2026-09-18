from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .filters import BlogPostFilter
from .models import BlogPost
from .permissions import IsOwner
from .serializers import BlogPostSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """CRUD endpoint for the signed-in user's own posts."""

    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filterset_class = BlogPostFilter
    search_fields = ["title", "content"]
    ordering_fields = ["id"]
    ordering = ["id"]

    def get_queryset(self):
        # Filtering starts from the current user's posts, so another user's data
        # is never exposed through either the list or detail endpoints.
        return BlogPost.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
