from django.urls import path
from .views import BlogPostDetailView, BlogPostListCreateView

urlpatterns = [
    path("posts/", BlogPostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/", BlogPostDetailView.as_view(), name="post-detail"),
]
