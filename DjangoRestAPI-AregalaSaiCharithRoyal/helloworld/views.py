from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .filters import BlogPostFilter
from .models import BlogPost
from .permissions import IsOwner
from .serializers import BlogPostSerializer


class BlogPostListCreateView(generics.ListCreateAPIView):
    """Show the logged-in user's posts and let them create a new one."""
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = BlogPostFilter
    search_fields = ["title", "content"]
    ordering_fields = ["id"]
    ordering = ["id"]

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Read, edit, or delete one post belonging to the logged-in user."""
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # A user cannot open another user's post, even if they know its ID.
        return BlogPost.objects.filter(author=self.request.user)
