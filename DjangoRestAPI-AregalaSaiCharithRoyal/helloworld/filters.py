import django_filters
from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):
    # Exact date filter, e.g. /api/posts/?created_at=2026-08-29
    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="date")

    class Meta:
        model = BlogPost
        fields = ["created_at"]
